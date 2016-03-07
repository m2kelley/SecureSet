#!/usr/bin/python
"""
Written by Michael Kelley @ SecureSet 2016
"""
import os
import datetime

path = (input('Please specify a directory:'))


def dirwalk(path):
    g = 0
    for root, dirs, files in os.walk(path, topdown=True):
        try:
            for name in files:
                name = name.strip()
#            os.stat_result(st_mode=33188, st_ino=7876932, st_dev=234881026,
# st_nlink=1, st_uid=501, st_gid=501, st_size=264, st_atime=1297230295,
# st_mtime=1297230027, st_ctime=1297230027)
                a = os.path.join(root, name)
                statinfo = os.stat(a)
                if statinfo.st_uid or statinfo.st_gid > 0:
                    ctime = datetime.datetime.fromtimestamp(statinfo.st_ctime)
                    mtime = datetime.datetime.fromtimestamp(statinfo.st_mtime)
                    atime = datetime.datetime.fromtimestamp(statinfo.st_atime)
                    own = statinfo.st_uid
                    print(a, '\nUID:', own, '\ncreated:', ctime, '\nmodified:', mtime, '\nlast accessed:', atime)
                else:
                    g += 1
            for name in dirs:
                name = name.strip()
                d = os.path.join(root, name)
                statinfo2 = os.stat(d)
                if statinfo2.st_uid or statinfo2.st_gid > 0:
                    cctime = datetime.datetime.fromtimestamp(statinfo.st_ctime)
                    mmtime = datetime.datetime.fromtimestamp(statinfo.st_mtime)
                    aatime = datetime.datetime.fromtimestamp(statinfo.st_atime)
                    oown = statinfo.st_uid
                    print(d, '\nUID:', oown, '\ncreated:', cctime, '\nmodified:', mmtime, '\nlast accessed:', aatime)
                else:
                    g += 1
        except FileNotFoundError:
            continue
    print('%i known files and directories with no UID or GID bits set.' % g)
dirwalk(path)
