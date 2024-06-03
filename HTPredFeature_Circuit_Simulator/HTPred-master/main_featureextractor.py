import HTPredBenchCreator
from enum import Enum


class CELL(Enum):
    TSMC = 'tsmc_cells/'
    SYNOPSIS = 'synopsis_cells/'


input_file = 'I:/b19_scan.v'

r = HTPredBenchCreator.FeatureExtractor(input_file, CELL.SYNOPSIS.value,'b19')
export_file = 'I:/b19_feature.csv'
r.getfeatures(export_file,['preferences/mux_list.txt'])
