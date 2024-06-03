def nnot(ans):
    if ans == 1:
        return 0
    else:
        return 1


def find_and(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans & arr[i]
    return ans


def find_or(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans | arr[i]
    return ans


def find_nand(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans & arr[i]
    return nnot(ans)


def find_not(arr):
    ans = arr[0]
    return nnot(ans)


def find_nor(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans | arr[i]
    return nnot(ans)


def find_xor(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans ^ arr[i]
    return ans


def find_xnor(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans ^ arr[i]
    return nnot(ans)


def cs1(mighty_raju_list, super_list_gates):
    should_i_continue = True

    while (should_i_continue):

        listA = []
        for i in super_list_gates:
            listA.append(super_list_gates[i]["SimVal"])
        if "" in listA:
            pass
        else:
            return super_list_gates

        for stmts in mighty_raju_list:
            input_container = stmts[-1]
            number_of_input = len(input_container)

            input_value_container = []

            for inp in input_container:
                temp_dictionary = super_list_gates[inp]
                p1 = temp_dictionary['SimVal']
                if p1 != "":
                    input_value_container.append(p1)

            if len(input_value_container) == number_of_input:

                type_of_gate = stmts[1][0].upper()
                output = stmts[0][0]

                if type_of_gate == "AND":
                    res = find_and(input_value_container)
                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"SimVal": res}
                    temp_dic.update(temp_dic_2)

                elif type_of_gate == "NAND":
                    res = find_nand(input_value_container)
                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"SimVal": res}
                    temp_dic.update(temp_dic_2)

                elif type_of_gate == "NOT":
                    res = find_not(input_value_container)
                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"SimVal": res}
                    temp_dic.update(temp_dic_2)

                elif type_of_gate == "OR":
                    res = find_or(input_value_container)
                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"SimVal": res}
                    temp_dic.update(temp_dic_2)

                elif type_of_gate == "NOR":
                    res = find_nor(input_value_container)
                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"SimVal": res}
                    temp_dic.update(temp_dic_2)

                elif type_of_gate == "XOR":
                    res = find_xor(input_value_container)
                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"SimVal": res}
                    temp_dic.update(temp_dic_2)

                elif type_of_gate == "XNOR":
                    res = find_xnor(input_value_container)
                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"SimVal": res}
                    temp_dic.update(temp_dic_2)

                elif type_of_gate == "DFF" or type_of_gate == "BUFF":
                    res = input_value_container[0]
                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"SimVal": res}
                    temp_dic.update(temp_dic_2)

                else:
                    print("No gate found")

