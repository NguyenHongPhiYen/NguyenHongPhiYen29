# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:10:21 2024

@author: Admin
"""

import cmath
a=float(input("nhập hệ số a:"))
b=float(input("nhập hệ số b:"))
c=float(input("nhập hệ số c:"))
if a==0:
    if b==0:
        if c==0:
            print("phương trình có vô số nghiệm.")
        else:
            print("phương trình vô nghiệm")
    else:
         x= -c / b
    print(f"nghiệm của phương trình là x = {x}")
else: 
    delta= b**2 - 4*a*c
    sqrt_delta = cmath.sqrt(delta)
    x1=(-b+sqrt_delta)/ (2*a)
    x2=(-b-sqrt_delta)/ (2*a)
    print(f"nghiệm thứ nhất: x1 = {x1}")
    print(f"nghiệm thứ hai: x2 = {x2}")

    