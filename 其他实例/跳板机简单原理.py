#!/usr/bin/env/python
import os
myip=raw_input('please input ip (192.168.0.109):')
user=raw_input ('please input username:').strip()
cmd='ssh %s@%s' % (user,myip)
os.system(cmd)

