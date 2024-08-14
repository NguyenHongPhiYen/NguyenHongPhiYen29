# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:59:27 2024

@author: Admin
"""

a=float(input("nhập hệ số a:"))
b=float(input("nhập hệ số b:"))
if a==0:
    if b==0:
        print("phương trình có vô số nghiệm.")
    else:
        print("phương trình vô nghiệm.")
else:
    x= -b / a
    print(f"Nghiệm của phương trình là: x = {x}")
    
    
