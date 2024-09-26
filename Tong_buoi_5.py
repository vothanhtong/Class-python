#  Viết hàm yêu cầu người dùng nhập họ tên rồi đưa lời chào ra màn hình
def nhapten():
    name = input("nhập họ tên của bạn: ")
    print("xin chào,"+name)
nhapten()
# 2. Viết hàm tính tổng, hiệu, tích, chia lấy nguyên, chia lấy dư(Có kiểm tra số bị chia có bằng 0 hay không?)
# hai số nguyên a và b rồi in ra màn hình = int(input("nhập số nguyên a: "))
a=int(input(" nhập số nguyên a: "))
b=int(input(" nhập số nguyên b: "))
def tinh_toan(a,b):
    tong = a+b
    hieu = a-b
    tich = a*b
    if b !=0 :
         thuong = a/b
    else: thuong = b/a 
    print(f"tổng của {a} và {b} là {tong}" )
    print(f"hiệu của {a}và{b} là {hieu}")
    print(f"tích của {a}và {b} là {tich}")
    print(f"thương của {a} và {b} là {thuong}")
tinh_toan(a,b)   
# 3. Viết hàm kiểm tra số chẳn hoặc lẻ với n là số nguyên dương người dùng nhập từ bàn phím rồi
# in kết quả ra màn hình
s=int(input("nhập một số bất kỳ: "))
def chan_le ():
    if s%2==0:
        print("đây là số chẵn: ")
    else:
        print("đây là số chẵn: ")
chan_le()
# 4. Viết hàm tính giá trị trung bình của hai số nguyên dương được người dùng nhập từ bàn phím rồi
# in kết quả ra màn hình
a = int(input("nhập số nguyên a: "))
b = int(input("nhập số nguyên b: "))
def tinh_toan(a,b):
    trung_binh = (a+b)/2
    print(f"trung bình của {a} và {b} là {trung_binh}")
tinh_toan(a,b)
# 5. Viết hàm tìm số lớn nhất của hai số nguyên dương được người dùng nhập từ bàn phím rồi
# in kết quả ra màn hình
# cách 1 
a=int(input("nhập số thứ nhất: "))
b=int(input("nhập số thứ hai: "))
def in_ra (a,b):
    return a,b
print(f"số lớn nhất là: {max (a,b)}")
in_ra()
# cách 2
def so_lon_nhat():
    a=int(input("nhập số lớn nhất: "))
    b=int(input("nhập số thứ hai: "))
    if a>b: lon_nhat = a
    else: lon_nhat = b
    print(f"số lớn nhất là: {max(a,b)}")
so_lon_nhat()
# BÀI TẬP LUYỆN TẬP (PHẠM VI BIẾN)
# 1. Hàm kiểm tra một số có phải là số nguyên tố không
def tim_so_nguyen_to (n):
    gia_su = True
    if n<=1:
        gia_su = False 
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i==0:
             gia_su = False
             break 
    return gia_su

s = int(input("Nhập vào một số: "))
if tim_so_nguyen_to(s):
    print(f"{s} là số nguyên tố.")
else:
    print(f"{s} không phải là số nguyên tố.")

# 2. Hàm xác định loại tam giác dựa trên độ dài ba cạnh
def tam_giac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Tam giác đều"
        elif a == b or a == c or b == c:
            return "Tam giác cân"
        else:
            return "Tam giác thường"
    else:
        return "Không phải là tam giác"
a = int(input("Nhập độ dài cạnh thứ nhất: "))
b = int(input("Nhập độ dài cạnh thứ hai: "))
c = int(input("Nhập độ dài cạnh thứ ba: "))
print(tam_giac(a, b, c))
# 3. Hàm kiểm tra tuổi để xác định có đủ điều kiện bầu cử hay không
def bau_cu():
    if a>=18:
        return "đủ tuổi bầu cử"
    else:
        return"không dủ tuổi để bàu cử"
a=int(input("nhập số tuổi của bạn: "))
print(bau_cu())
# 4. Hàm tính tổng các số từ 1 đến n
def tinh_tong(n):
    tong =0
    i=1
    while i<= n :
     tong+=i
     i+=1
    return tong
