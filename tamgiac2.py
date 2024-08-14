# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:37:43 2024

@author: Admin
"""

a=float(input("nhập cạnh a:"))
b=float(input("nhập cạnh b:"))
c=float(input("nhập cạnh c:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Tam giác đều")
    elif a==b or a==c or b==c:
        x,y,z= sorted([a,b,c])
        if x**2+y**2==z**2:
            print("Tam giác vuông cân")
        else: 
            print("Tam giác cân")
    else:
        x,y,z= sorted([a,b,c])
        if x**2+y**2==z**2:
            print("Tam giác vuông")
        else:
            print("Tam giác thường")
else: 
    print("a,b,c không là ba cạnh của tam giác")
         