# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:07:46 2018

@author: biam05
"""

def budgeting(budget, products, wishlist):
    price = 0
    for product, prices in products.items():
        for product2, quantity in wishlist.items():
            if product == product2:
                price += prices * quantity
    if price <= budget:
        return wishlist
    else:
        product_sorted = sorted(products.items(), key = lambda x:x[1])
        for i in range(len(product_sorted)):     
            while price > budget:
                if product_sorted[i][0] in wishlist:
                    if wishlist[product_sorted[i][0]] > 0:
                        wishlist[product_sorted[i][0]] = (wishlist[product_sorted[i][0]]-1)
                        price -= product_sorted[i][1]
                        if wishlist[product_sorted[i][0]] == 0:
                            del wishlist[product_sorted[i][0]]
                else:
                    break
                
    return wishlist