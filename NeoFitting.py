#!/usr/bin/env python

import sys
import numpy
from NeoData import jsonAccess

def middle(meta):
    '''
    figure out the middle value
    '''
    x = 0.0
    y = 0.0
    for i in range(meta['len']):
        x += float(meta['x'][i])
        y += float(meta['y'][i])
    x /= meta['len']
    y /= meta['len']
    dat = {'x': x, 'y': y}
    return dat

def collect(middle, meta):
    '''
    solve the average of angle and solve the average k
    '''
    k = []
    for i in range(meta['len']):
        dx = meta['x'][i] - middle['x']
        dy = meta['y'][i] - middle['y']
        if dx == 0:
            '''
            if dy > 0:
                k.append(numpy.arccos(0))
            elif dy < 0:
                k.append(-1 * numpy.arccos(0))
            else:
                continue'''
            if dy == 0:
                continue
            else:
                k.append(numpy.arccos(0))
        k.append(numpy.arctan(dy / dx))
    ans = 0.0
    for i in k:
        ans += i
    ans /= len(k)
    return ans


def main():
    # read meta data and prepare for the access
    js = jsonAccess()
    meta = js.read('dataset.json')
    if len(meta['x']) == len(meta['y']):
        meta['len'] = len(meta['x'])
    else:
        print 'data not usable.'
        return
    # solve middle value and get average value of k
    mid = middle(meta)
    k = numpy.tan(collect(mid, meta))

    # print out the answer
    print 'y +', mid['y'], '=', k, '* (x +', mid['x'], ')'
    

if __name__ == '__main__':
    main()