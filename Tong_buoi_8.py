du_lieu_trong= [ ]

def hien_thi_menu():
    print("1.thêm sụ kiện mới: ")
    print("2.in ra màng hình: ")
    print("3.sửa sự kiện: ")
    print("4.thoát")

def them_su_kien_moi ():
    while True :
        su_kien = {}
        su_kien ["tháng"] = input ("nhập tháng: ")
        su_kien ["tuần"] = input ("nhập tuần: ")
        su_kien ["ngày"] = input ("nhập ngày: ")
        su_kien ["bắt đầu"] = input ("nhập thời gian bắt đầu: ")
        su_kien ["kết thúc"] = input ("nhập thời gian kết thúc: ")
        su_kien ["tên sụ kiện"] = input ("nhập tên sự kiện: ")
        su_kien ["chi tiết sự kiện"] = input ("nhập chi tiết sự kiện: ")
        su_kien ["quan trọng"] = input ("sự kiện có quan trọng hay không: ")
        # kiểm tra hàm: 
        kiem_tra = None
        for event in du_lieu_trong:
            if (event ["tháng "] == su_kien ["tháng"] and 
                event ["tuần"] == su_kien ["tuần"] and
                event ["ngày"] == su_kien ["ngày"] and
                event ["tên sự kiện"] == su_kien ["tên sự kiện"] ):
                kiem_tra =event
                break
        if kiem_tra :
            print(f"sự kiện'{su_kien['tên sựu kiện']}'đã tồn tại vào ngày này" )
            lua_chon = input ("bạn có muốn hợp nhất lại không?  (có/không) ") .strip() .lower()
            if lua_chon == "có" :
                kiem_tra["chi tiết sự kiện "] += " | " + su_kien["chi tiết sự kiện"]
                kiem_tra["thời gian bắt đầu"] = min(kiem_tra["thời gian bắt đầu"],su_kien["thời gian bắt đấu"])
                kiem_tra["thời gian kết thúc"]= max(kiem_tra ["thời gian kết thúc"], su_kien["thời gian kết thúc"])
                kiem_tra["có quan trọng không"] = "có" if "có" in (kiem_tra["quan trọng"],su_kien["quan trọng"]) else "không"
                print ("sự kiện đã được hợp nhất")
            else:
                print ("sự kiện không được thêm")
        else:
            du_lieu_trong.append (su_kien)
            print (f"/n sự kiện '{su_kien['tên sự kiện']}' đã được thêm vào lịch trình.\n")

            tiep_tuc = input ("bạn có muốn thêm sự kiện khác không?(nhập 'end' để thoát):") .strip() .lower() 
            if tiep_tuc == 'end':
               break

def xem_lich_trinh():
    if not du_lieu_trong:
        print("không có sự kiện nào thêm lịch")
    else:
        for i, su_kien  in enumerate(du_lieu_trong,start=1):
         print(f"--- Sự kiện {i} ---")
         print(f"Tháng: {su_kien['Tháng']}")
         print(f"Tuần: {su_kien['Tuần']}")
         print(f"Ngày: {su_kien['Ngày']}")
         print(f"Thời gian bắt đầu: {su_kien['Thời gian bắt đầu']}")
         print(f"Thời gian kết thúc: {su_kien['Thời gian kết thúc']}")
         print(f"Tên sự kiện: {su_kien['Tên sự kiện']}")
         print(f"Chi tiết sự kiện: {su_kien['Chi tiết sự kiện']}")
         print(f"Quan trọng: {su_kien['Quan trọng']}")
         print()

def sua_su_kien():
    if not du_lieu_trong:
        print("không có sự kiện nào để sửa")
        return
    thang = input ("nhập vào tháng cần sửa .")
    tuan = input ("nhập vào tuần cần sửa. ")
    ngay = input ("nhập vào tuần cần sửa. ")
    found_events = [event for event in du_lieu_trong if event['tháng']==thang and event['tuần']==tuan and event['ngày']==ngay]
    if not found_events:
        print("không tìm thấy sự kiện nào vào ngày này")
        return
    print("\n các sự kiện trong ngày đã chọn. " )
    for i , event in enumerate(found_events,start=1):
        print(f"{i} .{event["tên sụ kiện"]}")
    
    try:
        index = int(input("chọn số sụ kiện bạn muốn sửa"))
        event= found_events[index]
    except(ValueError,IndexError):
        print("lựa chọn không hợp lệ")
        return
    print("chọn tuỳ chọn")
    print("1. thêm công việc")
    print("2. chỉnh sửa công việc")
    print("3. soá công việc")
    lua_chon = input ("chọn tuỳ chọn 1/2/3 ")
    if lua_chon == "1":
        event["chi tiết sự kiện"] += " | " + input ("nhập chi tiết sự kiện mới:")
        print("công việc được thêm :")
    elif lua_chon =="2":
        event["thời gian bắt đầu"] = input("nhập thời gian bắt đầu mới:")
        event["thời gian kết thúc"] = input("nhập thời gian kết thúc mới")
        event["chi tiết sự kiện"] = input("nhập chi tiết sự kiện mới:")
        event["quan trọng"] = input("sự kiện có quan trọng hay không? (có/không):")
        print("sự kiệm đã được chỉnh sửa: ")
    elif lua_chon == "3":
        du_lieu_trong.remove(event)
        print("sự kiện đã được soá:")
    else:
        print("tuỳ chọn không hợp lệ: ")

while True:
    hien_thi_menu()
    lua_chon=input("chọn một tuỳ chọn:(1/2/3/4) ")
    if lua_chon=="1":
        them_su_kien_moi()
    elif lua_chon =="2":
        xem_lich_trinh()
    elif lua_chon =="3":
        sua_su_kien()
    elif lua_chon =="4":
        break
    else:
        print("không hợp lệ vui lòng chọn lại :")
