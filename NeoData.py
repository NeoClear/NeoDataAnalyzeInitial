#!/usr/bin/env python

#
# Author: NeoClear
# Date: 2018-2-6
# E-mail: neoclear@outlook.com
#

import numpy
import scipy
import sympy
import json
import os

import datetime
import time

class jsonAccess(object):
    '''
    jsonAccess helps accessing json file
    '''
    def __init__(self):
        print 'jsonAccess initialized.'
    def read(self, fileName):
        return json.load(open(fileName, 'r+'))
    def write(self, fileName, data):
        return json.dump(data, fileName)

class neoPoly1dCount(object):
    '''
    neoPoly1dCount helps store and calculate poly1d functions
    '''
    def __init__(self):
        print 'neoPloy1dCount started'
    def setPoly(self, dat):
        self.__ploy = scipy.poly1d(dat)
        print self.__ploy
    def calculate(self, x):
        return self.__ploy(x)

def neoCompile(setn, addi, multi):
    '''
    precompile before used in calculating
    '''
    for i in range(len(setn)):
        setn[i] *= multi
        setn[i] += addi
    return setn

def genRandomData(density = 100, **area):
    '''
    generate random data
    '''
    xbase = min(area['x1'], area['x2'])
    xduration = numpy.abs(area['x1'] - area['x2'])
    ybase = min(area['y1'], area['y2'])
    yduration = numpy.abs(area['y1'] - area['y2'])

    xSet = neoCompile(numpy.random.rand(numpy.sqrt(density) * xduration), xbase, xduration)
    ySet = neoCompile(numpy.random.rand(numpy.sqrt(density) * yduration), ybase, yduration)
    setr = {}
    setr['x'] = xSet
    setr['y'] = ySet
    setr['len'] = len((xSet + ySet) / 2)
    return setr

def runCount(data, poly):
    '''
    count function
    '''
    up = 0
    down = 0
    for i in range(data['len']):   
        if  data['y'][i] > poly.calculate(data['x'][i]):
            up += 1
        else:
            down += 1
    print 'up:', up, 'down: ', down
    return float(up) / float(up + down)

def main():
    '''
    main function
    '''
    print 'main process started.'

    # instances
    neojs = jsonAccess()
    neoPoly = neoPoly1dCount()

    # get data and store in neoPoly
    dat = neojs.read('dataset.json')
    neoPoly.setPoly(dat)

    # generate random data and solve the problem
    data = genRandomData(1024 * 1024, x1 = -9, y1 = -9, x2 = 100, y2 = 100)
    ans = runCount(data, neoPoly)
    print 'Answer: ', ans

if __name__ == '__main__':
    # start = datetime.datetime.now()
    start = time.time()
    print 'Start at: ', start
    main()
    # end = datetime.datetime.now()
    end = time.time()
    print 'End at: ', end

    # duration, you know
    print "Duration: ", end - start