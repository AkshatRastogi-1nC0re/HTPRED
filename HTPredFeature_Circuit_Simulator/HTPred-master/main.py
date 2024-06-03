''' This code is related to the DSCI Hardware Security Project at Bennett University
    We are trying to perform feature extraction for machine learning
    Under the guidance of Dr. Vijaypal Singh Rathor and Dr. Deepak Singh '''
import os
import string_processing as sp
import features_extractor as f1
import structural_features_extractor as f2
import csv_append as ca
import headers_list
import time
from os.path import isfile, join
import HTPredBenchCreator
from enum import Enum
import sys
import os
import lfeaturesextractor
import getfunctionalfeatures as funf

'''(Trojan = 1, No Trojan = 0)'''

def get_feature_data(input_file):
    r = HTPredBenchCreator.BenchToFeature(input_file)
    final_data = r.getfeatures()
    return final_data


file_location_input = r'C:\Users\Akshat\Documents\GitHub\DSCI-feature-extractor\DSCI_Project_Feature_Extractor\python_project\non_trojan_new\AES_128_TjFree_bench.txt'
name_of_file = 'AES_128_TjFree_bench.bench'
trojan_nontrojan = 0


def get_raw_list_features(name_of_file):
    import csv
    from collections import defaultdict

    columns = defaultdict(list)  # each value in each column is appended to a list

    with open(name_of_file) as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():
                if(k=="Wire"):
                    continue
                columns[k].append(float(v))  # append the value into the appropriate list
                # based on column name k

    super_list = []

    super_list.append(columns['Controllability0'])
    super_list.append(columns['Controllability1'])
    super_list.append(columns['Observability'])
    super_list.append(columns['Prob0'])
    super_list.append(columns['Prob1'])

    return super_list



# get_raw_list_features(r"D:\DSCI Final Project Structured\functional_results_trojan\c3540_T003_bench.txtcontrol_observe.csv")




def main_function(file_location_input, name_of_file, trojan_notrojan):

    trojan_notrojan = str(trojan_notrojan)
    funf.getFunctionalfeatures(file_location_input,trojan_notrojan, name_of_file)

    start_time = time.time()
    print("String Processing Started")
    final_gates_list_2, final_gates_list, super_list_gates, mighty_raju_list, final_primary_inputs_list, final_primary_outputs_list, gate_list_input, gate_list_output, gate_list_name = sp.StringProcessing(file_location_input)
    print('[info]: String Processing Ended Successfully')
    end_time = time.time()
    print('[info]: Calculating Functional Features')

    time_elapsed = end_time - start_time
    print('Calculating Structural Features')

    if(trojan_notrojan=="0"): # Non Trojan
        path = r'C:\Users\Akshat\Documents\GitHub\HTPred_Feature_Extractor\functional_results_non_trojan'
    else:
        path = r'C:\Users\Akshat\Documents\GitHub\HTPred_Feature_Extractor\functional_results_trojan'


    files = os.listdir(path)
    raw_feature_list = []
    for f in files:
        if(name_of_file in f):
            new_path = join(path, f)
            raw_feature_list = get_raw_list_features(new_path)
            break

    if(raw_feature_list == []):
        raise Exception('File Functional Feature not found ! ')

    CC0_list = raw_feature_list[0]
    CC1_list = raw_feature_list[1]
    CO_list = raw_feature_list[2]
    P0_list = raw_feature_list[3]
    P1_list = raw_feature_list[4]

    list_of_features = f1.FeatureExtractor(final_primary_inputs_list, final_primary_outputs_list, final_gates_list, gate_list_input, gate_list_output, gate_list_name, time_elapsed, name_of_file, CC0_list, CC1_list, CO_list, P0_list, P1_list)

    result = get_feature_data(file_location_input)
    structural_data = result
    new_list = f2.extract_sf(structural_data)
    list_of_features.extend(new_list)
    Lfeatures = lfeaturesextractor.getLfeatures(CO_list)
    list_of_features.extend(Lfeatures)
    list_of_features.append(trojan_notrojan)
    print("\nFeature Extraction Successful")
    print('Number of Features Extracted :', len(list_of_features))
    print()
    print('Trying to Append to .CSV file\n')
    header_list = headers_list.Headers()
    ca.Append('data.csv', header_list, list_of_features)

    print("\n[  Features Successfully Appended to data.csv  ] \n")

    print("\nElapsed Time : {}".format(end_time - start_time))
    print("\nThank You for Using ML Feature Extractor")



