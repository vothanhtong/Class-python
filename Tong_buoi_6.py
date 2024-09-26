# Bài Tập 1: Tính Căn Bậc Hai
# Sử dụng module math, viết một chương trình yêu cầu người dùng nhập một số và in ra căn bậc hai của số đó.
import my_math
a=int(input("nhập vào một số a để tính căn bậc hai: "))
print("căn bậc hai của số trên là: ",my_math.sqrt(a))
# Bài Tập 2: Tính Diện Tích Hình Tròn
# Sử dụng module math, viết một chương trình yêu cầu người dùng nhập bán kính của hình tròn và tính diện tích của hình tròn đó.
a=int(input("nhập vào chiều dài hình tròn: "))
print("diện tích hình tròn là: ",my_math.pi)
# Bài Tập 3: Sinh Số Ngẫu Nhiên
# Sử dụng module random, viết một chương trình in ra một số nguyên ngẫu nhiên từ 1 đến 100.
import random
a = random.randint(1, 100)
print("số ngẫu nhiên từ một đến 100 là: ",a)
# Bài Tập 4: Chọn Ngẫu Nhiên Từ Danh Sách
# Sử dụng module random, viết một chương trình chứa một danh sách các tên và in ra một tên ngẫu nhiên từ danh sách đó.
import random
a = ["cầu", "dừa", "đủ", "sài", "sung"]
in_ra = random.choice(a)
print("in ra danh sách bất kỳ: ", in_ra)
# Bài Tập 5: Tính Ngày Hôm Sau
# Sử dụng module datetime, viết một chương trình in ra ngày hôm sau của ngày hiện tại.
import datetime
today= datetime.date.today()
print(today)
# Bài Tập 6: Tính Tuổi
# Sử dụng module datetime, viết một chương trình yêu cầu người dùng nhập ngày sinh của họ và tính tuổi của họ.
from datetime import datetime
ngay_sinh = input("Nhập ngày sinh của bạn (định dạng: ngày-tháng-năm): ")
ngay_sinh = datetime.strptime(ngay_sinh, "%Y-%m-%d")
ngay_hien_tai = datetime.today()
tuoi = ngay_hien_tai.year - ngay_sinh.year
if (ngay_hien_tai.month, ngay_hien_tai.day) < (ngay_sinh.month, ngay_sinh.day):
    tuoi -= 1
print("Tuổi của bạn là:", tuoi)
# Bài Tập 7: Đếm Ngược Thời Gian
# Sử dụng module datetime, viết một chương trình đếm ngược từ 10 giây xuống 0 và in ra “Time’s up!” khi hết giờ.
import time
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
print("Time's up!")
# Bài Tập 8: In Các Đối Số Dòng Lệnh
# Sử dụng module sys, viết một chương trình in ra tất cả các đối số dòng lệnh đã nhập vào khi chạy chương trình.
import sys
print("Các đối số dòng lệnh đã nhập vào là:")
for i, arg in enumerate(sys.argv):
    print(f"Đối số {i}: {arg}")
# Bài Tập 9: Kiểm Tra Phiên Bản Python
# Sử dụng module sys, viết một chương trình in ra phiên bản Python hiện tại đang được sử dụng.
import sys
print("Phiên bản Python hiện tại là:")
print(sys.version)
# Bài Tập 10: Kiểm Tra Đường Dẫn Python
# Sử dụng module sys, viết một chương trình in ra đường dẫn của trình thông dịch Python đang được sử dụng."
import sys
print("Đường dẫn của trình thông dịch Python là:")
print(sys.executable)
# ** ================================================= **
# BÀI TẬP ÁP DỤNG THỰC TẾ
# ** ================================================= **
# BÀI TẬP ÁP DỤNG THỰC TẾ
# Bài Tập 1: Ứng Dụng Máy Tính Cá Nhân: Viết một chương trình giả lập máy tính cá nhân. 
# Cho phép người dùng thực hiện các phép tính cơ bản như cộng, trừ, nhân, chia.
def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b != 0:
        return a / b
    else:
        return "Lỗi: Không thể chia cho 0"
print("Chào mừng đến với ứng dụng Máy Tính Cá Nhân!")
print("Vui lòng chọn phép tính:")
print("1. Cộng")
print("2. Trừ")
print("3. Nhân")
print("4. Chia")
lua_chon = input("Nhập lựa chọn (1/2/3/4): ")
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))
if lua_chon == '1':
    print(f"Kết quả: {so1} + {so2} = {cong(so1, so2)}")
elif lua_chon == '2':
    print(f"Kết quả: {so1} - {so2} = {tru(so1, so2)}")
elif lua_chon == '3':
    print(f"Kết quả: {so1} * {so2} = {nhan(so1, so2)}")