n=int(input("nhập vào một số bất kỳ: "))
print("tổng các chữ số từ 1 dến ",n,"là" , tinh_tong(n) )
# 5. Hàm in ra các số chẵn từ 1 đến n sử dụng vòng lặp while
def chan (n):
    tong = 0
    i=2
    while i<=n:
        tong+=i
        i+=2
    return tong
n=int(input("nhập vào số bất kỳ để tính tổng chẵn: "))
print("tổng các số chẵn từ 1 đên ",n, "là" ,chan(n))
# 6. Hàm in ra các số lẻ từ 1 đến n sử dụng vòng lặp while
def le (n):
    tong=0
    i=1
    while i<=n:
        tong+=i
        i+=2
    return tong
n=int(input("nhập vào một số để tính số lẻ từ 1 đến n: "))
print("tổng các số lẻ từ 1 đến ",n, "là",le(n))
# 7. Hàm tính tổng các số từ 1 đến n 
def tong (n):
    tong=0
    for i in range (1,n+1):
        tong +=i
    return tong
n=int(input("nhập vào một số để tính tổng từ 1 đến số đoá: "))
tong(n)
print("tổng các số lẻ tù 1 đến ",n, "là",tong(n))
# 8. Hàm in ra các số chẵn từ 1 đến n 
def tong_chan (n):
    tong=0
    for i in range (2,n+1,2):
        tong+=i
    return tong 
n=int(input("nhập vào một số để tính tổng chẵn mà không dùng vòng lặp while: "))
print("Tổng các số chẵn từ 1 đến ",n, "là",tong_chan(n))
# 9. Hàm in ra các số lẻ từ 1 đến n sử dụng vòng lặp while
def tong_le (n):
    tong=0
    for i in range (1,n+1,2):
        tong+=i
    return tong
n=int(input("nhập vào một số để tính tổng lẽ mà không sử dụng vòng lặp while: "))
print("Tổng các chữ số lẻ từ 1 đến ",n, "là",tong_le(n))
# 10. Hàm in ra các số nguyên tố từ 1 đến n ***** cần hỏi ******
def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def in_cac_so_nguyen_to(n):
    for i in range(2, n + 1):
        if la_so_nguyen_to(i):
            print(i, end="" )
