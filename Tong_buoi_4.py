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

    task = input("Nhập công việc cần thêm: ")

    # Tạo một khóa cho ngày cụ thể
    key = (month, week, day)
    
    if key not in schedule:
        schedule[key] = []
    schedule[key].append(task)
    
    print(f"Công việc '{task}' đã được thêm vào Tháng {month}, Tuần {week}, Ngày {day}.")

# Xem thời khoá biểu
def view_schedule():
    if not schedule:
        print("Không có sự kiện nào được lên lịch.")
    else:
        for key, tasks in schedule.items():
            month, week, day = key
            print(f"\nTháng: {month}, Tuần: {week}, Ngày: {day}")
            for i, task in enumerate(tasks, start=1):
                print(f"  {i}. {task}")

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
        print("1. Thêm công việc")
        print("2. Chỉnh sửa công việc")
        print("3. Xóa công việc")
        print("4. Quay lại menu chính")
        choice = int(input("Nhập lựa chọn của bạn: "))
        
        if choice == 1:
            task = input("Nhập công việc cần thêm: ")
            schedule[key].append(task)
            print(f"Công việc '{task}' đã được thêm vào Tháng {month}, Tuần {week}, Ngày {day}.")
        elif choice == 2:
            view_tasks(key)
            task_index = int(input("Nhập số của công việc bạn muốn chỉnh sửa: ")) - 1
            if 0 <= task_index < len(schedule[key]):
                new_task = input("Nhập công việc mới: ")
                schedule[key][task_index] = new_task
                print(f"Công việc đã được cập nhật thành '{new_task}'.")
            else:
                print("Số công việc không hợp lệ.")
        elif choice == 3:
            view_tasks(key)
            task_index = int(input("Nhập số của công việc cần xóa: ")) - 1
            if 0 <= task_index < len(schedule[key]):
                deleted_task = schedule[key].pop(task_index)
                print(f"Công việc '{deleted_task}' đã bị xóa.")
                if not schedule[key]:  # Xóa khóa nếu không còn công việc
                    del schedule[key]
            else:
                print("Số công việc không hợp lệ.")
        elif choice == 4:
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

# Xem công việc
def view_tasks(key):
    month, week, day = key
    print(f"Công việc cho Tháng: {month}, Tuần: {week}, Ngày: {day}:")
    for i, task in enumerate(schedule[key], start=1):
        print(f"  {i}. {task}")

# Chạy chương trình
def run_program():
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
    run_program()
