import HTPredBenchCreator
from enum import Enum


class CELL(Enum):
    TSMC = 'tsmc_cells/'
    SYNOPSIS = 'synopsis_cells/'


input_file = 'I:/b19_scan.v'

r = HTPredBenchCreator.Creator(input_file,CELL.TSMC.value, 'b19')
outpf = 'I:/benchoutput.bench'
s = open(outpf,'w')
s.write(r.convert())
s.close()
