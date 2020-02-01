# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:29:31 2018

@author: biam05
"""

def budgeting2(budget, products, wishlist):
    Max = 0
    best_combination = []
    wishlist = sorted(wishlist.items(), key = lambda x: products[x[0]], reverse = True)
    x,y = zip(*wishlist)
    prices = [products[i] for i in x]
    combination = linear_combination(y)
    for c in combination:
        total = sum(j[0]*j[1] for j in zip(c,prices))
        if total <= budget:
            if total > Max:
                best_combination = c
                Max = total
            elif total == Max and c > best_combination:
                best_combination = c
    return {a[0]: a[1] for a in zip(x,best_combination) if a[1]!=0}


def linear_combination(amount,comblist = []):
    if len(amount) == 0:
        return [comblist]
    combinations = []
    for i in range(amount[0]+1):
        combinations += linear_combination(amount[1:],comblist+[i])
    return combinations