n = int(input("Nhập vào một số bất kỳ: "))
in_cac_so_nguyen_to(n)
# # 11. Hàm in ra dãy số Fibonacci từ 1 đến n
def in_day_so_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
n = int(input("Nhập vào một số bất kỳ: "))
in_day_so_fibonacci(n)
# # 12. Viết hàm tính UCLN của hai số nguyên nhập từ bàn phím và in ra màn hình
def tinh_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
ucln = tinh_ucln(a, b)
print("UCLN của", a, "và", b, "là:", ucln)
# BÀI TẬP ÁP DỤNG
# 1. Viết chương trình nhập vào một chuỗi, sau đó in ra chuỗi đó với tất cả các chữ cái viết hoa.
s=input("bạn nhập vào một chuỗi bất kỳ: ")
viet_hoa = len(s)
print("độ dài của chuỗi là: ",viet_hoa)
print(s.upper())
# 2. Viết chương trình nhập vào một chuỗi, sau đó xóa bỏ tất cả các khoảng trắng ở đầu và cuối chuỗi đó.
s=input("nhập vào một chuỗi (nhớ có khoảng trắng để tôi bỏ khoảng trắng nho:))) ")
print (s.strip().upper())
# 3. Viết chương trình nhập vào một chuỗi, tìm kiếm và thay thế tất cả các từ "Python" bằng "Java".
s = input("nhạp vào ký tự chuỗi: ")
print(s.find("phython"))
print(s.replace("python", "java"))  
# 4. Viết chương trình nhập vào một chuỗi, tách chuỗi đó thành danh sách các từ và
# sau đó gộp lại thành một chuỗi duy nhất với khoảng trắng ngăn cách các từ.
chuoi=input("nhập vào một chuỗi: ")
danh_sach= chuoi.split()
chuoi_moi= " ".join(danh_sach)
print(chuoi.split)
print("chuỗi sau khi gộp lại: ", chuoi_moi)
# BÀI TẬP LUYỆN TẬP
# 1. Viết chương trình yêu cầu người dùng nhập vào một chuỗi và in ra chuỗi đó dưới dạng chữ hoa và chữ thường.
s=input("bạn hãy nhập vào một chuỗi bất kỳ: ")
print (s.upper())
print(s.lower())
# 2. Viết chương trình yêu cầu người dùng nhập vào một chuỗi và in ra chuỗi đó
# sau khi đã loại bỏ khoảng trắng ở đầu và cuối.
s=input("nhập vào chuỗi ký tựu: ")
print(s.strip())
# 3. Viết chương trình yêu cầu người dùng nhập vào một chuỗi,
# sau đó yêu cầu nhập vào ký tự cần thay thế và ký tự thay thế. In ra chuỗi sau khi đã thay thế.
n=input("nhập vào một chuỗi: ")
print(n.find("python"))
print(n.replace("python","java"))
# 4. Viết chương trình yêu cầu người dùng nhập vào một câu và in ra danh sách các từ trong câu đó.
n=input("nhập vào một chuỗi ký tự: ")
print(n.split())
# 5. Viết chương trình yêu cầu người dùng nhập vào một danh sách
# các từ(dùng dấu phẩy để ngăn cách) và in ra chuỗi sau khi đã nối các từ đó bằng dấu cách.
s=input("nhập vào một danh sách dùng dấu phẩy để ngăn cách: ")
moi=s.split(",")
chuoi_moi = " ".join(moi).strip()
print("Chuỗi sau khi nối các từ bằng dấu cách:", chuoi_moi)
# 6. Viết chương trình yêu cầu người dùng nhập vào hai chuỗi,
# kiểm tra xem chuỗi thứ hai có nằm trong chuỗi thứ nhất hay không.
chuoi_1=input("nhập vào một chuỗi thứ nhất: ")
chuoi_2=input("nhập vào một chuỗi thứ hai: ")
if chuoi_1 in chuoi_2:
    print("chuỗi thứ hai nằm trong chuỗi thứ nhất: ")
else:
    print("chuỗi thứ hai không nằm trong chuỗi thứ nhất: ")
# 7. Viết chương trình yêu cầu người dùng nhập vào một chuỗi và in ra chuỗi đó theo thứ tự ngược lại.
s=input("nhập vào một câu bất kỳ:")
print("in ra câu đảo ngược: " ,s[::-1])
# 8. Viết chương trình yêu cầu người dùng nhập vào một chuỗi và một ký tự,
# sau đó đếm số lần xuất hiện của ký tự đó trong chuỗi.
s=input("nhập vào một chuỗi bất kỳ: ")
n=input("tìm ký tự: ")
xuat_hien= s.count(n)
print(f"ký tự {n} xuất hiện {xuat_hien}lần trong chuỗi")
# 9. Viết chương trình yêu cầu người dùng nhập vào một chuỗi và
# kiểm tra xem chuỗi đó có phải là chuỗi đối xứng hay không.
def doi_xung(chuoi):
    if chuoi == chuoi[::-1]:
        return True
    else:
        return False
chuoi = input("Nhập vào một chuỗi: ")
if doi_xung(chuoi):
    print("Chuỗi này là đối xứng.")
else:
    print("Chuỗi này không đối xứng.")   
