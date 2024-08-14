# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:56:21 2024

@author: Admin
"""

def tinh_tien_taxi(km):
    if km <=0:
        return 0
    tong_tien= 0
    if km > 0:
        tong_tien +=20000
        km= -1
    if km > 0:
        km_tinh= min(km,3)
        tong_tien += km_tinh*13000
        km -= km_tinh
        if km > 0:
            km_tinh= min(km,5)
            tong_tien += km_tinh*12000
            km -= km_tinh
    if km > 0:
        tong_tien += km*10000
    if tong_tien > 100000:
        tong_tien *= 0.92
    return tong_tien
km_di=float(input("Nhấp số km đi được"))
tien_taxi= tinh_tien_taxi(km_di)
print(f"Tổng tiền taxi phải trả: {tien_taxi: .2f} VND")

    