
import numpy as np
import os

src = 'C:/Project/TimeCycle/dataset/mf.txt'
outlist = 'C:/Project/TimeCycle/dataset/test.txt'
foldername = 'C:/Project/DL_Competition/data/'

file = open(src, 'r')
fout = open(outlist, 'w')

for line in file:
    line = line[:-1]
    fname = foldername + line
    fnms  = len(os.listdir(fname))

    outstr = fname + ' ' + str(fnms) + '\n'
    fout.write(outstr)


file.close()
fout.close()
