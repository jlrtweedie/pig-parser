import sys
import numpy as np
import numpy.ma as ma
import string

VARIABLES = dict()

def _load(varname, filename):
    """Loads .csv into numpy array"""
    VARIABLES[varname] = np.genfromtxt(filename, delimiter=',', dtype=np.int32)

def _dump(varname):
    """Dumps array to console in .csv format"""
    # Catch exception for arrays masked to a single row
    if len(VARIABLES[varname].shape) == 1:
        print(','.join(map(str, VARIABLES[varname])))
    # Otherwise iterates rowwise
    else:
        for row in VARIABLES[varname]:
            print(','.join(map(str, row)))

def _filter(varname1, varname2, column, value, operator):
    """Generates a numpy mask, masks input array, returns compressed
        output to variables dict"""
    # To do: generate masks programatically given operator input
    # Operators are reversed in mask because true values are masked, not false
    if operator == '==':
        mask = np.repeat(VARIABLES[varname1][:,column]==value,
                         VARIABLES[varname1].shape[1])
    elif operator == '>':
        mask = np.repeat(VARIABLES[varname1][:,column]<=value,
                         VARIABLES[varname1].shape[1])
    elif operator == '>=':
        mask = np.repeat(VARIABLES[varname1][:,column]<value,
                         VARIABLES[varname1].shape[1])
    elif operator == '<':
        mask = np.repeat(VARIABLES[varname1][:,column]>=value,
                         VARIABLES[varname1].shape[1])
    elif operator == '<=':
        mask = np.repeat(VARIABLES[varname1][:,column]>value,
                         VARIABLES[varname1].shape[1])

    VARIABLES[varname2] = ma.compress_rows(ma.array(VARIABLES[varname1],
                                           mask=mask))

def _generate(varname1, varname2):
    pass

def check_var(varname):
    """"Checks if varname exists in variables dict"""
    if VARIABLES.get(varname) is not None:
        return True
    else:
        return False

def pig_parser(line):
    elements = line.split()
    if elements[0].lower() == 'dump':
        if check_var(elements[1]):
            _dump(elements[1])
        else:
            raise IndexError('Variable {} is undefined'.format(elements[1]))
    elif elements[2].lower() == 'load':
        pass
    elif elements[2].lower() == 'filter':
        pass
    elif elements[2].lower() == 'foreach':
        pass

if __name__ == '__main__':
    # Test functionality
    _load('a', 'myfile.csv')
