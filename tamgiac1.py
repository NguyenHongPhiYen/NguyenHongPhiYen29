# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:29:21 2024

@author: Admin
"""

a=float(input("nhập cạnh a:"))
b=float(input("nhập cạnh b:"))
c=float(input("nhập cạnh c:"))
if a+b>c and a+c>b and b+c>a:
    print("a,b,c là ba cạnh của tam giác.")
else:
    print("a,b,c không là ba cạnh của tam giác")