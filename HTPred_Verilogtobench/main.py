import HTPredBenchCreator
import os
import time



cell_dir = 'D:/dsci/Integration/tsmc_cells/'
input_file = 'D:/dsci/Integration/AES_T200_TjIn.v'

s = int(time.time()*1000)
r = HTPredBenchCreator.Creator(input_file, cell_dir,'top')
outputbench = r.convert()

file_o = open('D:/dsci/Integration/AES_T200_TjOu.txt','w')
file_o.write(outputbnch())
file_o.close(outputbench)

print('//Completed in : ' + str(int(time.time()*1000)-s) + ' millis')


# z = os.listdir(input_file)
# a = 0
#
# currentmillis = int(time.time()*1000)
# for t in z:
#     r = HTPredBenchCreator.Creator(input_file+t,cell_dir)
#     print(r.convert())
#     a += 1
#
# currentmillis = int(time.time()*1000) - currentmillis
#
# print('Compiled',a,'cells in',currentmillis,'millis')
