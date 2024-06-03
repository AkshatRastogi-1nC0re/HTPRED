import string_processing as sp
import circuit_simulator as cs
import prob_ref_test as pb
import getRareNodes as gr
import random
import os
import getTCS
from os.path import isfile, join


def GenerateTestFile(number_of_primary_input, number_of_test_patterns, file_name):
    f = open(file_name, "w")
    f.write("")
    f.close()
    for _ in range(number_of_test_patterns):
        bit = ""
        for i in range(number_of_primary_input):
            bit += str(round(random.random()))
        ff = open(file_name, "a")
        ff.write(bit + "\n")
        ff.close()


def OptimizeTextFile(result_file_name_output):
    result = []

    for line in open(result_file_name_output).readlines():
        line = line.strip()
        length = len(line)
        xx = [x.strip() for x in line.split("::")[-1].split(",")]
        del xx[-1]
        thisLine = {"length": length, "line": line, "set":set(xx)}
        result.append(thisLine)
    sortedList = sorted(result, key=lambda k:k["length"], reverse=True)
    removeRepeatingPatterns(result_file_name_output, sortedList)


def removeRepeatingPatterns(result_file_name_output, sortedList):
    new_sorted_list = []
    result_list = []
    for ind, dictio in enumerate(sortedList):

        current_set = dictio["set"]

        if ind==0:
            new_sorted_list.append(dictio)
        else:
            bool = False
            for i in range(ind):
                super_set = sortedList[i]["set"]
                if current_set.issubset(super_set):
                    bool = True
            if not bool:
                new_sorted_list.append(dictio)

    f = open(result_file_name_output, "w")
    f.write("")
    f.close()
    f = open(result_file_name_output, "a")
    for dictio in new_sorted_list:
        f.write(dictio["line"] + "\n")
        result_list.append(list(dictio["set"]))

    # print(result_list)
    print("TCS Value : ",getTCSval(result_list))



def getTCSval(new_sorted_list):
    return getTCS.getTCS(new_sorted_list)

def SimulateCircuit(file_location_input):
    final_gates_list_2, final_gates_list, super_list_gates, mighty_raju_list, final_primary_inputs_list, final_primary_outputs_list, gate_list_input, gate_list_output, gate_list_name = sp.StringProcessing(
        file_location_input)
    file_name = os.path.basename(file_location_input)
    print("File Name : ", file_name)
    print("Number of Primary Inputs : ", len(final_primary_inputs_list))
    print("Number of Primary Outputs : ", len(final_primary_outputs_list))
    new_file_name = "test_inputs/" + file_name.split(".")[0] + "_test" + ".txt"

    f = os.path.exists(new_file_name)
    if not f:
        GenerateTestFile(len(final_primary_inputs_list), 100, new_file_name)

    f = open(new_file_name)
    list_of_test_inputs = f.readlines()

    pb.prob3(file_name, super_list_gates)
    list_rare_nodes = gr.gr1(mighty_raju_list, super_list_gates)

    if len(list_rare_nodes) == 0:
        return

    print("Number of Rare Nodes : ", len(list_rare_nodes))

    result_file_name_output = "test_inputs/result/" + file_name.split(".")[0] + "_result" + ".txt"

    f_out = open(result_file_name_output, "w")
    f_out.write("")
    f_out.close()

    list_of_sets = []

    for test_input in list_of_test_inputs:
        final_gates_list_2, final_gates_list, super_list_gates, mighty_raju_list, final_primary_inputs_list, final_primary_outputs_list, gate_list_input, gate_list_output, gate_list_name = sp.StringProcessing(
            file_location_input)
        test_input = test_input[:-1]
        list_pi_map = list(map(int, list(test_input)))
        for ind, i in enumerate(final_primary_inputs_list):
            super_list_gates[i].update({"SimVal": list_pi_map[ind]})

        cs.cs1(mighty_raju_list, super_list_gates)

        output = ""
        for i in final_primary_outputs_list:
            output += str(super_list_gates[i]["SimVal"])

        activated_rare_nodes = []

        pb.prob3(file_name, super_list_gates)
        list_rare_nodes = gr.gr1(mighty_raju_list, super_list_gates)

        for rare_node in list_rare_nodes:
            rare_towards = super_list_gates[rare_node]["Rare_towards"]
            node_output = super_list_gates[rare_node]["SimVal"]
            if str(node_output) == str(rare_towards):
                activated_rare_nodes.append(rare_node)

        if len(activated_rare_nodes) == 0:
            continue

        string_rare_nodes_output = ""

        for xyz in activated_rare_nodes:
            string_rare_nodes_output += (xyz + ", ")

        f_out = open(result_file_name_output, "a")
        f_out.write(test_input + "::" + string_rare_nodes_output + "\n")
        f_out.close()

    print("Result Saved at :")
    print(result_file_name_output)

    OptimizeTextFile(result_file_name_output)


# GenerateTestFile(10, 10, "xyz.txt")

# path = r'C:\Users\Akshat\Documents\GitHub\HTPred_Feature_Extractor\Extra Files\b_test_files\bench'
#
# files = os.listdir(path)
#
# for f in files:
#     print(f)
#     new_path = join(path, f)
#     SimulateCircuit(new_path)

SimulateCircuit(r"C:\Users\Akshat\Documents\GitHub\HTPred_Feature_Extractor\HTPred-master\Non Trojan Files\c499.txt")