'''B Files'''

path = r'C:\Users\Akshat\Documents\GitHub\HTPred_Feature_Extractor\Extra Files\b_test_files\bench'

files = os.listdir(path)

for f in files:
    print(f)
    new_path = join(path, f)
    main_function(new_path, f, "0")



'''Extracting Data for Non-Trojan Files'''

# starttime = time.time()
#
# path = r'C:\Users\Akshat\Documents\GitHub\HTPred_Feature_Extractor\HTPred-master\Non Trojan Files'
#
# files = os.listdir(path)
# count = 0
# for f in files:
#     print(f)
#     new_path = join(path, f)
#     print(new_path)
#     trojan_nontrojan = '0'
#     try:
#         main_function(new_path,f,trojan_nontrojan)
#     except Exception as e:
#         print(e)
#
# print("Damaged Files = ", count)
#
# print("All Non- Trojan files Completed")
# endtime = time.time()
# print("Total time taken ", (endtime - starttime))
# time.sleep(20)
# print("Getting ready to extract Trojan Files")
# time.sleep(20)
# print("Starting Trojan extraction in T-20 seconds")


'''Extracting Data for a single file'''

# main_function(file_location_input,name_of_file,trojan_nontrojan)

'''Extracting Data for Trojan Files'''

# starttime = time.time()
#
# path = r'C:\Users\Akshat\Documents\GitHub\HTPred_Feature_Extractor\HTPred-master\Trojan Files'
#
# files = os.listdir(path)
#
# for f in files:
#     print(f)
#     new_path = join(path, f)
#     print(new_path)
#     trojan_nontrojan = '1'
#     try:
#         main_function(new_path,f,trojan_nontrojan)
#     except Exception as e:
#         print(e)
#
# print("All Non- Trojan files Completed")
# endtime = time.time()
# print("Total time taken ", (endtime - starttime))
# time.sleep(10)
# print("Thank You for using feature extractor")

'''Extracting Data for a 35k Trojan Files'''

# path = r'C:\Users\Akshat\Documents\GitHub\DSCI-feature-extractor\DSCI Project  Feature Extractor\python_project\35s'
#
# files = os.listdir(path)
#
# for f in files:
#     print(f)
#     new_path = join(path, f)
#     print(new_path)
#     trojan_nontrojan = '1'
#     try:
#         main_function(new_path,f,trojan_nontrojan)
#     except Exception as e:
#         print(e)
#
# print("All files Completed")


'''Testing S files'''

# path = r'C:\Users\Akshat\Documents\GitHub\DSCI-feature-extractor\DSCI Project  Feature Extractor\stest\bench\s208a.bench'
# f = 's208a.bench'
# main_function(path,f,0)
# print("All files Completed")

'''Extracting Data for a stest bench Files'''

# path = r'C:\Users\Akshat\Documents\GitHub\DSCI-feature-extractor\DSCI Project  Feature Extractor\stest1\bench'
#
# files = os.listdir(path)
# count = 0
# for f in files:
#     print(f)
#     new_path = join(path, f)
#     print(new_path)
#     trojan_nontrojan = '0'
#     try:
#         main_function(new_path,f,trojan_nontrojan)
#     except Exception as e:
#         count += 1
#         print(e)
#
# print("All files Completed")
# print("Damaged Files = ", count)

'''Extracting Data for a ctest bench Files'''

# path = r'C:\Users\Akshat\Documents\GitHub\DSCI-feature-extractor\DSCI Project  Feature Extractor\c_test_files\bench'
#
# files = os.listdir(path)
# count = 0
# for f in files:
#     print(f)
#     new_path = join(path, f)
#     print(new_path)
#     trojan_nontrojan = '0'
#     try:
#         main_function(new_path,f,trojan_nontrojan)
#     except Exception as e:
#         count += 1
#         print(e)
#
# print("All files Completed")
# print("Damaged Files = ", count)


#ENDOFCODE