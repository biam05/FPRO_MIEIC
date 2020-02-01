# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 13:25:39 2018

@author: biam05
"""
def anagrams(alist):
    word = ''
    all_words = []
    result_final = []
    for i in range(len(alist)):
        word = alist[i].split()
        one_word = ''
        for j in range(len(word)):
            one_word += word[j]
            one_word = one_word.lower()
        characters = list(one_word)
        alphabetical = sorted(characters)
        all_words.append(alphabetical)
    for k in range(len(all_words)):
        result = [alist[k]]
        for l in range(k+1, len(all_words)):
            if all_words[k] == all_words[l]:
                result.append(alist[l])
                result = sorted(result)
        result_final.append(result)
        if result not in result_final:
            result_final.append(result)
    result_final = sorted(result_final, key = lambda x : x[0].lower())
    result_final = sorted(result_final, key = lambda x : len(x))
    for n in range(len(alist)):
        for m in range(len(result_final)):
            try:
                for x in range(len(result_final)-1):
                    if x != m:
                        for z in range(len(result_final[m])):
                            if result_final[m][z] in result_final[x]:
                                if len(result_final[m]) >= len(result_final[x]):
                                    del result_final[x]
                                else:
                                    del result_final[m]
            except:
                IndexError
    result_final = sorted(result_final, key = lambda x : x[0].lower())
    return result_final