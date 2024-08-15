import random

def Random():
    choices = ["Kéo", "Búa", "Bao"]
    return random.choice(choices)

def ChonNguoiThang(Ban, MayTinh):
    if Ban == MayTinh:
        return "Hòa"
    elif (Ban == "Kéo" and MayTinh == "Búa") or \
         (Ban == "Búa" and MayTinh == "Bao") or \
         (Ban == "Bao" and MayTinh == "Kéo"):
        return "Bạn thắng"
    else:
        return "Máy thắng"

def play_game():
    print("Kéo Búa Bao")
    Ban = input("Chọn Kéo, Búa, Bao: ").capitalize()
    
    if Ban not in ["Kéo", "Búa", "Bao"]:
        print("Lựa chọn không hợp lệ.")
        return
    
    MayTinh = Random()
    print(f"Máy chọn: {MayTinh}")
    
    KetQua = ChonNguoiThang(Ban, MayTinh)
    print(KetQua)
    
play_game()