# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:09:50 2018

@author: biam05
"""

def longest_word(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    words = open('words')
    words = words.read()
    words = words.split("\n")
    wordsthere = set(html.split()).intersection(set(words))
    return sorted(sorted(wordsthere, key=lambda x:x[0]), key=lambda x: len(x), reverse=True)[0]
    