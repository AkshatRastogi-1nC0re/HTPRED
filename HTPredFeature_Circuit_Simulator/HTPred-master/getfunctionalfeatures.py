import os
import sys
import enum
import threading

import HTPredBenchCreator
from ControlObserveProbabCalculator import COPCalculator


class CELL(enum.Enum):
    TSMC = 'tsmc_cells/'
    SYNOPSIS = 'synopsis_cells/'


threading.stack_size(67108864)
sys.setrecursionlimit(2 ** 20)


def do():

    input_file = 'C:/Users/Akshat/Documents/GitHub/HTPred_Feature_Extractor/Extra Files/b_test_files/bench/'
    # r = ControllabilityObservabilityCalculator.COCalculator('I:/b19.bench')

    for files in os.listdir(input_file):
        print(files, end=' -> ')
        r = COPCalculator(input_file + files)
        r.export("C:/Users/Akshat/Documents/GitHub/HTPred_Feature_Extractor/functional_results_non_trojan/"+files+"control_observe.csv")


# t = threading.Thread(target=do)
# t.start()

# r = ControllabilityObservabilityCalculator.COCalculator('I:/testv.bench')

# r = HTPredBenchCreator.Creator(input_file,CELL.TSMC.value, 's15850')
# outpf = 'I:/benchoutput.bench'
# s = open(outpf,'w')
# s.write(r.convert())
# s.close()
# print(r.convert())

# r = HTPredBenchCreator.FeatureExtractor(input_file, CELL.SYNOPSIS.value,'b19')
# export_file = 'I:/b19_feature.csv'
# r.getfeatures(export_file,['preferences/mux_list.txt'])

# Non Trojan = 0, Trojan = 1

def getFunctionalfeatures(input_file, trojan_nontrojan, file_name):
    r = COPCalculator(input_file)
    if(trojan_nontrojan=="0"):
        r.export(
            "C:/Users/Akshat/Documents/GitHub/HTPred_Feature_Extractor/functional_results_non_trojan/" + file_name + "control_observe.csv")
    elif(trojan_nontrojan=="1"):
        r.export(
            "C:/Users/Akshat/Documents/GitHub/HTPred_Feature_Extractor/functional_results_trojan/" + file_name + "control_observe.csv")

    r.export(
        "C:/Users/Akshat/Documents/GitHub/HTPred_Feature_Extractor/functional_results_all/" + file_name + "control_observe.csv")
























