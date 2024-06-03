import HTPredBenchCreator
from enum import Enum
import sys
import os


class CELL(Enum):
    TSMC = 'tsmc_cells/'
    SYNOPSIS = 'synopsis_cells/'

#
# input_file = sys.argv[1]
# print(input_file)
# print(type(input_file))

# input_file = r'C:\Users\Akshat\Documents\GitHub\DSCI-feature-extractor\DSCI_Project_Feature_Extractor\python_project\non_trojan_new\AES_128_TjFree_bench.txt'


def get_feature_data(input_file):
    r = HTPredBenchCreator.BenchToFeature(input_file)
    final_data = r.getfeatures()
    return final_data

# final_data_str = str(get_feature_data(r'{}'.format(input_file)))
#
# with open(r'C:\Users\Akshat\Documents\GitHub\DSCI-feature-extractor\DSCI_Project_Feature_Extractor\python_project\structural_features\result.txt', 'w') as f:
#     f.write(final_data_str)


# f = open("result.txt", "w")
# print('writing file')
# f.write()
# f.close()
# print('file written')
