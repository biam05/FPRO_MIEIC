# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 12:51:00 2018

@author: biam05
"""

def manipulator(l, cmds):
    final = ''
    for i in range(len(cmds)):
        cmd = cmds[i].split()
        if cmd[0] == 'insert':
            l.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            final += ' ' + str(l)
        elif cmd[0] == 'remove':
            l.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            l.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            l = sorted(l)
        elif cmd[0] == 'pop':
            l.pop(len(l)-1)
        elif cmd[0] == 'reverse':
            l.reverse()
    final = final[1:]
    return final