# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:22:50 2018

@author: biam05
"""
          
def file_finder(dirs, file_name):
    if dirs == file_name:
        return file_name
    ficheiros = dirs[1:]
    nome_diretorio = dirs[0]
    for i in ficheiros:
        if file_finder(i, file_name) != None:        
            return nome_diretorio + '/' + file_finder(i, file_name)
