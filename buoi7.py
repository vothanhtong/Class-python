##### QUẢN LÝ THỜI KHOÁ BIỂU #####
schedule = {}

def main_menu():
    print("\nChọn một tùy chọn:")
    print("1. Thêm sự kiện")
    print("2. Xem thời khoá biểu")
    print("3. Chỉnh sửa sự kiện")
    print("4. Thoát")
    return int(input("Nhập số tương ứng với lựa chọn của bạn: "))

# Hàm kiểm tra đầu vào
def validate_input(value, name):
    if not value.isdigit():
        print(f"Đầu vào không hợp lệ cho {name}. Vui lòng nhập một số.")
        return False
    return True

# Thêm sự kiện
def add_event():
    while True:
        month = input("Nhập tháng (dưới dạng số): ")
        if validate_input(month, "tháng") and 1 <= int(month) <= 12:
            break

    while True:
        week = input("Nhập tuần (dưới dạng số): ")
        if validate_input(week, "tuần") and 1 <= int(week) <= 5:
            break

    while True:
        day = input("Nhập ngày (dưới dạng số): ")
        if validate_input(day, "ngày") and 1 <= int(day) <= 7:
            break

    while True:
        start_time = input("Nhập thời gian bắt đầu (vd: 5h00 hoặc 17h00): ")
        if "h" in start_time and len(start_time) >= 4:
            break
        else:
            print("Thời gian không hợp lệ, vui lòng nhập lại.")

    while True:
        end_time = input("Nhập thời gian kết thúc (vd: 5h00 hoặc 17h00): ")
        if "h" in end_time and len(end_time) >= 4:
            break
        else:
            print("Thời gian không hợp lệ, vui lòng nhập lại.")
    
    event_name = input("Nhập tên sự kiện: ")
    event_details = input("Nhập chi tiết sự kiện: ")
    important = input("Sự kiện này có quan trọng không? (có/không): ") .lower()

    if important == "có":
        important = True
    else:
        important = False

    important = input("Bạn có muốn thêm sự kiện khác không? (nhập 'end' để thoát): ").strip().lower()
    if important == 'end':
        important = True
    else:
        important = False    
    # Tạo một khóa cho ngày cụ thể
    key = (month, week, day)
    
    if key not in schedule:
        schedule[key] = []
    
    schedule[key].append({
        "Tên sự kiện": event_name,
        "Chi tiết": event_details,
        "Thời gian bắt đầu": start_time,
        "Thời gian kết thúc": end_time,
        "Quan trọng": important
    })

    print(f"Sự kiện '{event_name}' đã được thêm vào Tháng {month}, Tuần {week}, Ngày {day}.")
    
# Xem thời khoá biểu
def view_schedule():
    if not schedule:
        print("Không có sự kiện nào được lên lịch.")
    else:
        for key, events in schedule.items():
            month, week, day = key
            print(f"\nTháng: {month}, Tuần: {week}, Ngày: {day}")
            for i, event in enumerate(events, start=1):
                print(f"  {i}. {event['Tên sự kiện']} (Quan trọng: {'Có' if event['Quan trọng'] else 'Không'})")
                print(f"      Chi tiết: {event['Chi tiết']}")
                print(f"      Thời gian: {event['Thời gian bắt đầu']} - {event['Thời gian kết thúc']}")

# Chỉnh sửa sự kiện
def edit_event():
    while True:
        month = input("Nhập tháng (dưới dạng số): ")
        if validate_input(month, "tháng") and 1 <= int(month) <= 12:
            break

    while True:
        week = input("Nhập tuần (dưới dạng số): ")
        if validate_input(week, "tuần") and 1 <= int(week) <= 5:
            break

    while True:
        day = input("Nhập ngày (dưới dạng số): ")
        if validate_input(day, "ngày") and 1 <= int(day) <= 7:
            break
    
    key = (month, week, day)
    
    if key not in schedule or not schedule[key]:
        print(f"Không tìm thấy công việc nào cho Tháng {month}, Tuần {week}, Ngày {day}.")
        return
    
    while True:
        print(f"\nChỉnh sửa thời khoá biểu cho Tháng {month}, Tuần {week}, Ngày {day}:")
        print("1. Thêm sự kiện")
        print("2. Chỉnh sửa sự kiện")
        print("3. Xóa sự kiện")
        print("4. Quay lại menu chính")
        choice = int(input("Nhập lựa chọn của bạn: "))
        
        if choice == 1:
            add_event()
        elif choice == 2:
            view_tasks(key)
            task_index = int(input("Nhập số của sự kiện bạn muốn chỉnh sửa: ")) - 1
            if 0 <= task_index < len(schedule[key]):
                new_task = input("Nhập tên sự kiện mới: ")
                schedule[key][task_index]['Tên sự kiện'] = new_task
                print(f"Tên sự kiện đã được cập nhật thành '{new_task}'.")
            else:
                print("Số sự kiện không hợp lệ.")
        elif choice == 3:
            view_tasks(key)
            task_index = int(input("Nhập số của sự kiện cần xóa: ")) - 1
            if 0 <= task_index < len(schedule[key]):
                deleted_task = schedule[key].pop(task_index)
                print(f"Sự kiện '{deleted_task['Tên sự kiện']}' đã bị xóa.")
                if not schedule[key]:  
                    del schedule[key]
            else:
                print("Số sự kiện không hợp lệ.")
        elif choice == 4:
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

# Xem sự kiện
def view_tasks(key):
    month, week, day = key
    print(f"Sự kiện cho Tháng: {month}, Tuần: {week}, Ngày: {day}:")
    for i, event in enumerate(schedule[key], start=1):
        print(f"  {i}. {event['Tên sự kiện']} (Quan trọng: {'Có' if event['Quan trọng'] else 'Không'})")
        print(f"      Chi tiết: {event['Chi tiết']}")
        print(f"      Thời gian: {event['Thời gian bắt đầu']} - {event['Thời gian kết thúc']}")

# Chạy chương trình
def run():
    while True:
        choice = main_menu()
        if choice == 1:
            add_event()
        elif choice == 2:
            view_schedule()
        elif choice == 3:
            edit_event()
        elif choice == 4:
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
            
if __name__ == "__main__":
    run()
