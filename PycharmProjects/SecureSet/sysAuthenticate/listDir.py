#!/usr/bin/python
"""
Written by Michael Kelley @ SecureSet 2016
"""
import os
import stat


def getuidlist(path):

    print('Origin[' + path + ']')
    for root, dirs, files in os.walk(path):
        for name in files:
            p = os.path.join(root, name)
            s = stat.ST_UID
            instr="'{0}', '{1}'".format(p, s)
            print(instr)
        for name in dirs:
            print(os.path.join(root, name))


if __name__ == '__main__':
    getuidlist(input('Please specify path to scan:'))
