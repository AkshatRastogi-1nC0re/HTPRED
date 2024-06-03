import os
import random
import sys
import enum
import threading

from InputPatternGenerator import TestPatternGenerator

class CELL(enum.Enum):
    TSMC = 'tsmc_cells/'
    SYNOPSIS = 'synopsis_cells/'


threading.stack_size(67108864)
sys.setrecursionlimit(2 ** 20)

def getRandomOutputPattern(strlen):
    rStr = ""
    x = 5
    one = 3
    zero = 3
    total = x + one + zero
    for i in range(strlen):
        t = random.random()
        if t <= x/total:
            rStr += 'X'
        elif x/total < t <= (x+zero)/total:
            rStr += '0'
        else:
            rStr += '1'

    print(rStr)
    return rStr

def do():

    input_file = 'E:/dsci__1/processed_1/TRIT-TC/c2670_T000/c2670_T000_bench.txt'
    r = TestPatternGenerator(input_file)
    r.generatePattern(getRandomOutputPattern(140))
    result = r.getFormalResult()

    for key in result:
        print(result[key])

    # for files in os.listdir(input_file):
    #     print(files, end=' -> ')
    #     r = COPCalculator(input_file + files)
    #     r.export("C:\\Users\\anirb\\Desktop\\AES\\"+files+"control_observe.csv")


t = threading.Thread(target=do,)
t.start()

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


















