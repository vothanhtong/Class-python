# * BÀI TẬP
# Tính tổng Viết chương trình tính tổng của hai số a = 5 và b = 10.
a = 5
b = 10
print(a+b)
# Tính hiệu Viết chương trình tính hiệu của hai số a = 15 và b = 7.
a = 15
b = 7
print(a-b)
# Tính tích Viết chương trình tính tích của hai số a = 3 và b = 4.
a = 3
b = 4
print(a*b)
# Tính thương Viết chương trình tính thương của hai số a = 20 và b = 4.
a = 20
b = 4
print(a/b)
# Tính lũy thừa Viết chương trình tính lũy thừa của số a = 2 lên mũ b = 3.
a = 2
b = 3
print(a**b)
# Tính chia lấy dư Viết chương trình tính phần dư của phép chia a = 17 chia cho b = 5.
a = 17
b = 5
print(a%b)
# Tính trung bình Viết chương trình tính trung bình của ba số a = 5, b = 10, và c = 15.
a = 5
b = 10
c = 15
print((a+b+c)/3)
# Tính chu vi hình chữ nhật Viết chương trình tính chu vi của hình chữ nhật có chiều dài 
# d = 10 và chiều rộng w = 5.
d = 10
w = 5
print((d+w)*2)
# Tính diện tích hình chữ nhật Viết chương trình tính diện tích của hình chữ nhật có chiều 
# dài d = 10 và chiều rộng w = 5.
d = 10
w = 5
print(d*w)
# Tính chu vi hình vuông Viết chương trình tính chu vi của hình vuông có cạnh a = 6.
a = 6
print(a*4)
# Tính diện tích hình vuông Viết chương trình tính diện tích của hình vuông có cạnh a = 6.
a = 6
print(a*a)
# Tính diện tích hình tròn Viết chương trình tính diện tích của hình tròn có 
# bán kính r = 7. (Gợi ý: Diện tích hình tròn=π * r ^ 2, với π=3.14).
r = 7
pi = 3.14
print(r**r*pi)
# Tính chu vi hình tròn Viết chương trình tính chu vi của hình tròn 
# có bán kính r = 7. (Gợi ý: Chu vi hình tròn=2 * π * r, với π=3.14).
r = 7
pi = 3.14
print(2*r*pi)
# Bài tập về toán tử chia lấy phần dư (%)
# Chia lấy phần dư Viết chương trình chia a = 10 cho b = 3 và in ra phần dư.
a = 10
b = 3
print(a%b)
# Chia lấy phần dư với số âm Viết chương trình chia a = -15 cho b = 4 và in ra phần dư.
a = -15
b = 4
print(a%b)
# Chia lấy phần dư với số lớn Viết chương trình chia a = 12345 cho b = 10 và in ra phần dư.
a = 12345
b = 10
print(a%b)
# Chia lấy phần dư với số nhỏ Viết chương trình chia a = 7 cho b = 5 và in ra phần dư.
# Bài tập về toán tử lũy thừa (**)
a = 7
b = 5
print(a%b)
# Lũy thừa cơ bản Viết chương trình tính a = 2 lũy thừa b = 3 và in ra kết quả.
a = 2
b = 3
print(a**b)
# Lũy thừa số âm Viết chương trình tính a = 5 lũy thừa b = -1 và in ra kết quả.
a = 5
b = -1
print(pow(a,b))
# Lũy thừa số lớn Viết chương trình tính a = 10 lũy thừa b = 4 và in ra kết quả.
a = 10
b = 4
print(a**b)
# Lũy thừa số nhỏ Viết chương trình tính a = 3 lũy thừa b = 2 và in ra kết quả.
a = 3
b = 2
print(a**b)
# Lũy thừa của một Viết chương trình tính a = 7 lũy thừa b = 0 và in ra kết quả.
a = 7
b = 0
print(a**b)
# Bài tập về toán tử chia lấy phần nguyên (//)
# Chia lấy phần nguyên cơ bản Viết chương trình chia a = 10 cho b = 3 và in ra phần nguyên của kết quả.
a = 10
b = 3
print(a//b)
# Chia lấy phần nguyên với số âm Viết chương trình chia a = -15 cho b = 4 và in ra phần nguyên của kết quả.
a = -15
b = 4
print(a//b)
# Chia lấy phần nguyên với số lớn Viết chương trình chia a = 12345 cho b = 10 và in ra phần nguyên của kết quả.
a = 12345
b = 10
print(a//b)
# Chia lấy phần nguyên với số nhỏ Viết chương trình chia a = 7 cho b = 5 và in ra phần nguyên của kết quả.
a = 7 
b = 5
print(a//b)
# Chia lấy phần nguyên với số nhỏ hơn một Viết chương trình chia a = 7 cho b = 1 và in ra phần nguyên của kết quả.
a = 7
b = 1
print(a//b)
# Thực hành luyện tập cấu trúc điều kiện
# 1. Viết chương trình yêu cầu người dùng nhập vào một số và kiểm tra xem số đó là chẵn hay lẻ.
s=int(input("nhập vào số: "))
if s%2==0:
    print("đây là số chẵn")
else:
    print("đây là số lẻ")
# 2. Viết chương trình kiểm tra xem một năm cho trước có phải là năm nhuận hay không.
s=int(input("nhập vào số năm"))
if s%4==0 and s % 100 != 0 or (s % 400 == 0):
   print("đây là năm nhuận")
else:
   print("đây là không phải năm nhuận ") 
# 3. Viết chương trình yêu cầu người dùng nhập vào điểm số của họ. 
# Kiểm tra và in ra thông điệp dựa trên điểm số: đậu ( >= 50) hoặc rớt ( < 50).
s=int(input("nhập vào số điểm của bạn"))
if s>=50:
    print("đậu")
else:
    print("rớt")
# 4. Viết chương trình yêu cầu người dùng nhập vào mật khẩu. 
# Kiểm tra và in ra thông điệp xem mật khẩu có đúng không(mật khẩu đúng là "python").
s=input("nhập mật khẩu của bạn: ")
if (s == "python"):
    print("mật khẩu đúng")
else:
    print("mật khẩu sai")
# 5. Viết chương trình yêu cầu người dùng nhập vào một số. 
# Kiểm tra và in ra thông điệp xem số đó có chia hết cho cả 3 và 5 hay không.
s=int(input("nhập vào một số: "))
if s%3==0 and s%5==0:
   print("số này chia hết cho 3 và 5")
else:
   print("số này không chia hết cho 3 và 5")
# 1. Viết chương trình kiểm tra xem một số cho trước là chẵn hay lẻ sử dụng shorthand if -else .
s=int(input("nhập vào một số: "))
if s%2==0:
    print("đây là số chẵn")
else:
    print("đây là số lẻ")
# 2. Viết chương trình hỏi tuổi của người dùng và in ra thông điệp "Trẻ em" nếu dưới 13 tuổi, ngược lại in ra "Không phải trẻ em".
# python
s=int(input("nhập vào số tuổi của bạn: "))
if (s>=13):
    print("không phải trẻ em")
else:
    print("đây là trẻ em")
# 3. Viết chương trình kiểm tra chiều cao và in ra "Cao" nếu trên 180 cm, ngược lại in ra "Không cao".
s=int(input("nhập vào chiều cao của bạn: "))
if (s>180):
    print("cao")
else:
    print("thấp")
# 4. Viết chương trình kiểm tra nhiệt độ và in ra "Nóng" nếu trên 30 độ C, ngược lại in ra "Không nóng".
s=int(input("nhập vào nhiệt độ của bạn: "))
if (s>30):
    print("nóng")
else:
    print("không nóng")
# 5. Viết chương trình kiểm tra mật khẩu và in ra "Mật khẩu đúng" nếu mật khẩu là "python", 
# ngược lại in ra "Mật khẩu sai".
s=input("nhập vào mật khẩu của bạn")
if (s=="python"):
    print("mật khẩu đúng")
else:
    print("mật khẩu sai")
# 6. Viết chương trình yêu cầu người dùng nhập vào độ dài ba cạnh của một tam giác. 
# Kiểm tra và in ra thông điệp xem đó có phải là tam giác đều, tam giác cân hay tam giác thường.
a=int(input("nhập vào độ dài cạnh thứ nhất: "))
b=int(input("nhập vào độ dài cạnh thứ hai: "))
c=int(input("nhập vào độ dài cạnh thứ ba: "))
if (a==b==c):
    print("đây là tam giác điều")
else:
    if (a==b or a==c or b==c):
        print("đây là tam giác cân")
    else:
        print("đây là ta, giác thường")
# 7.Viết chương trình yêu cầu người dùng nhập vào số đại diện cho ngày trong tuần(1-7). 
# Kiểm tra và in ra thông điệp tương ứng với ngày đó(1: Thứ Hai, 2: Thứ Ba, ..., 7: Chủ Nhật).
s=int(input("nhập vào một số đại diện trong tuần từ 2-8): "))
if (s==2): print("đây là thứ hai")
if (s==3): print("đây là thứ ba ")
if (s==4): print("đây là thứ tư")
if (s==5): print("đây là thứ năm")
if (s==6): print("đây là thứ sáu")
if (s==7): print("đây là thứ bảy")
if (s==8): print("đây là chủ nhật")
# 8. Viết chương trình yêu cầu người dùng nhập vào điểm số của họ. 
# Kiểm tra và in ra thông điệp đánh giá dựa trên điểm số: xuất sắc (90-100), giỏi (70-89), khá (50-69), trung bình (< 50).
s=int(input("nhập vào số điểm của bạn (lưu ý nhập từ 1 đến 100): "))
if s >= 90:
    print("suất sắc")
elif s>=70:
    print("giỏi")
elif s>=50:
    print("khá")
elif s<50:
    print("trung bình ")
else: print("không có điểm này")
# 9. Viết chương trình yêu cầu người dùng nhập vào giờ(24 giờ). 
# Kiểm tra và in ra thông điệp dựa trên giờ: buổi sáng(5-11 giờ), buổi chiều(12-17 giờ), buổi tối(18-22 giờ), ban đêm(23-4 giờ).
s=int(input("hãy nhập vào số giờ (từ 0 đến 24): "))
if s >=5 and s<=11 :
    print("buổi sáng")
elif s>=12 and s<=17:
    print("buổi chiều")
elif s>=18 and s<=22:
    print("buổi tối")
elif s>=23 and s<=4:
    print("ban đêm")
else:
    print("bạn nhập sai")
# 10. Viết chương trình yêu cầu người dùng nhập vào chiều cao của họ(tính bằng cm). 
# Kiểm tra và in ra thông điệp dựa trên chiều cao: thấp(dưới 150 cm), trung bình(150-180 cm), cao(trên 180 cm).
s=int(input("nhập vào chiều cao của bạn (tính bằng cm): "))
if s > 180 :
    print("bạn cao quá ")
elif s>=150 and s<=180 :
    print("bạn cao trung bình")
else:
    print("bạn thấp quá")

# CẤU TRÚC VÒNG LẬP FOR & WHILE
# 1. VÒNG LẶP FOR
# Cú pháp:
# for bien_lap in chuoi_lap:
#     Khối lệnh của for

# Trong cú pháp trên, chuoi_lap là chuỗi cần lặp, bien_lap là biến nhận giá trị của từng mục bên
# trong chuoi_lap trên mỗi lần lặp. Vòng lặp sẽ tiếp tục cho đến khi nó lặp tới mục cuối cùng trong chuỗi.

# BÀI TẬP ÁP DỤNG:

s="Thanh Tong"
for ch in s :
    print("ch")
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
