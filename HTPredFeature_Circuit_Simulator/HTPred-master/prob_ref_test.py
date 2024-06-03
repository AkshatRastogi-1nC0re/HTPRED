def prob1(mighty_raju_list, super_list_gates):
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
                p0_val = super_list_gates[input_name]["P0"]
                p1_val = super_list_gates[input_name]["P1"]
                status = super_list_gates[input_name]["Status_P"]
                if p0_val != "" and p1_val != "" and status == "Fake":
                    type_of_gate = stmts[1][0].upper()
                    output = stmts[0][0]
                    input_data = []

                    for inp in input_list:
                        temp_dictionary = super_list_gates[inp]
                        p1 = temp_dictionary['P1']
                        p0 = temp_dictionary['P0']
                        if p0 != "" and p1 != "":
                            input_data.append([p0, p1])

                    if len(input_data) == 0:
                        pass
                    else:
                        if type_of_gate == "AND":
                            p1_mul = 1
                            for i in input_data:
                                p1_mul = p1_mul * i[1]
                            p1 = p1_mul
                            p0 = 1 - p1
                            super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "Fake"})
                        elif type_of_gate == "NOT" or type_of_gate == "BUFF":
                            p1 = input_data[0][1]
                            p0 = input_data[0][0]
                            super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "Fake"})
                        elif type_of_gate == "DFF":
                            p1_mul = 1
                            for i in input_data:
                                p1_mul = p1_mul * i[1]
                            p1 = p1_mul
                            p0 = 1 - p1
                            super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "Fake"})
                        elif type_of_gate == "NAND":
                            p1_mul = 1
                            for i in input_data:
                                p1_mul = p1_mul * i[1]
                            p1 = p1_mul
                            p0 = 1 - p1
                            super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "Fake"})
                        elif type_of_gate == "OR":
                            p0_mul = 1
                            for i in input_data:
                                p0_mul = p0_mul * i[0]
                            p0 = p0_mul
                            p1 = 1 - p0
                            super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "Fake"})
                        elif type_of_gate == "NOR":
                            p0_mul = 1
                            for i in input_data:
                                p0_mul = p0_mul * i[0]
                            p0 = p0_mul
                            p1 = 1 - p0
                            super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "Fake"})
                        elif type_of_gate == "XOR":
                            t1 = 1
                            t2 = 1
                            for i in input_data:
                                t1 = t1 * i[0]
                                t2 = t2 * i[1]
                            p0 = t1 + t2
                            p1 = 1 - p0
                            super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "Fake"})
                        elif type_of_gate == "XNOR":
                            t1 = 1
                            t2 = 1
                            for i in input_data:
                                t1 = t1 * i[0]
                                t2 = t2 * i[1]

                            p0 = t1 + t2
                            p1 = 1 - p0

                            super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "Fake"})

                elif p0_val != "" and p1_val != "" and status == "True":
                    type_of_gate = stmts[1][0].upper()
                    output = stmts[0][0]

                    input_data = []

                    for inp in input_list:
                        temp_dictionary = super_list_gates[inp]
                        p1 = temp_dictionary['P1']
                        p0 = temp_dictionary['P0']
                        if p0 != "" and p1 != "":
                            input_data.append([p0, p1])

                    if len(input_data) == 0:
                        pass
                    else:
                        if type_of_gate == "AND":
                            p1_mul = 1
                            for i in input_data:
                                p1_mul = p1_mul * i[1]
                            p1 = p1_mul
                            p0 = 1 - p1
                            super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "True"})
                        elif type_of_gate == "NOT" or type_of_gate == "BUFF":

                            p1 = input_data[0][1]
                            p0 = input_data[0][0]
                            super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "True"})
                        elif type_of_gate == "DFF":
                            p1_mul = 1
                            for i in input_data:
                                p1_mul = p1_mul * i[1]
                            p1 = p1_mul
                            p0 = 1 - p1
                            super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "True"})
                        elif type_of_gate == "NAND":
                            p1_mul = 1
                            for i in input_data:
                                p1_mul = p1_mul * i[1]
                            p1 = p1_mul
                            p0 = 1 - p1
                            super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "True"})
                        elif type_of_gate == "OR":
                            p0_mul = 1
                            for i in input_data:
                                p0_mul = p0_mul * i[0]
                            p0 = p0_mul
                            p1 = 1 - p0
                            super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "True"})
                        elif type_of_gate == "NOR":
                            p0_mul = 1
                            for i in input_data:
                                p0_mul = p0_mul * i[0]
                            p0 = p0_mul
                            p1 = 1 - p0
                            super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "True"})
                        elif type_of_gate == "XOR":
                            t1 = 1
                            t2 = 1
                            for i in input_data:
                                t1 = t1 * i[0]
                                t2 = t2 * i[1]
                            p0 = t1 + t2
                            p1 = 1 - p0
                            super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "True"})
                        elif type_of_gate == "XNOR":
                            t1 = 1
                            t2 = 1
                            for i in input_data:
                                t1 = t1 * i[0]
                                t2 = t2 * i[1]

                            p0 = t1 + t2
                            p1 = 1 - p0
                            super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "True"})

                else:
                    pass
            else:
                # Status_P Checker
                temp0 = []
                for ii in input_list:
                    temp0.append(super_list_gates[ii]["Status_P"])

                output = stmts[0][0]
                prestored_value_output = [super_list_gates[output]["P0"], super_list_gates[output]["P1"]]

                if "Fake" in temp0 and "" not in prestored_value_output:
                    type_of_gate = stmts[1][0].upper()
                    output = stmts[0][0]
                    p0_val = []
                    p1_val = []

                    input_data = []

                    for inp in input_list:
                        temp_dictionary = super_list_gates[inp]
                        p1 = temp_dictionary['P1']
                        p0 = temp_dictionary['P0']
                        if p0 != "" and p1 != "":
                            input_data.append([p0, p1])

                    if len(input_data) == 0:
                        pass
                    else:

                        for i in range(len(input_data)):
                            list_of_inp = input_data[i]
                            p0 = list_of_inp[0]
                            p1 = list_of_inp[1]
                            p0_val.append(p0)
                            p1_val.append(p1)

                        if type_of_gate == "AND":
                            p1_mul = 1
                            for i in input_data:
                                p1_mul = p1_mul * i[1]
                            p1 = p1_mul
                            p0 = 1 - p1
                            if prestored_value_output == [p0, p1]:
                                super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "True"})
                            else:
                                super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "Fake"})

                        elif type_of_gate == "NOT" or type_of_gate == "BUFF":

                            p1 = input_data[0][1]
                            p0 = input_data[0][0]
                            if prestored_value_output == [p1, p0]:
                                super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "True"})
                            else:
                                super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "Fake"})

                        elif type_of_gate == "DFF":
                            p1_mul = 1
                            for i in input_data:
                                p1_mul = p1_mul * i[1]
                            p1 = p1_mul
                            p0 = 1 - p1
                            if prestored_value_output == [p0, p1]:
                                super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "True"})
                            else:
                                super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "Fake"})
                        elif type_of_gate == "NAND":
                            p1_mul = 1
                            for i in input_data:
                                p1_mul = p1_mul * i[1]
                            p1 = p1_mul
                            p0 = 1 - p1
                            if prestored_value_output == [p1, p0]:
                                super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "True"})
                            else:
                                super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "Fake"})
                        elif type_of_gate == "OR":
                            p0_mul = 1
                            for i in input_data:
                                p0_mul = p0_mul * i[0]
                            p0 = p0_mul
                            p1 = 1 - p0
                            if prestored_value_output == [p0, p1]:
                                super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "True"})
                            else:
                                super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "Fake"})
                        elif type_of_gate == "NOR":
                            p0_mul = 1
                            for i in input_data:
                                p0_mul = p0_mul * i[0]
                            p0 = p0_mul
                            p1 = 1 - p0
                            if prestored_value_output == [p1, p0]:
                                super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "True"})
                            else:
                                super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "Fake"})
                        elif type_of_gate == "XOR":
                            t1 = 1
                            t2 = 1
                            for i in input_data:
                                t1 = t1 * i[0]
                                t2 = t2 * i[1]
                            p0 = t1 + t2
                            p1 = 1 - p0
                            if prestored_value_output == [p0, p1]:
                                super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "True"})
                            else:
                                super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "Fake"})
                        elif type_of_gate == "XNOR":
                            t1 = 1
                            t2 = 1
                            for i in input_data:
                                t1 = t1 * i[0]
                                t2 = t2 * i[1]

                            p0 = t1 + t2
                            p1 = 1 - p0
                            if prestored_value_output == [p0, p1]:
                                super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "True"})
                            else:
                                super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "Fake"})

                elif "Fake" in temp0 and "" in prestored_value_output:

                    type_of_gate = stmts[1][0].upper()
                    output = stmts[0][0]
                    p0_val = []
                    p1_val = []

                    input_data = []

                    for inp in input_list:
                        temp_dictionary = super_list_gates[inp]
                        p1 = temp_dictionary['P1']
                        p0 = temp_dictionary['P0']
                        if p0 != "" and p1 != "":
                            input_data.append([p0, p1])

                    if len(input_data) == 0:
                        pass
                    else:

                        for i in range(len(input_data)):
                            list_of_inp = input_data[i]
                            p0 = list_of_inp[0]
                            p1 = list_of_inp[1]
                            p0_val.append(p0)
                            p1_val.append(p1)

                        if type_of_gate == "AND":
                            p1_mul = 1
                            for i in input_data:
                                p1_mul = p1_mul * i[1]
                            p1 = p1_mul
                            p0 = 1 - p1
                            super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "Fake"})
                        elif type_of_gate == "NOT" or type_of_gate == "BUFF":

                            p1 = input_data[0][1]
                            p0 = input_data[0][0]
                            super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "Fake"})
                        elif type_of_gate == "DFF":
                            p1_mul = 1
                            for i in input_data:
                                p1_mul = p1_mul * i[1]
                            p1 = p1_mul
                            p0 = 1 - p1
                            super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "Fake"})
                        elif type_of_gate == "NAND":
                            p1_mul = 1
                            for i in input_data:
                                p1_mul = p1_mul * i[1]
                            p1 = p1_mul
                            p0 = 1 - p1
                            super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "Fake"})
                        elif type_of_gate == "OR":
                            p0_mul = 1
                            for i in input_data:
                                p0_mul = p0_mul * i[0]
                            p0 = p0_mul
                            p1 = 1 - p0
                            super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "Fake"})
                        elif type_of_gate == "NOR":
                            p0_mul = 1
                            for i in input_data:
                                p0_mul = p0_mul * i[0]
                            p0 = p0_mul
                            p1 = 1 - p0
                            super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "Fake"})
                        elif type_of_gate == "XOR":
                            t1 = 1
                            t2 = 1
                            for i in input_data:
                                t1 = t1 * i[0]
                                t2 = t2 * i[1]
                            p0 = t1 + t2
                            p1 = 1 - p0
                            super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "Fake"})
                        elif type_of_gate == "XNOR":
                            t1 = 1
                            t2 = 1
                            for i in input_data:
                                t1 = t1 * i[0]
                                t2 = t2 * i[1]
                            p0 = t1 + t2
                            p1 = 1 - p0
                            super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "Fake"})

                else:

                    type_of_gate = stmts[1][0].upper()
                    output = stmts[0][0]
                    p0_val = []
                    p1_val = []

                    input_data = []

                    for inp in input_list:
                        temp_dictionary = super_list_gates[inp]
                        p1 = temp_dictionary['P1']
                        p0 = temp_dictionary['P0']
                        if p0 != "" and p1 != "":
                            input_data.append([p0, p1])

                    for i in range(len(input_data)):
                        list_of_inp = input_data[i]
                        p0 = list_of_inp[0]
                        p1 = list_of_inp[1]
                        p0_val.append(p0)
                        p1_val.append(p1)

                    if type_of_gate == "AND":
                        p1_mul = 1
                        for i in input_data:
                            p1_mul = p1_mul * i[1]
                        p1 = p1_mul
                        p0 = 1 - p1
                        super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "True"})
                    elif type_of_gate == "NOT" or type_of_gate == "BUFF":

                        p1 = input_data[0][1]
                        p0 = input_data[0][0]
                        super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "True"})
                    elif type_of_gate == "DFF":
                        p1_mul = 1
                        for i in input_data:
                            p1_mul = p1_mul * i[1]
                        p1 = p1_mul
                        p0 = 1 - p1
                        super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "True"})
                    elif type_of_gate == "NAND":
                        p1_mul = 1
                        for i in input_data:
                            p1_mul = p1_mul * i[1]
                        p1 = p1_mul
                        p0 = 1 - p1
                        super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "True"})
                    elif type_of_gate == "OR":
                        p0_mul = 1
                        for i in input_data:
                            p0_mul = p0_mul * i[0]
                        p0 = p0_mul
                        p1 = 1 - p0
                        super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "True"})
                    elif type_of_gate == "NOR":
                        p0_mul = 1
                        for i in input_data:
                            p0_mul = p0_mul * i[0]
                        p0 = p0_mul
                        p1 = 1 - p0
                        super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "True"})
                    elif type_of_gate == "XOR":
                        t1 = 1
                        t2 = 1
                        for i in input_data:
                            t1 = t1 * i[0]
                            t2 = t2 * i[1]
                        p0 = t1 + t2
                        p1 = 1 - p0
                        super_list_gates[output].update({"P0": p0, "P1": p1, "Status_P": "True"})
                    elif type_of_gate == "XNOR":
                        t1 = 1
                        t2 = 1
                        for i in input_data:
                            t1 = t1 * i[0]
                            t2 = t2 * i[1]

                        p0 = t1 + t2
                        p1 = 1 - p0

                        super_list_gates[output].update({"P0": p1, "P1": p0, "Status_P": "True"})