elif lua_chon == '4':
    ket_qua = chia(so1, so2)
    print(f"Kết quả: {so1} / {so2} = {ket_qua}")
else:
    print("Lựa chọn không hợp lệ!")
# Bài Tập 2: Quản Lý Danh Bạ Điện Thoại: Viết chương trình quản lý danh bạ điện thoại, 
# cho phép người dùng thêm, sửa, xóa và xem danh sách các số liên lạc.
# Khởi tạo danh bạ điện thoại rỗng
danh_ba = {}       
def hien_thi_menu():
    print("\n--- Quản lý danh bạ điện thoại ---")
    print("1. Thêm số liên lạc")
    print("2. Sửa số liên lạc")
    print("3. Xóa số liên lạc")
    print("4. Xem danh sách số liên lạc")
    print("5. Thoát")

def them_lien_lac():
    ten = input("Nhập tên liên lạc: ")
    so_dien_thoai = input("Nhập số điện thoại: ")
    danh_ba[ten] = so_dien_thoai
    print(f"Đã thêm liên lạc {ten} với số điện thoại {so_dien_thoai}.")

def sua_lien_lac():
    ten = input("Nhập tên liên lạc cần sửa: ")
    if ten in danh_ba:
        so_dien_thoai = input("Nhập số điện thoại mới: ")
        danh_ba[ten] = so_dien_thoai
        print(f"Đã cập nhật số điện thoại của {ten} thành {so_dien_thoai}.")
    else:
        print("Liên lạc không tồn tại!")

def xoa_lien_lac():
    ten = input("Nhập tên liên lạc cần xóa: ")
    if ten in danh_ba:
        del danh_ba[ten]
        print(f"Đã xóa liên lạc {ten}.")
    else:
        print("Liên lạc không tồn tại!")

def xem_danh_sach():
    if danh_ba:
        print("\nDanh sách số liên lạc:")
        for ten, so_dien_thoai in danh_ba.items():
            print(f"Tên: {ten}, Số điện thoại: {so_dien_thoai}")
    else:
        print("Danh bạ hiện tại rỗng!")

