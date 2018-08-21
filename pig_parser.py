import sys
import csv
import numpy as np
import string

VARNAMES = dict()

def _load(varname, filename):
    # with open(filename, newline='') as csvfile:
    #     fileread = csv.reader(csvfile, delimiter=',')
    #     return fileread
    VARNAMES[varname] = np.genfromtxt(filename, delimiter=',', dtype=np.int32)

def _dump(varname):
    for row in VARNAMES[varname]:
        print(','.join(map(str, row)))

def _filter(varnme):
    pass

def _generate(varname):
    pass

def check_var(varname):
    if VARNAMES.get(varname) is not None:
        return True
    else:
        return False

def pig_parser(line):
    elements = line.split()
    if elements[0].lower() == 'dump':
        if check_var(elements[1]):
            _dump(elements[1])
    elif elements[2].lower() == 'load':
        pass
    elif elements[2].lower() == 'foreach':
        pass
    elif elements[2].lower() == 'filter':
        pass