# 10. Viết chương trình yêu cầu người dùng nhập vào một đoạn văn bản và đếm số từ trong đoạn văn bản đó.
s=input("nhập vào một câu: ")
dem= s.split()
so_tu=len(dem)
print("số từ trong chuỗi trên là: ",so_tu)
# 11. Viết chương trình yêu cầu người dùng nhập vào một đoạn văn bản và tìm từ dài nhất trong đoạn văn bản đó.
# 11. Viết chương trình yêu cầu người dùng nhập vào một đoạn văn bản và tìm từ dài nhất trong đoạn văn bản đó.
s=input("nhập vào một văn bản: ")
dem=s.split()
tu_dai_nhat=max(dem,key=len)
print("từ dài nhất trong đoạn văn là: ",tu_dai_nhat)
# 12. Viết chương trình yêu cầu người dùng nhập vào một đoạn văn bản
# và một từ cần thay thế, sau đó nhập vào từ thay thế và in ra đoạn văn bản sau khi đã thay thế.
s=input("nhập vào một đoạn văn: ")
n=input("nhập vào từ cần thy thế: ")
t=input("từ cần thay thế: ")
moi= s.replace(n,t)
print("in ra văn bản đã thay thế: ",moi)
# 13. Viết chương trình yêu cầu người dùng nhập vào một danh sách
# các tên(dùng dấu phẩy để ngăn cách) và in ra danh sách các tên đó theo thứ tự bảng chữ cái.
s=input("nhập vào một danh sách bất kỳ: ")
s= [ten.strip() for ten in s.split(",")]
s.sort()
print("Danh sách các tên theo thứ tự bảng chữ cái là:")
for ten in s:
    print(ten)
# 14. Viết chương trình yêu cầu người dùng nhập vào một chuỗi ở dạng "Tên, Tuổi, Địa chỉ" và
# chuyển đổi chuỗi đó thành định dạng "Tên: [tên], Tuổi: [tuổi], Địa chỉ: [địa chỉ]".
s=input("nhập tên,tuổi ,địa chỉ của bạn: ")
ten,tuoi,dia_chi= s.split(",")
print(f"tên :{ten.split()}, tuổi: {tuoi.split()},địa chỉ: {dia_chi.split()}")
# 15. Viết chương trình yêu cầu người dùng nhập vào một đoạn văn bản và đếm số câu trong đoạn văn bản đó.
s=input("nhập vào một đoạn văn: ")
tach=s.split(".")
dem=len(tach)
print(f"số câu trong đoạn văn là:{dem} ")
# 16. Viết chương trình yêu cầu người dùng nhập vào một đoạn văn bản và tìm các từ
# xuất hiện nhiều nhất trong đoạn văn bản đó.
s = input("Nhập vào một đoạn văn bản: ")
n = s.split()
dem = {}
for word in n:
    dem[word] = dem.get(word, 0) + 1
max_word = max(dem, key=dem.get)
print(f"Từ xuất hiện nhiều nhất là: {max_word} ({dem[max_word]} lần)")
# BÀI TẬP ÁP DỤNG MẢNG MỘT CHIỀU ######################################################################################################################################
# Khai báo một mảng chứa 5 số bất kỳ. Truy cập và in ra giá trị của phần tử thứ 2 và phần tử cuối cùng.
so = []
for i in range(5):
    number = int(input(f"Nhập số thứ {i+1}: "))
    so.append(number)
print("Số thứ hai là:",so [1])
print("Số cuối cùng là:",so[-1])
# Thay đổi giá trị của phần tử đầu tiên và phần tử cuối cùng trong mảng.
so=[]
for i in range (5):
    nhap=int(input(f"nhập vào 5 số bất kỳ: {i+1}"))
    so.append(nhap)
print(f"số sau khi thay đổi là: {so}")
if len(so)>0:
    so[0]=int(input("nhập số thay đổi thứ nhất: "))
if len(so)>1:
    so[-1]=int(input("nhập số thay đổi cuối cùng: "))
print(f"danh sách sau khi thay đổi là: {so}")
# Thêm một số vào cuối mảng và một số vào vị trí thứ 3.
so=[]
for i in range (5):
    nhap=int(input(f"nhập vào 5 số bất kỳ:{i+1}   "))
    so.append(nhap)
print(f"số sau khi thay đổi là: {so}")
cuoi=int(input("thêm một số vào số cuối: "))
so.append(cuoi)
giua=int(input("thêm vào số thứ ba: "))
so.insert(2,giua)
print(f"in ra màng hình dãy số mới là: {so}")
# Xóa phần tử thứ 2 và phần tử có giá trị bằng 4 trong mảng.
so=[]
for i in range (5):
    nhap=int(input(f"nhập vào 5 số bất kỳ:{i+1}   "))
    so.append(nhap)
