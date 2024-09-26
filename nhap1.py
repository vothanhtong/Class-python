import time

def stopwatch():
    print("Nhấn 'Enter' để bắt đầu đồng hồ bấm giờ")
    print("Nhấn 'Ctrl + C' để dừng đồng hồ bấm giờ")
    
    input()  # Bắt đầu khi nhấn Enter
    start_time = time.time()  # Lưu thời điểm bắt đầu
    print("Đồng hồ đang chạy...")
    
    try:
        while True:
            elapsed_time = time.time() - start_time  # Tính thời gian đã trôi qua
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            # Hiển thị thời gian ở định dạng HH:MM:SS
            print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nĐồng hồ bấm giờ đã dừng lại.")

stopwatch()

