import csv
# import headers_list

# ht = headers_list.Headers()
# file_location_output = r'C:\Users\Akshat\Documents\GitHub\DSCI-feature-extractor\DSCI_Project_Feature_Extractor\python_project\data.csv'
# lof = []

def Append(file_name, headers_list, list_of_features):

    with open(file_name, 'a', newline='') as csvfile:
        print("Working")
        writer = csv.writer(csvfile)
        # writer.writerow(headers_list)
        writer.writerow(list_of_features)
        # print(len(headers_list) == len(list_of_features))

# Append(file_location_output, ht, lof)