print(f"số sau khi thay đổi là: {so}")
so.remove(4)
so.pop(1)
print(f"in ra màng hình dãy số mới là: {so}")
# BÀI TẬP LUYỆN TẬP
# Bài 1: Viết chương trình để in tất cả các phần tử của một mảng số nguyên được nhập từ bàn phím.
n=int(input("nhập vào số lượng của một phần tử là: "))
so=[]
for i in range(n):
    dem=int(input(f"nhập số thứ {i+1}"))
    so.append(dem)
print("các phần tử của mảng là: ")
for i in so:
    print(i)
# Bài 2: Viết chương trình để tính tổng tất cả các phần tử trong một mảng số nguyên được nhập từ bàn phím.
m=int(input("nhập vào số lượng của một phần tử là: "))
so=[]
for i in range(m):
    dem=int(input(f"nhập vào phần tử thứ {i+1}: "))
    so.append(dem)
print(f"tổng các phần tử của mảng là: ",sum(so))
# Bài 3: Viết chương trình để đếm số phần tử chẵn trong một mảng số nguyên được nhập từ bàn phím.
s=int(input("nhập vào số lượng của các phần tử: "))
so=[]
for i in range(s):
    dem=int(input(f"nhập vào số thứ {i+1} "))
    so.append(dem)  
tong=sum(num for num in so if num % 2 == 0)    
print(" tổng các số phần tử chẵn trong mảng là:",tong)
# Bài 4: Viết hàm linear_search(arr, value) để tìm kiếm vị trí của giá trị value trong mảng arr.
# Nếu không tìm thấy, trả về - 1. Với mảng arr và value được nhập từ bàn phím.

# Bài 5: Viết chương trình để tìm và in ra giá trị lớn nhất trong một mảng số nguyên được nhập từ bàn phím.
s=int(input("nhập số nguyên vào các phần tử: "))
so=[]
for i in range(s):
    dem=int(input(f"nhập vào số thứ {i+1}: "))
    so.append(dem)
print("số lớn nhất trong mảng là: ",max(so))
# Bài 6: Viết hàm check_existence(arr, value) để kiểm tra xem giá trị
# value có tồn tại trong mảng arr hay không. Trả về True nếu có, ngược lại trả về False.
# Với mảng arr và value được nhập từ bàn phím.
def check_existence(arr, value):
    return value in arr
def main():
    arr_input = input("Nhập các giá trị của mảng, cách nhau bởi dấu phẩy: ")
    arr = arr_input.split(',')  
    arr = [item.strip() for item in arr]  
    value = input("Nhập giá trị cần kiểm tra: ").strip()
    exists = check_existence(arr, value)
    if exists:
        print(f"Giá trị '{value}' tồn tại trong mảng.")
    else:
        print(f"Giá trị '{value}' không tồn tại trong mảng.")
if __name__ == "__main__":
    main()
# Bài 7: Viết chương trình để sắp xếp một mảng số nguyên được nhập từ bàn phím theo
# thứ tự tăng dần sử dụng phương thức sort().
def main():
    # Nhập mảng từ bàn phím
    arr_input = input("Nhập các số nguyên cách nhau bởi dấu phẩy: ")
    arr = list(map(int, arr_input.split(',')))

    # Sắp xếp mảng theo thứ tự tăng dần
    arr.sort()
    print("Mảng sau khi sắp xếp theo thứ tự tăng dần:", arr)

if __name__ == "__main__":
    main()
# Bài 8: Viết chương trình để sắp xếp một mảng số nguyên được nhập từ bàn phím theo
# thứ tự giảm dần sử dụng hàm sorted().
def main():
    # Nhập mảng từ bàn phím
    arr_input = input("Nhập các số nguyên cách nhau bởi dấu phẩy: ")
    arr = list(map(int, arr_input.split(',')))

    # Sắp xếp mảng theo thứ tự giảm dần
    arr_sorted_desc = sorted(arr, reverse=True)
    print("Mảng sau khi sắp xếp theo thứ tự giảm dần:", arr_sorted_desc)

