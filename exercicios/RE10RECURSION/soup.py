# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:29:20 2018

@author: biam05
"""

def soup(matrix, word):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for row in range(len(matrix)):
        for letter in range(len(matrix[row])):
            if matrix[row-1][letter-1] == word[0]:
                if checksoup(matrix,row-1,letter-1,word[1:]):
                    return "{0}{1}".format(alphabet[row-1],letter)
            else:
                if matrix[row][letter-1] == word[0]:
                    if checksoup(matrix,row-1,letter-1,word[1:]):
                        return "{0}{1}".format(alphabet[row],letter)


def checksoup(matrix,row,letter,word):
    if word == "":
        return True
    else:
        for r in range(row-1,row+2):
            for l in range(letter-1,letter+2):
                if r>=0 and l>=0 and r<len(matrix) and l<len(matrix) and word[0] == matrix[r][l]:
                    matrix[r][l] == ""
                    if checksoup(matrix,r,l,word[1:]):
                        return checksoup(matrix,r,l,word[1:])
                    

    