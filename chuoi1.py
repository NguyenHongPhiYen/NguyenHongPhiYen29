# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:38:03 2024

@author: Student
"""

chuoi=("Đại học Quốc gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, Tp.HCM")
#phần 1
print("Đại học Quốc Gia\nKhu phố 6\nP.Linh Trung\nQ.Thủ Đức\nTp.HCM")
#xóa các chữ P,Q,Tp
print(chuoi.replace(',','\n').replace('P.','').replace('Q.','').replace('Tp.',''))