if __name__ == "__main__":
    main()

# Bài 9: Viết hàm bubble_sort(arr) để sắp xếp một mảng số nguyên được nhập từ bàn phím
# theo thứ tự tăng dần sử dụng thuật toán sắp xếp nổi bọt(Bubble Sort).
def bubble_sort(arr):
    """Sắp xếp mảng theo thứ tự tăng dần bằng thuật toán Bubble Sort."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    # Nhập mảng từ bàn phím
    arr_input = input("Nhập các số nguyên cách nhau bởi dấu phẩy: ")
    arr = list(map(int, arr_input.split(',')))

    # Sắp xếp mảng bằng thuật toán Bubble Sort
    bubble_sort(arr)
    print("Mảng sau khi sắp xếp theo thứ tự tăng dần:", arr)

if __name__ == "__main__":
    main()

# BÀI TẬP ÁP DỤNG
# Bài 1: Viết hàm kiểm tra ngày trong tuần dựa trên số đầu vào được nhập từ bàn phím ( 1 <= n <= 7)
def check_day_of_week(n):
    """Kiểm tra ngày trong tuần dựa trên số đầu vào."""
    days = ["Chủ nhật", "Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy"]
    if 1 <= n <= 7:
        return days[n-1]
    else:
        return "Số không hợp lệ!"

def main():
    n = int(input("Nhập số (1-7) để kiểm tra ngày trong tuần: "))
    print(check_day_of_week(n))

if __name__ == "__main__":
    main()

# Bài 2: Viết hàm phân loại học sinh dựa trên điểm số được nhập từ bàn phím (0 <= n <= 100 )
def classify_student(score):
    """Phân loại học sinh dựa trên điểm số."""
    if 90 <= score <= 100:
        return "Xuất sắc"
    elif 80 <= score < 90:
        return "Giỏi"
    elif 70 <= score < 80:
        return "Khá"
    elif 60 <= score < 70:
        return "Trung bình"
    elif 0 <= score < 60:
        return "Yếu"
    else:
        return "Điểm không hợp lệ"

def main():
    score = int(input("Nhập điểm số của học sinh (0-100): "))
    print(classify_student(score))

if __name__ == "__main__":
    main()

# BÀI TẬP LUYỆN TẬP
# Bài 1: Viết hàm check_even_odd(number) để kiểm tra xem một số là chẵn hay lẻ.
def check_even_odd(number):
    """Kiểm tra số chẵn hay lẻ."""
    return "Chẵn" if number % 2 == 0 else "Lẻ"

def main():
    number = int(input("Nhập một số nguyên: "))
    print(f"Số {number} là {check_even_odd(number)}.")

if __name__ == "__main__":
    main()

# Bài 2: Viết hàm identify_shape(sides) để xác định loại hình học dựa trên số cạnh.
def identify_shape(sides):
    """Xác định loại hình học dựa trên số cạnh."""
    if sides == 3:
        return "Tam giác"
    elif sides == 4:
        return "Hình vuông hoặc hình chữ nhật"
    elif sides == 5:
        return "Ngũ giác"
    elif sides == 6:
        return "Lục giác"
    else:
        return "Hình học không xác định"

def main():
    sides = int(input("Nhập số cạnh của hình: "))
    print(identify_shape(sides))

if __name__ == "__main__":
    main()

# Bài 3:  Viết hàm classify_age(age) để phân loại tuổi.
def classify_age(age):
    """Phân loại tuổi."""
    if 0 <= age <= 12:
        return "Trẻ em"
    elif 13 <= age <= 19:
        return "Vị thành niên"
    elif 20 <= age <= 64:
        return "Người trưởng thành"
    elif age >= 65:
        return "Người cao tuổi"
    else:
        return "Tuổi không hợp lệ"

def main():
    age = int(input("Nhập tuổi của bạn: "))
    print(classify_age(age))

if __name__ == "__main__":
    main()

# Bài 4: Viết hàm process_order(order) để xử lý đơn hàng dựa trên trạng thái.
def process_order(order_status):
    """Xử lý đơn hàng dựa trên trạng thái."""
    status_messages = {
        "pending": "Đơn hàng đang chờ xử lý.",
        "shipped": "Đơn hàng đã được gửi đi.",
        "delivered": "Đơn hàng đã được giao.",
        "canceled": "Đơn hàng đã bị hủy."
    }
    return status_messages.get(order_status, "Trạng thái đơn hàng không hợp lệ.")

def main():
    order_status = input("Nhập trạng thái đơn hàng (pending, shipped, delivered, canceled): ").strip()
    print(process_order(order_status))

if __name__ == "__main__":
    main()

# Bài 5: Viết hàm delivery_method(method) để phân loại hình thức giao hàng.
def delivery_method(method):
    """Phân loại hình thức giao hàng."""
    methods = {
        "standard": "Giao hàng tiêu chuẩn",
        "express": "Giao hàng nhanh",
        "same_day": "Giao hàng trong ngày"
    }
    return methods.get(method, "Hình thức giao hàng không hợp lệ.")

def main():
    method = input("Nhập hình thức giao hàng (standard, express, same_day): ").strip()
    print(delivery_method(method))

if __name__ == "__main__":
    main()

# Bài 6: Viết hàm month_name(month) để trả về tên tháng dựa trên số tháng.
def month_name(month):
    """Trả về tên tháng dựa trên số tháng."""
    months = [
        "Không hợp lệ", "Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4",
        "Tháng 5", "Tháng 6", "Tháng 7", "Tháng 8", "Tháng 9",
        "Tháng 10", "Tháng 11", "Tháng 12"
    ]
    return months[month] if 1 <= month <= 12 else "Số tháng không hợp lệ"

def main():
    month = int(input("Nhập số tháng (1-12): "))
    print(month_name(month))

if __name__ == "__main__":
    main()

# Bài 7: Viết hàm classify_animal(animal) để phân loại động vật dựa trên đặc điểm.
def classify_animal(animal):
    """Phân loại động vật dựa trên đặc điểm."""
    animals = {
        "cat": "Mèo",
        "dog": "Chó",
        "fish": "Cá",
        "bird": "Chim"
    }
    return animals.get(animal.lower(), "Động vật không xác định")

def main():
    animal = input("Nhập tên động vật (cat, dog, fish, bird): ").strip()
    print(classify_animal(animal))

if __name__ == "__main__":
    main()

# Bài 8: Viết hàm calculate_area(shape) để tính diện tích hình học dựa trên loại hình và thông số.
import math

def calculate_area(shape, *params):
    """Tính diện tích hình học dựa trên loại hình và thông số."""
    if shape == "circle":
        radius = params[0]
        return math.pi * radius ** 2
    elif shape == "rectangle":
        length, width = params
        return length * width
    elif shape == "triangle":
        base, height = params
        return 0.5 * base * height
    else:
        return "Hình học không xác định"

def main():
    shape = input("Nhập loại hình (circle, rectangle, triangle): ").strip()
    if shape == "circle":
        radius = float(input("Nhập bán kính của hình tròn: "))
        area = calculate_area(shape, radius)
    elif shape == "rectangle":
        length = float(input("Nhập chiều dài của hình chữ"))
# Bài 9: Viết hàm classify_employee(employee) để phân loại nhân viên dựa trên vai trò.
def classify_employee(role):
    """Phân loại nhân viên dựa trên vai trò."""
    roles = {
        "manager": "Quản lý",
        "developer": "Nhà phát triển",
        "designer": "Nhà thiết kế",
        "analyst": "Nhà phân tích",
        "intern": "Thực tập sinh"
    }
    return roles.get(role.lower(), "Vai trò không xác định")

def main():
    role = input("Nhập vai trò của nhân viên (manager, developer, designer, analyst, intern): ").strip()
    print(f"Vai trò của nhân viên là: {classify_employee(role)}")

if __name__ == "__main__":
    main()
# Bài 10: Viết hàm classify_student(age) để phân loại học sinh dựa trên tuổi.
def classify_student(age):
    """Phân loại học sinh dựa trên tuổi."""
    if 6 <= age <= 11:
        return "Học sinh tiểu học"
    elif 12 <= age <= 14:
        return "Học sinh trung học cơ sở"
    elif 15 <= age <= 17:
        return "Học sinh trung học phổ thông"
    elif age >= 18:
        return "Sinh viên đại học hoặc đã tốt nghiệp"
    else:
        return "Tuổi không hợp lệ"

def main():
    age = int(input("Nhập tuổi của học sinh: "))
    print(f"Học sinh thuộc loại: {classify_student(age)}")

if __name__ == "__main__":
    main()
# # 1. Viết một chương trình Python để tìm tất cả các số nguyên tố trong một dãy số cho trước,
# # sau đó sắp xếp dãy số tìm được theo chiều từ lớn đến bé và in ra dãy số đó
# # đây là dãy số cho trước[18, 9, 99, 23, 11, 4, 13, 97, 1, 3]
def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def thu_tu(numbers):
    primes = [num for num in numbers if la_so_nguyen_to(num)]
    primes.sort(reverse=True)
    return primes
numbers = [18, 9, 99, 23, 11, 4, 13, 97, 1, 3]
sorted_primes = thu_tu(numbers)
print("Dãy số nguyên tố theo thứ tự từ lớn đến bé:", sorted_primes)
# 2. Viết chương trình Python để thực hiện các yêu cầu sau:
#     - Tạo 2 danh sách chứa giá của các loại trái cây có trong một cửa hàng,
#         yêu cầu có nhiều hơn 5 loại trái cây[20000, 9000, 15000, 10500, ...]["chuối", "nho", "đủ đủ", "thanh long", ...]
#     - In ra bảng giá trái cây của cửa hàng này theo thứ tự giá tăng dần. nho: 9000 thanh long: 10500 đu đủ: 15000 .....
#     - Hỏi người dùng nhập một loại trái cây và số lượng muốn mua. Hãy nhập loại trái cây muốn mua: Hãy nhập số lượng trái cây muốn mua:
#         - Kiểm tra xem loại trái cây người dùng nhập có trong Danh Sách hay không.
#         + Nếu có, in ra thông báo Bạn đã mua[số lượng trái cây][tên trái cây] với số tiền: [tổng số tiền mua trái cây]
#         + Nếu không, in ra thông báo Loại trái cây[tên trái cây] không có trong cửa hàng!
def tao_bang_gia():
    """Tạo bảng giá trái cây."""
    gia_trai_cay = [20000, 9000, 15000, 10500, 12000, 18000]
    ten_trai_cay = ["chuối", "nho", "đu đủ", "thanh long", "dưa hấu", "táo"]
    return dict(zip(ten_trai_cay, gia_trai_cay))

def in_bang_gia(bang_gia):
    """In bảng giá trái cây theo thứ tự giá tăng dần."""
    sorted_items = sorted(bang_gia.items(), key=lambda x: x[1])
    print("Bảng giá trái cây của cửa hàng:")
    for ten, gia in sorted_items:
        print(f"{ten}: {gia}")

def mua_trai_cay(bang_gia):
    """Xử lý việc mua trái cây từ danh sách giá."""
    ten_trai_cay = input("Nhập loại trái cây muốn mua: ").strip()
    so_luong = int(input("Nhập số lượng trái cây muốn mua: ").strip())
    
    if ten_trai_cay in bang_gia:
        gia = bang_gia[ten_trai_cay]
        tong_tien = gia * so_luong
        print(f"Bạn đã mua {so_luong} {ten_trai_cay} với số tiền: {tong_tien}")
    else:
        print(f"Loại trái cây '{ten_trai_cay}' không có trong cửa hàng!")

def main():
    bang_gia = tao_bang_gia()
    in_bang_gia(bang_gia)
    mua_trai_cay(bang_gia)

if __name__ == "__main__":
    main()
