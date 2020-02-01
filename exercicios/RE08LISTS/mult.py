# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:53:09 2018

@author: Carlos Lousada
"""
def inner(u, v):
    result = 0
    if u == [] or v == []:
        return result
    else:
        for i in range(len(u)):
            result += u[i] * v[i]
    return result


def mult(M, N):
    Nt = []
    for j in range(len(N[0])):
        cN = []
        for i in range(len(N)):
            cN.append(N[i][j])
        Nt.append(cN)
    #print(Nt)
    if len(M[0]) != len(Nt[0]):
        return []
    else:
        result = []
        for j in range(len(M)):
            resultrows = []
            for i in range(len(Nt)):
                resultrows.append(inner(M[j], Nt[i]))
            result.append(resultrows)
        return result

            