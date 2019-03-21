# dictionary={"computer":"máy tính","mouse":"chuột","keyboard":"bàn phím"}
# while True:
#     type = input("nhập từ cần tra :")
#     if type in dictionary:
#         print(dictionary[type])
#     else:
#         print("từ này không nằm trong từ điển")
#     nhap = input("bạn có muốn thoát không : (Y/N) ").lower()
#     if nhap == "y" :
#         break 
#     elif nhap == "n":
#         break 
tap_nguoi=[]
nguoi_1 ={
    "name":"nguyen van a",
    "age":12,
    "add":"ha noi",
    "sđt":["0123","43434"]
}
tap_nguoi.append(nguoi_1)
nguoi_2 ={
    "name":"nguyen van b",
    "age":12,
    "add":"ha noi",
    "sđt":["0123","43434"]
}

tap_nguoi.append(nguoi_2)
# print(tap_nguoi[0]["age"])
for v in tap_nguoi:
    print(v["name"])
    

    