def main():
    while True:
        hien_thi_menu()
        lua_chon = input("Chọn một tùy chọn (1/2/3/4/5): ")
        
        if lua_chon == '1':
            them_lien_lac()
        elif lua_chon == '2':
            sua_lien_lac()
        elif lua_chon == '3':
            xoa_lien_lac()
        elif lua_chon == '4':
            xem_danh_sach()
        elif lua_chon == '5':
            print("Thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
# Bài Tập 3: Ứng Dụng Chuyển Đổi Tiền Tệ: Viết chương trình chuyển đổi giữa các loại tiền tệ khác nhau 
# (ví dụ: USD sang VND). Tỷ giá hối đoái có thể được cung cấp sẵn.
    def chuyen_doi_tien(te_tien, so_tien, ti_gia):
     return so_tien * ti_gia

def hien_thi_menu():
    print("\n--- Ứng dụng chuyển đổi tiền tệ ---")
    print("1. USD sang VND")
    print("2. VND sang USD")
    print("3. Thoát")

def chuyen_doi_usd_sang_vnd():
    ti_gia_usd_to_vnd = 23500  # Ví dụ tỷ giá USD sang VND
    so_usd = float(input("Nhập số tiền USD: "))
    so_vnd = chuyen_doi_tien("USD", so_usd, ti_gia_usd_to_vnd)
    print(f"{so_usd} USD = {so_vnd:.2f} VND")

def chuyen_doi_vnd_sang_usd():
    ti_gia_vnd_to_usd = 1 / 23500  # Tỷ giá ngược lại từ VND sang USD
    so_vnd = float(input("Nhập số tiền VND: "))
    so_usd = chuyen_doi_tien("VND", so_vnd, ti_gia_vnd_to_usd)
    print(f"{so_vnd} VND = {so_usd:.2f} USD")

def main():
    while True:
        hien_thi_menu()
        lua_chon = input("Chọn một tùy chọn (1/2/3): ")
        
        if lua_chon == '1':
            chuyen_doi_usd_sang_vnd()
        elif lua_chon == '2':
            chuyen_doi_vnd_sang_usd()
        elif lua_chon == '3':
            print("Thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")
if __name__ == "__main__":
    main()
# Bài Tập 4: Ứng Dụng Kiểm Tra Mật Khẩu Mạnh: Viết chương trình kiểm tra độ mạnh của mật khẩu. 
# Mật khẩu phải có ít nhất 8 ký tự, chứa cả chữ hoa, chữ thường và số.
import re
def kiem_tra_mat_khau(mat_khau):
    # Kiểm tra độ dài
    if len(mat_khau) < 8:
        return 
    # Kiểm tra có ít nhất một chữ cái hoa
    if not re.search(r'[A-Z]', mat_khau):
        return 
    # Kiểm tra có ít nhất một chữ cái thường
    if not re.search(r'[a-z]', mat_khau):
        return
# Bài Tập 5: Ứng Dụng Quản Lý Chi Tiêu Cá Nhân: Viết chương trình giúp người dùng theo dõi và quản lý 
# các khoản chi tiêu cá nhân. Cho phép người dùng nhập khoản chi tiêu và tổng kết số tiền đã chi trong tháng.
def them_khoan_chi(chi_tieu):
    """Thêm một khoản chi tiêu vào danh sách."""
    ten = input("Nhập mô tả khoản chi: ")
    so_tien = float(input("Nhập số tiền chi: "))
    chi_tieu.append({'mo_ta': ten, 'so_tien': so_tien})
    print(f"Đã thêm khoản chi: {ten} với số tiền {so_tien:.2f}.")

def tong_khoan_chi(chi_tieu):
    """Tính tổng số tiền đã chi trong tháng."""
    tong = sum(khoan['so_tien'] for khoan in chi_tieu)
    return tong

def xem_danh_sach(chi_tieu):
    """Hiển thị danh sách các khoản chi tiêu."""
    if chi_tieu:
        print("\nDanh sách các khoản chi tiêu:")
        for khoan in chi_tieu:
            print(f"Mô tả: {khoan['mo_ta']}, Số tiền: {khoan['so_tien']:.2f}")
    else:
        print("Danh sách chi tiêu hiện tại rỗng!")

def main():
    chi_tieu = []
    while True:
        print("\n--- Quản lý chi tiêu cá nhân ---")
        print("1. Thêm khoản chi tiêu")
        print("2. Tổng kết số tiền đã chi")
        print("3. Xem danh sách chi tiêu")
        print("4. Thoát")
        
        lua_chon = input("Chọn một tùy chọn (1/2/3/4): ")
        
        if lua_chon == '1':
            them_khoan_chi(chi_tieu)
        elif lua_chon == '2':
            tong = tong_khoan_chi(chi_tieu)
            print(f"Tổng số tiền đã chi trong tháng là: {tong:.2f}")
        elif lua_chon == '3':
            xem_danh_sach(chi_tieu)
        elif lua_chon == '4':
            print("Thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
# Bài Tập 6: Tạo Lịch Nhắc Nhở Công Việc: Viết chương trình cho phép người dùng tạo danh sách các công việc 
# cần làm và nhận thông báo khi đến thời gian đã định.
import datetime
import time
def them_cong_viec(cong_viec):
    """Thêm công việc vào danh sách."""
    mo_ta = input("Nhập mô tả công việc: ")
    thoi_gian_str = input("Nhập thời gian nhắc nhở (định dạng YYYY-MM-DD HH:MM): ")
    thoi_gian = datetime.datetime.strptime(thoi_gian_str, "%Y-%m-%d %H:%M")
    cong_viec.append({'mo_ta': mo_ta, 'thoi_gian': thoi_gian})
    print(f"Đã thêm công việc '{mo_ta}' với thời gian nhắc nhở {thoi_gian}.")

def xem_danh_sach(cong_viec):
    """Hiển thị danh sách các công việc cần làm."""
    if cong_viec:
        print("\nDanh sách công việc cần làm:")
        for cv in cong_viec:
            print(f"Mô tả: {cv['mo_ta']}, Thời gian nhắc nhở: {cv['thoi_gian']}")
    else:
        print("Danh sách công việc hiện tại rỗng!")

def thong_bao(cong_viec):
    """Kiểm tra và thông báo công việc khi đến thời gian đã định."""
    while True:
        now = datetime.datetime.now()
        for cv in cong_viec:
            if cv['thoi_gian'] <= now:
                print(f"THÔNG BÁO: Đến thời gian thực hiện công việc '{cv['mo_ta']}'!")
                cong_viec.remove(cv)  
        time.sleep(60) 

def main():
    cong_viec = [] 
    while True:
        print("\n--- Lịch nhắc nhở công việc ---")
        print("1. Thêm công việc")
        print("2. Xem danh sách công việc")
        print("3. Bắt đầu kiểm tra nhắc nhở")
        print("4. Thoát")
        
        lua_chon = input("Chọn một tùy chọn (1/2/3/4): ")
        
        if lua_chon == '1':
            them_cong_viec(cong_viec)
        elif lua_chon == '2':
            xem_danh_sach(cong_viec)
        elif lua_chon == '3':
            print("Bắt đầu kiểm tra nhắc nhở...")
            thong_bao(cong_viec)
        elif lua_chon == '4':
            print("Thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
# Bài Tập 7: Trò Chơi Đoán Số: Viết chương trình trò chơi đoán số. Máy tính sẽ chọn một số ngẫu nhiên 
# và người dùng sẽ đoán số đó. Nếu đoán đúng, chương trình sẽ thông báo chiến thắng.
import random
def choi_doan_so():
    so_ngau_nhien = random.randint(1, 100) 
    so_lan_doan = 0

    print("Chào mừng bạn đến với trò chơi đoán số!")
    print("Tôi đã chọn một số ngẫu nhiên từ 1 đến 100. Hãy cố gắng đoán số đó!")

    while True:
        try:
            doan = int(input("Nhập số bạn đoán: "))
            so_lan_doan += 1

            if doan < so_ngau_nhien:
                print("Số bạn đoán quá thấp. Thử lại!")
            elif doan > so_ngau_nhien:
                print("Số bạn đoán quá cao. Thử lại!")
            else:
                print(f"Chúc mừng! Bạn đã đoán đúng số {so_ngau_nhien} sau {so_lan_doan} lần đoán.")
                break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

def main():
    choi_doan_so()
    while True:
        lua_chon = input("Bạn có muốn chơi lại không? (có/không): ").strip().lower()
        if lua_chon == 'có':
            choi_doan_so()
        elif lua_chon == 'không':
            print("Cảm ơn bạn đã chơi!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
# Bài Tập 8: Ứng Dụng Đếm Số Từ Trong Văn Bản: Viết chương trình cho phép người dùng nhập một đoạn văn bản 
# và đếm số lượng từ trong đó.
def dem_so_tu(van_ban):
    """Đếm số lượng từ trong văn bản."""
    danh_sach_tu = van_ban.split()
    so_tu = len(danh_sach_tu)
    return so_tu

def main():
    van_ban = input("Nhập đoạn văn bản để đếm số từ: ")
    so_tu = dem_so_tu(van_ban)
    print(f"Số lượng từ trong đoạn văn bản là: {so_tu}")

if __name__ == "__main__":
    main()
# Bài Tập 9: Ứng Dụng Tạo Mã OTP: Viết chương trình tạo mã OTP (One-Time Password) gồm 6 chữ số ngẫu nhiên 
# và hiển thị nó cho người dùng.
import random
def tao_ma_otp():
    otp = random.randint(100000, 999999)  
    return otp

def main():
    otp = tao_ma_otp()
    print(f"Mã OTP của bạn là: {otp}")

if __name__ == "__main__":
    main()
# Bài Tập 10: Tính Lãi Suất Ngân Hàng: Viết chương trình tính lãi suất ngân hàng dựa trên số tiền gốc, 
# lãi suất hàng năm và số năm gửi.
def tinh_lai_suat_don(so_tien_goc, lai_suat_hang_nam, so_nam_gui):
    lai_suat = so_tien_goc * lai_suat_hang_nam * so_nam_gui
    tong_tien = so_tien_goc + lai_suat
    return tong_tien

def main():
    so_tien_goc = float(input("Nhập số tiền gốc: "))
    lai_suat_hang_nam = float(input("Nhập lãi suất hàng năm (dưới dạng phần trăm, ví dụ: 5 cho 5%): ")) / 100
    so_nam_gui = float(input("Nhập số năm gửi: "))
    
    tong_tien = tinh_lai_suat_don(so_tien_goc, lai_suat_hang_nam, so_nam_gui)
    print(f"Số tiền cuối cùng sau {so_nam_gui} năm là: {tong_tien:.2f}")

if __name__ == "__main__":
    main()
def tinh_lai_suat_kep(so_tien_goc, lai_suat_hang_nam, so_nam_gui, so_lan_tinh_lai_moi_nam=1):
    lai_suat_hang_nam /= 100  
    tong_tien = so_tien_goc * (1 + lai_suat_hang_nam / so_lan_tinh_lai_moi_nam) ** (so_lan_tinh_lai_moi_nam * so_nam_gui)
    return tong_tien

def main():
    so_tien_goc = float(input("Nhập số tiền gốc: "))
    lai_suat_hang_nam = float(input("Nhập lãi suất hàng năm (dưới dạng phần trăm, ví dụ: 5 cho 5%): "))
    so_nam_gui = float(input("Nhập số năm gửi: "))
    
    tong_tien = tinh_lai_suat_kep(so_tien_goc, lai_suat_hang_nam, so_nam_gui)
    print(f"Số tiền cuối cùng sau {so_nam_gui} năm là: {tong_tien:.2f}")

if __name__ == "__main__":
    main()