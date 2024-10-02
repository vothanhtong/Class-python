# # Tạo một mảng hai chiều (ma trận 3x3)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Hiển thị ma trận
# for row in matrix:
#     print(row)

# # Tính tổng các phần tử trong ma trận
# total_sum = 0
# for row in matrix:
#     for element in row:
#         total_sum += element

# print("Tổng các phần tử trong ma trận là:", total_sum)

#                       Khởi tạo ma trận 3x3 rỗng
matrix = []

# Nhập giá trị cho từng phần tử của ma trận
for i in range(3):
    row = []  # Tạo hàng mới
    for j in range(3):
        value = int(input(f"Nhập giá trị cho phần tử [{i}][{j}]: "))
        row.append(value)  # Thêm giá trị vào hàng
    matrix.append(row)  # Thêm hàng vào ma trận

# In ma trận
print("Ma trận vừa nhập:")
for row in matrix:
    print(row)

# Tính tổng các phần tử
total = 0
for row in matrix:
    total += sum(row)

print(f"Tổng các phần tử trong ma trận: {total}")
