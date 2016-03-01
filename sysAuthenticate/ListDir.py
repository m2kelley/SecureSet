#!/usr/bin/python
"""
Written by Michael Kelley @ SecureSet 2016
"""
import os
import stat

def getuidlist(path):

    print('Origin[' + path + ']')
    x = 0
    y = 0
    for root, dirs, files in os.walk(path):
        if stat.ST_UID:
            x += 1
        if oct(stat.ST_MODE) > oct(0o0):
            y += 1
        for name in files:
            p = os.path.join(root, name)
            s = stat.ST_UID
            m = oct(stat.ST_MODE)
            instr = "'Path::{0}', 'UID::{1}', 'MODE::{2}'".format(p, s, m)
            print(instr)
        for name in dirs:
            print(os.path.join(root, name))
    print('Number of set UID bits is: %i' % x)
    print('Number of set MODE bits is: %s' % y)

if __name__ == '__main__':
    getuidlist(input('Please specify path to scan:'))
