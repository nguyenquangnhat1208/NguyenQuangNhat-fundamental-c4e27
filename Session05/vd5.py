# n = int(input("Nhập số :"))

# for i in range(2,n):
#     if n%i ==0:
#         print("không là số nguyên tố")
#         break
        
#     else :
#         print("đây là số nguyên tố")
#         break
def is_prime (n):
    if n <2:
        return False
    for v in range (2,n):
        if n % v == 0:
            return False
    return True
so = int(input("nhap so can kiem tra :"))
for v in range (2,so+1):
    if is_prime(v):
        print("so nguyen to la",v)
# if is_prime(so) :
#     print("la so nguyen to ")
# else:
#     print("khong la so nguyen to ")

