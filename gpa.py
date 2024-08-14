# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:33:55 2024

@author: Admin
"""

GPA=float(input("nhập điểm trung bình:"))
if GPA < 3.5: ranking= "Học lực Kém"
elif 3.5 <= GPA < 5.0: ranking= "Học lực Yếu"
elif 5.0 <= GPA < 7.0: ranking= "Học lực Trung bình"
elif 7.0 <= GPA < 8.0: ranking= "Học lực Khá"
elif 8.0 <= GPA < 9.0: ranking= "Học lực Giỏi"
elif 9.0 <= GPA <= 10: ranking= "Học lực Xuất sắc"
else: ranking= "Điểm không hợp lệ"
print(ranking)