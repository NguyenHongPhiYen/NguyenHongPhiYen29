# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:55:18 2024

@author: Admin
"""

print("Tính tiền taxi ")
a=float(input("Số km đi được"))
if a== 1:
    print("tiền taxi là 20000")
if a==2 or a==3:
    b=a*13000
    print("tiền taxi là",b)
if a>=4 and a<=8:
    b= 3*13000 + (a-3)*12000
    print("tiền taxi là",b)
if a>8:
    b= 3*13000 + 5*12000 + (a-8)*10000
    print("tiền taxi là",b)
if b>100000:
    b=b*92/100
    print("tiền taxi sau khi được giảm là",b)
    