"""A module to estimate the numerical value of pi using Monte Carlo"""

import numpy  # to generate arrays of random numbers
import pylab  # to make plots

def throwDarts(n):
    """returns an array of n uniformly random (x,y) pairs lying within the square that circumscribes the unit circle centered at the origin, i.e., the square with corners at (-1,-1), (-1,1), (1,1), (1,-1)"""
    pass

def inUnitCircle(p):
    """return a boolean array, whose elements are True if the corresponding point in the array p is within the unit circle centered at the origin, and False otherwise -- hint: use numpy.linalg.norm to find the length of a vector"""
    pass

def EstimatePi1(n):
    """returns an estimate of pi by drawing n random numbers in the square [[-1,1], [-1,1]] and calculating what fraction land within the unit circle"""
    pass

def EstimatePi2(n):
    """returns an estimate of pi by drawing n random numbers in the square [[-1,1], [-1,1]] and calculating what fraction land within the unit circle; in this version, draw all the random numbers at once and do a single array comparison to count what fraction lie within the unit circle"""
    pass

def EstimatePi3(n, block=10000):
    """returns an estimate of pi by drawing n random numbers in the square [[-1,1], [-1,1]] and calculating what fraction land within the unit circle; in this version, draw random numbers in blocks of the specified size, and keep a running total of the number of points within the unit circle"""
    pass

def RunningEstimatePi1(n, block=10000):
    """returns a running estimate of pi in blocks by drawing n random numbers in the square [[-1,1], [-1,1]] and calculating what fraction land within the unit circle"""
    pass

def PlotDarts(n):
    """Draw a scatter plot of n thrown darts, coloring those inside and outside the unit circle differently""" 