import Gates
import bench_session
import uuid


class wire:
    __in = None
    __out = None
    __uniqueID = None

    def __init__(self):
        self.__uniqueID = uuid.uuid4()
        self.__out = []
        self.__in = []
        pass

    def __operate(self):
       pass

    def set_in(self, in_port):
        self.__in = in_port

    def add_out(self, out_port):
        self.__out.extend(out_port)

    def remove_out(self, out_port):
        self.__out.remove(out_port)

    def get_endpoints(self):
        return self.__in, self.__out

    def get_in(self):
        return self.__in

    def get_out(self):
        return self.__out

    def get_unique_id(self):
        return self.__uniqueID


class Module:
    _Input_Pins = None
    _Output_Pins = None
    _Internal_Wires = None
    _Internal_Gates = None
    _Module_name = None
    _io_pin_name = None
    _supplier = None

    def __init__(self, supplier):
        self._Input_Pins = dict()
        self._Output_Pins = dict()
        self._Internal_Wires = dict()
        self._Internal_Gates = dict()
        self._io_pin_name = []
        self._supplier = supplier

    def parse(self, module_desc):

        self.__onmodule_decl(module_desc)
        self.__onmodule_input(module_desc)
        self.__onmodule_output(module_desc)
        self.__onmodule_wire(module_desc)
        self.__createVDDGND()

        for instruction in module_desc.get_instructions():
            self.__handle_module_integration(instruction)

    def __createVDDGND(self):
        self._Input_Pins['VDD'] = []
        self._Input_Pins['GND'] = []

    def getInputs(self):
        return self._Input_Pins

    def getOutputs(self):
        return self._Output_Pins

    def getWires(self):
        return self._Internal_Wires

    def getInternalGates(self):
        return self._Internal_Gates

    def __onmodule_decl(self, module_desc):
        self._Module_name = module_desc.get_name()
        self._io_pin_name = module_desc.get_ordered_arg()

    def __onmodule_input(self, module_desc):
        for pins in module_desc.get_inputs():
            self._Input_Pins[pins] = []

    def __onmodule_output(self, module_desc):
        for pins in module_desc.get_outputs():
            self._Output_Pins[pins] = []

    def __onmodule_wire(self, module_desc):
        for i in module_desc.get_wires():
            self._Internal_Wires[i] = wire()

    def __handle_module_integration(self, instr):
        module_type = instr.get_module_type()
        module_name = instr.get_module_name()
        module_key = instr.get_ordered_arg_primitive()

        mappings = instr.get_arg_map()

        if self.is_module_primitive(module_type):
            temp_gate = None

            if module_type == 'DFF':
                temp_gate = Gates.DFF(module_name, module_key)
            elif module_type == 'OR':
                temp_gate = Gates.ORGate(module_name, module_key)
            elif module_type == 'NOT':
                temp_gate = Gates.NOTGate(module_name, module_key)
            elif module_type == 'AND':
                temp_gate = Gates.ANDGate(module_name, module_key)
            elif module_type == 'NAND':
                temp_gate = Gates.NANDGate(module_name, module_key)
            elif module_type == 'NOR':
                temp_gate = Gates.NORGate(module_name, module_key)
            elif module_type == 'XOR':
                temp_gate = Gates.XORGate(module_name, module_key)
            elif module_type == 'XNOR':
                temp_gate = Gates.XNORGate(module_name, module_key)
            elif module_type == 'BUFF':
                temp_gate = Gates.BUFF(module_name, module_key)

            self._Internal_Gates[module_name + "_" + str(temp_gate.get_unique_id())] = temp_gate

            for k in mappings.keys():
                if k in temp_gate.get_inputs().keys():
                    if mappings[k] in self._Input_Pins.keys():
                        self._Input_Pins[mappings[k]].extend(temp_gate.get_inputs()[k])
                    elif mappings[k] in self._Internal_Wires.keys():
                        self._Internal_Wires[mappings[k]].add_out(temp_gate.get_inputs()[k])
                    elif mappings[k] in self._Output_Pins.keys():
                        self._Output_Pins[mappings[k]].extend(temp_gate.get_inputs()[k])

                elif k in temp_gate.get_outputs().keys():
                    if mappings[k] in self._Output_Pins.keys():
                        self._Output_Pins[mappings[k]].extend(temp_gate.get_outputs()[k])
                    elif mappings[k] in self._Internal_Wires.keys():
                        self._Internal_Wires[mappings[k]].set_in(temp_gate.get_outputs()[k])

        else:
            internal_module = Module(self._supplier)
            internal_module.parse(self._supplier.get_module(module_type))

            for i in internal_module.getInternalGates().keys():
                self._Internal_Gates[internal_module.getInternalGates()[i].get_name() + '_' + str(
                    internal_module.getInternalGates()[i].get_unique_id())] = internal_module.getInternalGates()[i]

            for i in internal_module.getWires().keys():
                self._Internal_Wires[i + "_" + str(internal_module.getWires()[i].get_unique_id())] = internal_module.getWires()[i]

            for k in mappings.keys():
                if k in internal_module.getInputs().keys():
                    if mappings[k] in self._Input_Pins.keys():
                        self._Input_Pins[mappings[k]].extend(internal_module.getInputs()[k])
                    elif mappings[k] in self._Internal_Wires.keys():
                        self._Internal_Wires[mappings[k]].add_out(internal_module.getInputs()[k])
                    elif mappings[k] in self._Output_Pins.keys():
                        self._Output_Pins[mappings[k]].extend(internal_module.getInputs()[k])

                elif k in internal_module.getOutputs().keys():
                    if mappings[k] in self._Output_Pins.keys():
                        self._Output_Pins[mappings[k]].extend(internal_module.getOutputs()[k])
                    elif mappings[k] in self._Internal_Wires.keys():
                        self._Internal_Wires[mappings[k]].set_in(internal_module.getOutputs()[k])

    def is_module_primitive(self, module):
        return module in ['AND', 'OR', 'NOT', 'XOR', 'NAND', 'NOR', 'XOR', 'XNOR', 'DFF', 'BUFF']

    def print_module(self):
        module_p = str()
        module_p += 'Module \'' + self._Module_name + '\'\n'
        module_p += 'Module Info :\n'

        module_p += 'INPUT PINS\n' + '------------\n'
        for i in self._Input_Pins.keys():
            module_p += i + ' ->' + str(self._Input_Pins[i]) + '\n'
        module_p += '\n'

        module_p += 'OUTPUT PINS\n' + '------------\n'
        for i in self._Output_Pins.keys():
            module_p += i + ' ->' + str(self._Output_Pins[i]) + '\n'
        module_p += '\n'

        module_p += 'WIRES\n' + '------\n'
        for i in self._Internal_Wires.keys():
            module_p += i + ' -> ' + str(self._Internal_Wires[i]) + 'Connecting IN of ' + str(self._Internal_Wires[i].get_out()) + 'with OUT of ' + str(self._Internal_Wires[i].get_in()) + '\n'
        module_p += '\n'

        module_p += 'INTERNAL_GATES\n' + '---------------\n'
        for i in self.getInternalGates().keys():
            module_p += str(self.getInternalGates()[i]) + ' -> ' + self.getInternalGates()[i].get_name() + '----> INPUT_PINS [ '
            for j in self.getInternalGates()[i].get_inputs().keys():
                module_p += '\'' + j + '\': ' + str(self.getInternalGates()[i].get_inputs()[j][0])
            module_p += ' ] OUTPUT_PINS [ '
            for j in self.getInternalGates()[i].get_outputs().keys():
                module_p += '\'' + j + '\': ' + str(self.getInternalGates()[i].get_outputs()[j][0])
            module_p += ' ]\n'
        print(module_p)

    def get_bench_file(self):
        #self.print_module()
        output = str()
        output += '//Module name: ' + self._Module_name + '\n\n'

        session = bench_session.bench_session(self, 'I', 'U', 'W')
        mapping = session.get_map()

        for i in self.getInputs().keys():
            if i == 'VDD' or i == 'GND':
                continue
            output += 'INPUT(' + (mapping[self.getInputs()[i][0]] if len(self.getInputs()[i]) > 0 else mapping['!UNCONNECTED'+i]) + ')\n'
        output += '\n'

        for i in self.getOutputs().keys():
            output += 'OUTPUT(' + (mapping[self.getOutputs()[i][0]] if len(self.getOutputs()[i]) > 0 else mapping['!UNCONNECTED'+i]) + ')\n'
        output += '\n'

        for i in self.getInternalGates().keys():
            output += (mapping[self.getInternalGates()[i].get_outputs()[list(self.getInternalGates()[i].get_outputs())[0]][0]] if self.getInternalGates()[i].get_outputs()[list(self.getInternalGates()[i].get_outputs())[0]][0] in mapping else '!UNCONNECTED' ) + ' = ' + self.getInternalGates()[i].get_type() + '('
            pin_keys = list(self.getInternalGates()[i].get_inputs().keys())
            for pins_i in range(len(pin_keys)):
                output += (mapping[self.getInternalGates()[i].get_inputs()[pin_keys[pins_i]][0]] if self.getInternalGates()[i].get_inputs()[pin_keys[pins_i]][0] in mapping else '!UNCONNECTED')
                if pins_i != len(self.getInternalGates()[i].get_inputs().keys()) - 1:
                    output += ','
            output += ')\n'

        return output