def cs2(mighty_raju_list, super_list_gates):
    should_i_continue = True



    while (should_i_continue):

        listA = []
        for i in super_list_gates:
            listA.append(super_list_gates[i]["Status_P"])
        if "Fake" in listA:
            pass
        else:
            return super_list_gates

        for stmts in mighty_raju_list:
            input_list = stmts[-1]
            initial_num_of_inputs = len(stmts[-1])
            if initial_num_of_inputs == 1:
                input_name = stmts[-1][0]
                p0_val = super_list_gates[input_name]["SimVal"]
                status = super_list_gates[input_name]["Status_P"]
                if p0_val != "" and status == "Fake":
                    type_of_gate = stmts[1][0].upper()
                    output = stmts[0][0]
                    input_data = []

                    for inp in input_list:
                        temp_dictionary = super_list_gates[inp]
                        p1 = temp_dictionary['SimVal']
                        if p1 != "":
                            input_data.append(p1)

                    if len(input_data) == 0:
                        pass
                    else:
                        if type_of_gate == "AND":
                            res = find_and(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res,"Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "NAND":
                            res = find_nand(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res,"Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "NOT":
                            res = find_not(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res,"Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "OR":
                            res = find_or(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res,"Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "NOR":
                            res = find_nor(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res,"Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "XOR":
                            res = find_xor(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res,"Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "XNOR":
                            res = find_xnor(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res,"Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "DFF" or type_of_gate == "BUFF":
                            res = input_data[0]
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res,"Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        else:
                            print("No gate found")

                elif p0_val != "" and status == "True":
                    type_of_gate = stmts[1][0].upper()
                    output = stmts[0][0]

                    input_data = []

                    for inp in input_list:
                        temp_dictionary = super_list_gates[inp]
                        p1 = temp_dictionary['SimVal']
                        if p1 != "":
                            input_data.append(p1)

                    if len(input_data) == 0:
                        pass
                    else:
                        if type_of_gate == "AND":
                            res = find_and(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "NAND":
                            res = find_nand(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "NOT":
                            res = find_not(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "OR":
                            res = find_or(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "NOR":
                            res = find_nor(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "XOR":
                            res = find_xor(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "XNOR":
                            res = find_xnor(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "DFF" or type_of_gate == "BUFF":
                            res = input_data[0]
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            temp_dic.update(temp_dic_2)

                        else:
                            print("No gate found")

                else:
                    pass
            else:
                # Status_P Checker
                temp0 = []
                for ii in input_list:
                    temp0.append(super_list_gates[ii]["Status_P"])

                output = stmts[0][0]
                prestored_value_output = super_list_gates[output]["SimVal"]

                if "Fake" in temp0 and prestored_value_output != "":
                    type_of_gate = stmts[1][0].upper()
                    output = stmts[0][0]

                    input_data = []

                    for inp in input_list:
                        temp_dictionary = super_list_gates[inp]
                        p1 = temp_dictionary['SimVal']
                        if p1 != "":
                            input_data.append(p1)

                    if len(input_data) == 0:
                        pass
                    else:

                        if type_of_gate == "AND":
                            res = find_and(input_data)
                            temp_dic = super_list_gates[output]
                            if prestored_value_output == res:
                                temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            else:
                                temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "NAND":
                            res = find_nand(input_data)
                            temp_dic = super_list_gates[output]
                            if prestored_value_output == res:
                                temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            else:
                                temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "NOT":
                            res = find_not(input_data)
                            temp_dic = super_list_gates[output]
                            if prestored_value_output == res:
                                temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            else:
                                temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "OR":
                            res = find_or(input_data)
                            temp_dic = super_list_gates[output]
                            if prestored_value_output == res:
                                temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            else:
                                temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "NOR":
                            res = find_nor(input_data)
                            temp_dic = super_list_gates[output]
                            if prestored_value_output == res:
                                temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            else:
                                temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "XOR":
                            res = find_xor(input_data)
                            temp_dic = super_list_gates[output]
                            if prestored_value_output == res:
                                temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            else:
                                temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "XNOR":
                            res = find_xnor(input_data)
                            temp_dic = super_list_gates[output]
                            if prestored_value_output == res:
                                temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            else:
                                temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "DFF" or type_of_gate == "BUFF":
                            res = input_data[0]
                            temp_dic = super_list_gates[output]
                            if prestored_value_output == res:
                                temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                            else:
                                temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        else:
                            print("No gate found")

                elif "Fake" in temp0 and prestored_value_output=="":

                    type_of_gate = stmts[1][0].upper()
                    output = stmts[0][0]
                    p0_val = []
                    p1_val = []

                    input_data = []

                    for inp in input_list:
                        temp_dictionary = super_list_gates[inp]
                        p1 = temp_dictionary['SimVal']
                        if p1 != "":
                            input_data.append(p1)

                    if len(input_data) == 0:
                        pass
                    else:


                        if type_of_gate == "AND":
                            res = find_and(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "NAND":
                            res = find_nand(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "NOT":
                            res = find_not(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "OR":
                            res = find_or(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "NOR":
                            res = find_nor(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "XOR":
                            res = find_xor(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "XNOR":
                            res = find_xnor(input_data)
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        elif type_of_gate == "DFF" or type_of_gate == "BUFF":
                            res = input_data[0]
                            temp_dic = super_list_gates[output]
                            temp_dic_2 = {"SimVal": res, "Status_P": "Fake"}
                            temp_dic.update(temp_dic_2)

                        else:
                            print("No gate found")

                else:

                    type_of_gate = stmts[1][0].upper()
                    output = stmts[0][0]

                    input_data = []

                    for inp in input_list:
                        temp_dictionary = super_list_gates[inp]
                        p1 = temp_dictionary['SimVal']
                        if p1 != "":
                            input_data.append(p1)


                    if type_of_gate == "AND":
                        res = find_and(input_data)
                        temp_dic = super_list_gates[output]
                        temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                        temp_dic.update(temp_dic_2)

                    elif type_of_gate == "NAND":
                        res = find_nand(input_data)
                        temp_dic = super_list_gates[output]
                        temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                        temp_dic.update(temp_dic_2)

                    elif type_of_gate == "NOT":
                        res = find_not(input_data)
                        temp_dic = super_list_gates[output]
                        temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                        temp_dic.update(temp_dic_2)

                    elif type_of_gate == "OR":
                        res = find_or(input_data)
                        temp_dic = super_list_gates[output]
                        temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                        temp_dic.update(temp_dic_2)

                    elif type_of_gate == "NOR":
                        res = find_nor(input_data)
                        temp_dic = super_list_gates[output]
                        temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                        temp_dic.update(temp_dic_2)

                    elif type_of_gate == "XOR":
                        res = find_xor(input_data)
                        temp_dic = super_list_gates[output]
                        temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                        temp_dic.update(temp_dic_2)

                    elif type_of_gate == "XNOR":
                        res = find_xnor(input_data)
                        temp_dic = super_list_gates[output]
                        temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                        temp_dic.update(temp_dic_2)

                    elif type_of_gate == "DFF" or type_of_gate == "BUFF":
                        res = input_data[0]
                        temp_dic = super_list_gates[output]
                        temp_dic_2 = {"SimVal": res, "Status_P": "True"}
                        temp_dic.update(temp_dic_2)

                    else:
                        print("No gate found")

