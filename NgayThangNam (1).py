def kiemTraNamNhuan(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 1
        
    return 0

def kiemTraNgayThangNam(day, month, year):
    
    if month == 2:
        if kiemTraNamNhuan(year):
            if day < 1 or day > 29:
                return 0
        else:
            if day < 1 or day > 28:
                return 00
    
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return 0
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return 0
    else:
        return 0  

    
    if month < 1 or month > 12:
        return 0

    
    if day < 1 or day > 31 or year < 1:
        return 0

    return 1


day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))


if kiemTraNgayThangNam(day, month, year):
    print(f"{day}/{month}/{year} hợp lệ.")
else:
    print(f"{day}/{month}/{year} không hợp lệ.")