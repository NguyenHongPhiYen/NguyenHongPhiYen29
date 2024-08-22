# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
a=float(input("nhập số a:"))
b=float(input("nhập số b:"))
tinh=(((a**(1/2)-b**(1/2)) / (a**(1/4) - b**(1/4)))) - ((a**(1/2) + (a*b)**(1/4))) / (a**(1/4)+b**(1/4))
print("kết quả là", tinh)