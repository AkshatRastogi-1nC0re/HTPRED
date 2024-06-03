import uuid


class instruction:

    __supplier = None
    __parent_module = None
    __module_type = None
    __module_name = None

    _arg_map = None
    _ordered_arg_primitive = None

    def __init__(self,module_supplier,parent_module,instr):
        self.__supplier = module_supplier
        self.__parent_module = parent_module
        self._arg_map = dict()
        self._ordered_arg_primitive = []
        self.__parse(instr)

    def get_module_type(self):
        return self.__module_type

    def get_module_name(self):
        return self.__module_name

    def get_ordered_arg_primitive(self):
        return self._ordered_arg_primitive

    def get_arg_map(self):
        return self._arg_map

    def __parse(self,instr):
        if len(instr) > 7 and instr[:6] == 'assign':
            instr = self.__create_buffer(instr.strip())

        ins_split_1 = instr.split(' ',1)
        self.__module_type = ins_split_1[0].strip()
        name_param = ins_split_1[1].strip()
        name_end = -1
        for i in range(len(name_param)):
            if name_param[i] == '(':
                name_end = i
                break

        self.__module_name = name_param[:name_end]
        arg_str = name_param[name_end:].strip()
        self.break_args(arg_str[1:len(arg_str)-1])

    def __create_buffer(self, line):
        line = line[6:]
        line = [i.strip() for i in line.split('=')]
        return 'BUFF buff' + str(uuid.uuid4()) + ' (.A(' + line[1] + '), .Y(' + line[0] + '))'

    def break_args(self,arg_str):
        brace_open = False
        modified_arg_str = str()
        for i in arg_str:
            if i == '{':
                brace_open = True
            elif i == '}':
                brace_open = False
            elif i == ',' and brace_open:
                modified_arg_str += '%'
                continue
            modified_arg_str += i

        map_str_dict = [i.strip() for i in modified_arg_str.split(',')]
        map_str_dict = self.__fix_positional_args(map_str_dict)

        for individual_map in map_str_dict:
            key,value = self.__split_kv(individual_map)
            if len(value) == 1:
                self._arg_map[key] = value[0]
            else:
                arr_map = self.__supplier.get_module(self.__module_type).get_iwo_value_list(key)
                for i in range(len(arr_map)):
                    self._arg_map[arr_map[i]] = value[i]

    def __fix_positional_args(self,to_fix):
        if to_fix[0].find('.') != -1:
            return to_fix

        else:
            fixed = []
            args = self.__supplier.get_module(self.__module_type).get_ordered_arg()
            for i in range(len(to_fix)):
                fixed.append('.'+args[i]+' ('+to_fix[i]+')')
            return fixed

    def __split_kv(self,individual_map):
        dot, brac_o, brac_c = -1,-1,-1
        for i in range(len(individual_map)):
            if individual_map[i] == '.':
                dot = i
            elif individual_map[i] == '(':
                brac_o = i
            elif individual_map[i] == ')':
                brac_c = i

        key = individual_map[dot+1:brac_o].strip()
        value = individual_map[brac_o+1:brac_c].strip()
        if len(value) == 0:
            value = '{}'

        if value[0] == '{' and value[-1] == '}':
            value = [i.strip() for i in value[1:-1].split('%')]

        value = self.__expand_value(value)
        self._ordered_arg_primitive.append(key)
        return key,value

    def __expand_value(self,value):
        if not isinstance(value,list):
            if value.find('\'b') != -1:
                return self.__expand_value([value])
            else:
                return self.__parent_module.get_iwo_value_list(value)

        else:
            argv = []
            for i in value:
                if i.find('\'b') == -1:
                    argv.extend(self.__expand_value(i))
                else:
                    bit_cv = i.split('\'b')
                    bit_arg = []
                    for it in range(int(bit_cv[0])):
                        bit_arg.append('VDD' if bit_cv[1][it] == '1' else 'GND')
                    argv.extend(bit_arg)
            return argv


