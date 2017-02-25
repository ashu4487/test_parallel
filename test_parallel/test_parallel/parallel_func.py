'''
Created on Feb 21, 2017

@author: ashu
'''
from multiprocessing import Pool
import numpy

def sqrt(x):
    return numpy.sqrt(x)
if __name__ == '__main__':
    pool = Pool()
    roots = pool.map(sqrt, range(100))
    print roots