#Cấu trúc vòng lặp FOR, WHILE
#1. Vòng lặp FOR
# Cú pháp
# for bien_lap in chuoi_lap:
#   <Khối lệnh cần thực hiện>
#Trong cú pháp trê, chuoi_lap là chuỗi cần lặp, bien_lap là biến nhận giá trị của từng mục bên
#trong chuoi_lap trên mỗi lần lặp. Vòng lặp sẽ tiếp tục cho đến khi nó lặp tới mục cuối cùng trong chuỗi.
# Vd
chuoi = 'Thanh Tong'
for ch in chuoi:
    print(ch)

# Break và Continue
# chuoi = 'Thanh Tòng'
# for ch in chuoi:
#     if ch == 'A':
#         continue # Bỏ qua lần lặp hiện tại
#     if ch == 'y':
#         break # Dừng vòng lặp
#     print(ch, end="") #end="" là để nối các ký tự lại trong chuỗi
# Câu lệnh range(start, stop, step)
# Câu lệnh range(n): trả lại vùng giá trị gồm n số từ 0 đến n-1.
# Cú pháp của lệnh lặp với số lần biết trước như sau:
# for <biến_lặp> in range(n):
#     <Khối lệnh>


# ===============
# for <biến_lặp> in range(1, n, 2)
#     <khối lệnh>


# BÀI TẬP ÁP DỤNG:
# 1. Viết chương trình sử dụng vòng lặp for để in ra các số từ 1 đến 10.
for i in range(1,11):
    print(i, end= " ")
print("\n")
# 2. Viết chương trình sử dụng vòng lặp for để tính tổng các số từ 1 đến 100 và in kết quả.
s = 0
for i in range(1, 101):
    s += i
print("Tổng các số từ 1 đến 100 là: ", s)

# 3. Viết chương trình sử dụng vòng lặp for để in ra các số chẵn từ 1 đến 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
# 4. Viết chương trình sử dụng vòng lặp for để in ra các
# phần tử của danh sách sau: ['apple', 'banana', 'cherry', 'date'].
do_an = ['apple', 'banana', 'cherry', 'date']
for i in range (len(do_an)):
    print (do_an [i],end=" ")
print("\n")
# 5. Viết chương trình sử dụng vòng lặp for để in ra từng ký tự của chuỗi "Hello, World!".
chao = " Hello,World "
for i in range (len(chao)):
    print(chao[i],end=" ")
print("\n")
# BÀI TẬP LUYỆN TẬP
# 1. Viết chương trình sử dụng vòng lặp for để tính giai thừa của một số nguyên dương n.
n = int(input("Nhập một số nguyên dương: "))
s = 1
for i in range(1, n + 1):
    s *= i
print(f"Giai thừa của {n} là {s}")
print("\n")
# 2. Viết chương trình sử dụng vòng lặp for để in ra bảng cửu chương từ 1 đến 10.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}", end='\t')
    print()
# 3. Viết chương trình sử dụng vòng lặp for để in ra tam giác sao có chiều cao n.
# Chiều cao của tam giác
n = int(input("Nhập chiều cao của tam giác: "))
for i in range(1,n + 1):
    print("*" * i)
# 4. Viết chương trình sử dụng vòng lặp for để kiểm tra xem một số nguyên n có phải là số nguyên tố hay không.
n = int(input("nhập số nguyên tố "))
i = 2
while n <= 0:
    n = int(input("nhập lại số nguyên tố dương"))
else:
    while i < n :
        if n % i == 0:
            print("đây không phải là số nguyên tố")
            break 
        i = i + 1
    if i == n :print("đây là số nguyên tố") 

# 5. Viết chương trình sử dụng vòng lặp for để tìm ước số chung lớn nhất(ƯCLN) của hai số nguyên dương a và b.
a = int(input("nhập số nguyên dương a: "))
b = int(input("nhập số nguyên dương b: "))
ucln = min (a,b)
while ucln > 0:
    if a %  ucln == 0 and b %  ucln == 0 :
       print("UCLN của hai số là:", ucln )
       break
    ucln -= 1

# 6. Viết chương trình tính tổng các số chẵn từ 1 đến n, với n là số nguyên dương nhập từ người dùng. (Dùng while)
n = int(input("Nhập số nguyên dương n: "))
tong_chan = 0
i = 2
while i <= n:
    tong_chan += i 
    i += 2  
print("Tổng các số chẵn từ 1 đến", n, "là:", tong_chan)
# 7. Viết chương trình tính tổng các số lẻ từ 1 đến n, với n là số nguyên dương nhập từ người dùng. (Dùng while)
n = int(input("Nhập số nguyên dương n: "))
tong_le = 0
i = 1
while i <= n:
    tong_le += i 
    i += 2 
print("Tổng các số lẻ từ 1 đến", n, "là:", tong_le)