class module_description:

    __module_name = None
    __arg_order = None
    __inputs = None
    __outputs = None
    __wires = None
    __instructions = None
    __supplier = None

    def __init__(self,supplier,module_body):
        self.__supplier = supplier
        self.__inputs = dict()
        self.__outputs = dict()
        self.__wires = dict()
        self.__instructions = []
        self.__parse_module(module_body)

    def get_name(self):
        return self.__module_name

    def __parse_module(self,module_body):
        for line in module_body.split('\n'):
            if len(line) > 7 and line[:7] == 'module ':
                self.__handle_header(line[7:])
            elif len(line) > 5 and line[:5] == 'input':
                self.__handle_iow(line[5:].strip(),self.__inputs)
            elif len(line) > 6 and line[:6] == 'output':
                self.__handle_iow(line[6:].strip(),self.__outputs)
            elif len(line) > 4 and line[:4] == 'wire':
                self.__handle_iow(line[4:].strip(),self.__wires)
            elif line == 'endmodule':
                return
            else:
                self.__parse_instruction(line)

    def __handle_header(self,param):
        brac_o,brac_e = -1,-1
        for i in range(len(param)):
            if param[i] == '(' and brac_o == -1:
                brac_o = i
            elif param[i] == ')':
                brac_e = i
        self.__module_name = param[:brac_o].strip()
        args = param[brac_o+1:brac_e]
        args = [i.strip() for i in args.split(',')]
        self.__arg_order = args

    def __handle_iow(self,param,objset):
        arr_o,arr_e,colon,is_array = -1,-1,-1,False
        for i in range(len(param)):
            if arr_e != -1:
                if arr_o == -1 or colon == -1:
                    raise Exception("Syntax error")
                else:
                    is_array = True
                    break
            if param[i] == '[':
                arr_o = i
            elif param[i] == ']':
                arr_e = i
            elif param[i] == ':':
                colon = i

        if is_array:
            start_index = int(param[arr_o+1:colon])
            end_index = int(param[colon+1:arr_e])
            arg_list = [i.strip() for i in param[arr_e+1:].split(',')]
            for arg in arg_list:
                if arg not in objset:
                    objset[arg] = []
                for i in range(start_index , end_index + (1 if start_index <= end_index else -1) , (1 if start_index <= end_index else -1)):
                    app_str = arg+'['+str(i)+']'
                    if objset is self.__wires and ((arg in self.__inputs and app_str in self.__inputs[arg]) or (arg in self.__outputs and app_str in self.__outputs[arg])):
                        continue
                    objset[arg].append(app_str)
                if not len(objset[arg]):
                    del objset[arg]
        else:
            arg_list = [i.strip() for i in param.split(',')]
            for arg in arg_list:
                if (objset is self.__wires) and ((arg in self.__inputs and arg in self.__inputs[arg]) or (arg in self.__outputs and arg in self.__outputs[arg])):
                    continue
                objset[arg] = [arg]

    def __parse_instruction(self,instr):
        self.__instructions.append(instruction(self.__supplier,self,instr))

    def get_ordered_arg(self):
        return self.__arg_order

    def get_expanded_ordered_arg(self,arg_order=None):
        ret_list = []
        if arg_order is None:
            arg_order = self.get_ordered_arg()
        for i in arg_order:
            if i in self.__inputs:
                ret_list.extend(self.__inputs[i])
            elif i in self.__outputs:
                ret_list.extend(self.__outputs[i])
        return ret_list

    def get_inputs(self):
        ret_list = []
        for i in self.__inputs.keys():
            ret_list.extend(self.__inputs[i])
        return ret_list

    def get_outputs(self):
        ret_list = []
        for i in self.__outputs.keys():
            ret_list.extend(self.__outputs[i])
        return ret_list

    def get_wires(self):
        ret_list = []
        for i in self.__wires.keys():
            ret_list.extend(self.__wires[i])
        return ret_list

    def get_iwo_value_list(self,pin):
        if pin == '':
            return [None]
        if pin in self.__inputs:
            return self.__inputs[pin]
        elif pin in self.__outputs:
            return self.__outputs[pin]
        elif pin in self.__wires:
            return self.__wires[pin]
        else:
            brac_o,brac_c,colon = -1,-1,-1
            for i in range(len(pin)):
                if pin[i] == '[':
                    brac_o = i
                if pin[i] == ']':
                    brac_c = i
                if pin[i] == ':':
                    colon = i
            if brac_o != -1 and brac_c != -1:
                p_name = pin[:brac_o]
                if colon != -1:
                    start = int(pin[brac_o+1:colon])
                    end = int(pin[colon+1:brac_c])
                    arr_subset = []
                    for i in range(start,end + (1 if start<=end else -1), (1 if start<=end else -1)):
                        arr_subset.append(p_name+'['+str(i)+']')
                    return arr_subset
                else:
                    #individual elements
                    if p_name in self.__inputs:
                        if pin in self.__inputs[p_name]:
                            return [pin]
                    elif p_name in self.__outputs:
                        if pin in self.__outputs[p_name]:
                            return [pin]
                    elif p_name in self.__wires:
                        if pin in self.__wires[p_name]:
                            return [pin]
                    else:
                        return [None]
            else:
                return [None]

    def get_instructions(self):
        return self.__instructions



