def kiem_tra_so_nt(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            return False
    return True
number = int(input("Nhập vào số cần kiểm tra: "))
if kiem_tra_so_nt(number):
    print(number, "là số nguyên tô.")
else:
    print(number, "không phải là số nguyên tố.")