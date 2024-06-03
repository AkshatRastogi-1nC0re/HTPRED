import os
# Importing os package to open the desired file
import time
import re
import random

# Importing re package to find by patterns in strings


def StringProcessing(name):
    # startime = time.time()
    lol = open(name)
    string_lists = lol.readlines()
    lol.close()

    string_lists2 = string_lists[:]
    j = 1
    for i in string_lists2:
        if j >= 20:
            break
        j +=1
        if i.startswith("//") or ("//" in i) or i.startswith("#") or ("#" in i):
            string_lists.remove(i)
        else:
            continue

    for _ in range(5):
        for i in string_lists:
            if ("//" in i) or ("#" in i):
                string_lists.remove(i)
            else:
                continue

    while '' in string_lists:
        string_lists.remove('')

    gates_list = []
    # print("Process Started")
    string_lists2 = string_lists[:]
    for strings in string_lists2:
        strings = strings.strip('\n')
        if "=" in strings and ('AND' in strings or 'OR' in strings or 'NAND' in strings or 'NOT' in strings or 'DFF' in strings or 'XOR' in strings or 'XNOR' in strings or 'NOR' in strings or 'BUFF' in strings):
            gates_list.append(strings)

    # string_lists2 = []
    # for i in string_lists:
    #     if i == "\n":
    #         string_lists.remove(i)
    #     else:
    #         string_lists2.append(i.strip("\n"))
    #
    # string_lists = string_lists2[:]

    primary_input_statement_list = []
    primary_output_statement_list = []

    for i in range(len(string_lists)):
        temp_variable = string_lists[i]
        if 'INPUT' in temp_variable:
            primary_input_statement_list.append(temp_variable)
        elif 'OUTPUT' in temp_variable:
            primary_output_statement_list.append(temp_variable)

    temp_list = []

    for statements in primary_input_statement_list:
        pattern = "\(.*?\)"
        match = re.search(pattern, statements).group()
        temp_list.append(match)

    final_primary_inputs_list = []

    for items in temp_list:
        word = ""
        for i in items:
            if "(" in i or ")" in i:
                pass
            else:
                word = word + i

        final_primary_inputs_list.append(word)

    temp_list = []
    for statements in primary_output_statement_list:
        pattern = "\(.*?\)"
        match = re.search(pattern, statements).group()
        temp_list.append(match)

    final_primary_outputs_list = []

    for items in temp_list:
        word = ""
        for i in items:
            if "(" in i or ")" in i:
                pass
            else:
                word = word + i

        final_primary_outputs_list.append(word.strip(" "))

    temp_list3 = []
    gate_list_output = []
    for i in gates_list:
        str_2 = i.split(" ")
        str_3 = i.index("(")
        str_4 = i.index(")")
        inut = i[str_3 + 1:str_4]
        temp_list3.append(inut)
        x = str_2[0]
        gate_list_output.append(x)

    # print(gate_list_output)

    gate_list_input = []
    for lol in temp_list3:
        if ',' in lol:
            yy = lol.split(",")
            xx = []
            for i in yy:
                xx.append(i.strip(" "))
            gate_list_input.append(xx)
        else:
            gate_list_input.append([lol.strip(" ")])

    # print(gate_list_input)

    temp_names_of_gates_list = []

    for i in gates_list:
        str_3 = i.index("= ")
        str_4 = i.index("(")
        inPut = i[str_3 + 1:str_4]
        temp_names_of_gates_list.append(inPut)

    gate_list_name = []
    for gates in temp_names_of_gates_list:
        word = ""
        for letters in gates:
            if letters != " ":
                word += letters
        gate_list_name.append(word)

    mighty_raju_list = []

    for i in range(len(gates_list)):
        temp_list_12 = []
        temp_list_12.append([gate_list_output[i].strip(" ")])
        temp_list_12.append([gate_list_name[i].strip(" ")])
        temp_list_12.append(gate_list_input[i])

        mighty_raju_list.append(temp_list_12)

    final_gates_list = []

    for gat in mighty_raju_list:
        final_gates_list.extend(gat[0])
        final_gates_list.extend(gat[2])


    final_gates_list_2 = list(dict.fromkeys(final_gates_list))

    super_list_gates = {}





    for gi in final_gates_list_2:
        feauture_dict = {gi: {"CC0": "", "CC1": "", "CO": "", "P0": "", "P1": "", "Status": "Fake", "Status_P": "Fake", "SimVal":"", "Rare_Node_Factor":"", "Rare_towards":""}}
        super_list_gates.update(feauture_dict)

    dff_list = []
    for items in mighty_raju_list:
        if items[1][0] == "DFF":
            dff_list.extend(items[2])

    final_dff_list = list(dict.fromkeys(dff_list))

    for gijoe in final_dff_list:
        feauture_dict = {gijoe: {"CC0": 1, "CC1": 1, "CO": "", "P0": 0.5, "P1": 0.5, "Status": "Fake", "Status_P": "Fake", "SimVal":round(random.random()), "Rare_Node_Factor":"", "Rare_towards":""}}
        super_list_gates.update(feauture_dict)

    for ii in super_list_gates:
        dicto = super_list_gates[ii]
        if ii in final_primary_inputs_list:
            diction = {'CC0': 1, 'CC1': 1, 'P0': 0.5, 'P1': 0.5, 'Status': "True", "Status_P": "True", "SimVal":"", "Rare_Node_Factor":"", "Rare_towards":""}
            dicto.update(diction)
        elif ii in final_primary_outputs_list:
            diction = {'CO': 0}
            dicto.update(diction)
        else:
            pass




    # endtime = time.time()
    # print(endtime - startime)
    return final_gates_list_2, final_gates_list, super_list_gates, mighty_raju_list, final_primary_inputs_list, final_primary_outputs_list, gate_list_input, gate_list_output, gate_list_name

# final_gates_list_2 , final_gates_list, super_list_gates, mighty_raju_list, final_primary_inputs_list, final_primary_outputs_list, gate_list_input, gate_list_output, gate_list_name = StringProcessing(r'C:\Users\Akshat\Documents\GitHub\HTPred_Feature_Extractor\HTPred-master\Non Trojan Files\c7552.txt')

# print(mighty_raju_list)
# print()
# print(super_list_gates)
# print()
# print(final_primary_outputs_list)
# print()
# print('241' in final_primary_inputs_list)
# print()
# print(final_gates_list)
# print(final_gates_list_2)
# print()
# print(gate_list_input)