def prob2(mighty_raju_list, super_list_gates):

    should_i_continue = True

    while(should_i_continue):

        listA = []
        for i in super_list_gates:
            listA.append(super_list_gates[i]["P0"])
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
                p1 = temp_dictionary['P1']
                p0 = temp_dictionary['P0']
                if p0 != "" and p1 != "":
                    input_value_container.append([p0,p1])

            if len(input_value_container) == number_of_input:

                type_of_gate = stmts[1][0].upper()
                output = stmts[0][0]
                p0_val = []
                p1_val = []

                for i in range(len(input_value_container)):
                    list_of_inp = input_value_container[i]
                    p0 = list_of_inp[0]
                    p1 = list_of_inp[1]
                    p0_val.append(p0)
                    p1_val.append(p1)

                if type_of_gate == "AND":
                    p1_mul = 1
                    for i in input_value_container:
                        p1_mul = p1_mul * i[1]
                    p1 = p1_mul
                    p0 = 1 - p1

                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"P0": p0, "P1": p1}
                    temp_dic.update(temp_dic_2)

                elif type_of_gate == "NAND":
                    p1_mul = 1
                    for i in input_value_container:
                        p1_mul = p1_mul * i[1]
                    p1 = p1_mul
                    p0 = 1 - p1

                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"P0": p1, "P1": p0}
                    temp_dic.update(temp_dic_2)

                elif type_of_gate == "NOT" or type_of_gate == "BUFF":

                    p1 = input_value_container[0][1]
                    p0 = input_value_container[0][0]

                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"P0": p1, "P1": p0}
                    temp_dic.update(temp_dic_2)

                elif type_of_gate == "OR":
                    p0_mul = 1
                    for i in input_value_container:
                        p0_mul = p0_mul * i[0]
                    p0 = p0_mul
                    p1 = 1 - p0

                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"P0": p0, "P1": p1}
                    temp_dic.update(temp_dic_2)


                elif type_of_gate == "NOR":
                    p0_mul = 1
                    for i in input_value_container:
                        p0_mul = p0_mul * i[0]
                    p0 = p0_mul
                    p1 = 1 - p0

                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"P0": p1, "P1": p0}
                    temp_dic.update(temp_dic_2)

                elif type_of_gate == "XOR":
                    t1 = 1
                    t2 = 1
                    for i in input_value_container:
                        t1 = t1 * i[0]
                        t2 = t2 * i[1]

                    p0 = t1 + t2
                    p1 = 1 - p0

                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"P0": p0, "P1": p1}
                    temp_dic.update(temp_dic_2)

                elif type_of_gate == "XNOR":
                    t1 = 1
                    t2 = 1
                    for i in input_value_container:
                        t1 = t1 * i[0]
                        t2 = t2 * i[1]

                    p0 = t1 + t2
                    p1 = 1 - p0

                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"P0": p1, "P1": p0}
                    temp_dic.update(temp_dic_2)


                elif type_of_gate == "DFF":
                    p1_mul = 1
                    for i in input_value_container:
                        p1_mul = p1_mul * i[1]

                    p1 = p1_mul
                    p0 = 1 - p1

                    temp_dic = super_list_gates[output]
                    temp_dic_2 = {"P0": p0, "P1": p1}
                    temp_dic.update(temp_dic_2)

                else:
                    print("No gate found")

def prob3(filename, super_list_gates):
    filepath = r"C:\Users\Akshat\Documents\GitHub\HTPred_Feature_Extractor\functional_results_all" + "\{}".format(filename) + "control_observe.csv"

    import csv
    from collections import defaultdict

    columns = defaultdict(list)  # each value in each column is appended to a list

    with open(filepath) as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():
                if (k == "Wire"):
                    columns[k].append(v)
                else:
                    columns[k].append(float(v))  # append the value into the appropriate list
                # based on column name k

    super_list = []
    wire_list = columns['Wire']
    prob0_list = columns['Prob0']
    prob1_list = columns['Prob1']

    for w,p0, p1 in zip(wire_list, prob0_list, prob1_list):
        super_list_gates[w].update({"P0":p0, "P1":p1})
