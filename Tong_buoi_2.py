# tính tổng. viết chương trình tính tổng hai số a=5 và b=10
a = 5 
b = 10
print (a+b)
# tính hiệu. viết chương trình tính tổng hai số a = 15 và b = 7
a = 15
b = 7
print (a-b)
# tính tích .viết chương trình tính tích hai số a = 3 và b = 4
a = 3
b = 4
print (a*b)
# tính thương. viết chươg trình tính thương hai số a = 20 và b = 4
a = 20
b = 4
print (a/b)
# Tính lũy thừa Viết chương trình tính lũy thừa của số a = 2 lên mũ b = 3.
a = 2
b = 3
print (pow(a,b))
# Tính chia lấy dư Viết chương trình tính phần dư của phép chia a = 17 chia cho b = 5.
a = 17
b = 5
print (a%b)
# Tính trung bình Viết chương trình tính trung bình của ba số a = 5, b = 10, và c = 15.
a = 5
b = 10
c = 15
print ((a+b+c)/3)
# Tính chu vi hình chữ nhật Viết chương trình tính chu vi của hình chữ nhật có chiều dài 
# d = 10 và chiều rộng w = 5.
d = 10
w = 5
print ((d+w)*2)
# Tính diện tích hình chữ nhật Viết chương trình tính diện tích của hình chữ nhật có chiều 
# dài d = 10 và chiều rộng w = 5.
d = 10
w = 5
print (d*w)
# Tính chu vi hình vuông Viết chương trình tính chu vi của hình vuông có cạnh a = 6.
a = 6
print (a*4)
# Tính diện tích hình vuông Viết chương trình tính diện tích của hình vuông có cạnh a = 6.
a = 6
print (a*a)
# Tính diện tích hình tròn Viết chương trình tính diện tích của hình tròn có 
# bán kính r = 7. (Gợi ý: Diện tích hình tròn=π * r ^ 2, với π=3.14).
r = 7
print (3.14*r*r)
# Tính chu vi hình tròn Viết chương trình tính chu vi của hình tròn 
# có bán kính r = 7. (Gợi ý: Chu vi hình tròn=2 * π * r, với π=3.14).
r = 7
print (2*3.14*r)
# Bài tập về toán tử chia lấy phần dư (%)
# Chia lấy phần dư Viết chương trình chia a = 10 cho b = 3 và in ra phần dư.
a = 10
b = 3 
print (a//b)
# Chia lấy phần dư với số âm Viết chương trình chia a = -15 cho b = 4 và in ra phần dư.
a = -15
b = 4
print (a//b)
# Chia lấy phần dư với số lớn Viết chương trình chia a = 12345 cho b = 10 và in ra phần dư.
a = 12345
b = 10
print (a//b)
# Chia lấy phần dư với số nhỏ Viết chương trình chia a = 7 cho b = 5 và in ra phần dư.
a = 7
b = 5
print (a//b)
# Bài tập về toán tử lũy thừa (**)
# Lũy thừa cơ bản Viết chương trình tính a = 2 lũy thừa b = 3 và in ra kết quả.
a = 2
b = 3
print (pow(a,b))
# Lũy thừa số âm Viết chương trình tính a = 5 lũy thừa b = -1 và in ra kết quả.
a = 5
b = -1
print (pow(a,b))
# Lũy thừa số lớn Viết chương trình tính a = 10 lũy thừa b = 4 và in ra kết quả.
a = 10 
b = 4
print (pow(a,b))
# Lũy thừa số nhỏ Viết chương trình tính a = 3 lũy thừa b = 2 và in ra kết quả.
a = 3
b = 2
print (pow(a,b))
# Lũy thừa của một Viết chương trình tính a = 7 lũy thừa b = 0 và in ra kết quả.
a = 7
b = 0
print (pow(a,b))
# Bài tập về toán tử chia lấy phần nguyên (//)
# Chia lấy phần nguyên cơ bản Viết chương trình chia a = 10 cho b = 3 và in ra phần nguyên của kết quả.
a = 10
b = 3
print (a//b)
# Chia lấy phần nguyên với số âm Viết chương trình chia a = -15 cho b = 4 và in ra phần nguyên của kết quả.
a = -15
b = 4
print (a//b)
# Chia lấy phần nguyên với số lớn Viết chương trình chia a = 12345 cho b = 10 và in ra phần nguyên của kết quả.
a = 12345
b = 10 
print (a//b)
# Chia lấy phần nguyên với số nhỏ Viết chương trình chia a = 7 cho b = 5 và in ra phần nguyên của kết quả.
a = 7
b = 5
print (a//b)
# Chia lấy phần nguyên với số nhỏ hơn một Viết chương trình chia a = 7 cho b = 1 và in ra phần nguyên của kết quả.
a = 7
b = 1
print (a//b)
# Thực hành luyện tập cấu trúc điều kiện
# 1. Viết chương trình yêu cầu người dùng nhập vào một số và kiểm tra xem số đó là chẵn hay lẻ.
so = int(input("Nhập vào một số: "))
if so % 2 == 0:
    print(f"Số {so} là số chẵn.")
else:
    print(f"Số {so} là số lẻ.")
# 2. Viết chương trình kiểm tra xem một năm cho trước có phải là năm nhuận hay không.
nam = int(input("Nhập vào một năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")
# 3. Viết chương trình yêu cầu người dùng nhập vào điểm số của họ. 
# Kiểm tra và in ra thông điệp dựa trên điểm số: đậu ( >= 50) hoặc rớt ( < 50).
diem = int(input("nhập vào một số : "))
if (diem < 50 ):
    print ("rớt")
else: 
    print("đậu")
# 4. Viết chương trình yêu cầu người dùng nhập vào mật khẩu.
# Kiểm tra và in ra thông điệp xem mật khẩu có đúng không(mật khẩu đúng là "python").
matkhau = input("Hãy hập mật khẩu của bạn:")
if(matkhau == "python"): 
    print("Mật khẩu đúng")
else: 
    print("Mật khẩu không đúng ")
# 5. Viết chương trình yêu cầu người dùng nhập vào một số. 
# Kiểm tra và in ra thông điệp xem số đó có chia hết cho cả 3 và 5 hay không.
x = int(input(" nhập một số "))
if (x % 3 ==0 and x % 5 == 0) :
    print ("x chia hêt cho 3 và 5")
else:
    print ("x không chia hết cho 3 và 5")
# 1. Viết chương trình kiểm tra xem một số cho trước là chẵn hay lẻ sử dụng shorthand if -else .
a = int(input(" nhập một số " ))
if (a % 2 == 0 ):
    print ("chẵn")
else :
    print("lẻ")
# 2. Viết chương trình hỏi tuổi của người dùng và in ra thông điệp "Trẻ em" nếu dưới 13 tuổi, ngược lại in ra "Không phải trẻ em".
# python
tuoi = int(input("nhập tuổi của bạn"))
if (tuoi <13):
    print("trẻ em")
else:
    print("không phải trẻ em")
# 3. Viết chương trình kiểm tra chiều cao và in ra "Cao" nếu trên 180 cm, ngược lại in ra "Không cao".
chieucao = int(input("nhập chiều cao của bạn"))
if (chieucao > 180):
    print("cao")
else: 
    print("không cao")
# 4. Viết chương trình kiểm tra nhiệt độ và in ra "Nóng" nếu trên 30 độ C, ngược lại in ra "Không nóng".
nhiet_do = int(input("nhập vào nhiệt độ"))
if (nhiet_do > 30):
    print("nóng")
else:
    print("không nóng")
# 5. Viết chương trình kiểm tra mật khẩu và in ra "Mật khẩu đúng" nếu mật khẩu là "python", 
# ngược lại in ra "Mật khẩu sai".
passw = input("nhập mật khẩu")
if (passw == "python" ):
    print("mật khẩu đúng")
else:
    print("không đúng")
# 6. Viết chương trình yêu cầu người dùng nhập vào độ dài ba cạnh của một tam giác. 
# Kiểm tra và in ra thông điệp xem đó có phải là tam giác đều, tam giác cân hay tam giác thường.
do_dai_1 = float(input("Nhập vào độ dài cạnh thứ 1 của tam giác"))
do_dai_2 = float(input("Nhập vào độ dài cạnh thứ 2 của tam giác"))
do_dai_3 = float(input("Nhập vào độ dài cạnh thứ 3 của tam giác"))
if do_dai_1 == do_dai_2 and do_dai_1 == do_dai_3 and do_dai_2 == do_dai_3: 
    print("Đây là tam giác đều")
else:
    if do_dai_1 == do_dai_2 or do_dai_1 == do_dai_3 or do_dai_2 == do_dai_3:
        print("Đây là tam giác cân")
    else: print("Đây là tam giác thường")
# 7.Viết chương trình yêu cầu người dùng nhập vào số đại diện cho ngày trong tuần(1-7). 
# Kiểm tra và in ra thông điệp tương ứng với ngày đó(1: Thứ Hai, 2: Thứ Ba, ..., 7: Chủ Nhật).
ngay_trong_tuan = int(input("Nhập vào một ngày trong tuần (từ 1 đến 7): "))
if ngay_trong_tuan == 1: print("Thứ 2")
if ngay_trong_tuan == 2: print("Thứ 3")
if ngay_trong_tuan == 3: print("Thứ 4")
if ngay_trong_tuan == 4: print("Thứ 5")
if ngay_trong_tuan == 5: print("Thứ 6")
if ngay_trong_tuan == 6: print("Thứ 7")
if ngay_trong_tuan == 7: print("Chủ Nhật")
# 8. Viết chương trình yêu cầu người dùng nhập vào điểm số của họ. 
# Kiểm tra và in ra thông điệp đánh giá dựa trên điểm số: xuất sắc (90-100), giỏi (70-89), khá (50-69), trung bình (< 50).
diem_so= int(input("Nhập điểm từ 10 - 100: "))
if diem_so >= 90:
    print("Xuất sắc")
elif diem_so >= 70:
    print("Giỏi")
elif diem_so >= 50:
    print("Khá")
else:
    print("Trung bình")
# 9. Viết chương trình yêu cầu người dùng nhập vào giờ(24 giờ). 
# Kiểm tra và in ra thông điệp dựa trên giờ: buổi sáng(5-11 giờ), buổi chiều(12-17 giờ), buổi tối(18-22 giờ), ban đêm(23-4 giờ).
gio = int(input("Nhập vào một giờ trong ngày (0 - 24h): "))
if gio >= 5 and gio <= 11:
    print("Sáng")
elif gio >= 12 and gio <= 17:
    print("Chiều")
elif gio >= 18 and gio <= 22:
    print("Tối")
else:
    print("Đêm")
# 10. Viết chương trình yêu cầu người dùng nhập vào chiều cao của họ(tính bằng cm). 
# Kiểm tra và in ra thông điệp dựa trên chiều cao: thấp(dưới 150 cm), trung bình(150-180 cm), cao(trên 180 cm).
chieu_cao = int(input("Nhap chieu cao: "))
if chieu_cao < 150:
    print("Thấp")
elif chieu_cao >= 150 and chieu_cao <= 180:
    print("Trung bình")
else:
    print("Cao")