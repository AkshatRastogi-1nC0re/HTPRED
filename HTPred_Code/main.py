import os
import sys
import enum
import threading

import CircuitSimulator
import ControlObserveProbabCalculator
import HTPredBenchCreator
from InputPatternGenerator import TestPatternGenerator


class CELL(enum.Enum):
    TSMC = 'tsmc_cells/'
    SYNOPSIS = 'synopsis_cells/'


def do():



    # Verilog to Bench
    # input_file = 'file.v'
    # r = HTPredBenchCreator.Creator(input_file, CELL.TSMC.value, 's15850')  # InputFile, Cell Library, Main Module name
    # print(r.convert())  # Bench File String



    # Structural Feature Extractor
    # input_file = 'file.v'
    # r = HTPredBenchCreator.FeatureExtractor(input_file, CELL.SYNOPSIS.value, 'b19')  # InputFile, Cell Library, Main Module name
    # export_file = 'I:/b19_feature.csv'  # Export file
    # r.getfeatures(export_file, ['preferences/mux_list.txt'])



    # Circuit Simulator
    # input_file = 'file.bench'
    # simulator = CircuitSimulator.CircuitSimulator(input_file, '1001100110')  # InputFile, Input
    # simulator.result()  # Dictionary { NodeName: Value, ... }



    # Controllability Observability Probability Calculator
    # input_file = 'file.bench'
    # copC = ControlObserveProbabCalculator.COPCalculator(input_file)
    # export_file = 'file.csv'
    # copC.export(export_file)



    # Test Pattern Generator
    input_file = r'D:\dsci__1\c432.txt'
    prob = ControlObserveProbabCalculator.COPCalculator(input_file)

    r = TestPatternGenerator(input_file)
    desiredpattern = prob.get_rareness()

    r.generatePattern(desiredpattern)
    (result, count) = r.getResult()

    for i in result:
        print(i, result[i])

    print(count)




threading.stack_size(67108864)
sys.setrecursionlimit(2 ** 20)
t = threading.Thread(target=do, )
t.start()
