import random
import time

def taofile(ten_file, so_luong, max):
    with open(ten_file, 'w') as file:
        ds_so = [str(random.randint(0, max - 1)) for _ in range(so_luong)]
        file.write(" ".join(ds_so))  # Cú pháp thêm số vào ds chuỗi

# Tạo các file input
taofile("input1.txt", 10, 10)
taofile("input2.txt", 100, 100)
taofile("input3.txt", 500, 100)
taofile("input4.txt", 5000, 100)

def docfile(ten_file):
    with open(ten_file, 'r') as file:
        return list(map(int, file.read().split()))  # sửa từ 'spilt()' thành 'split()'

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def ghifile(ten_file):
    arr = docfile(ten_file)

    # Tạo 1 bản sao của arr
    arr_bubble = arr[:]

    start = time.time()  # Bước 1: Lưu thời gian bắt đầu
    bubble_sort(arr_bubble)  # Bước 2: Thực hiện sắp xếp với thuật toán Bubble Sort
    time_bubble = time.time() - start  # Bước 3: Tính toán thời gian đã trôi qua

    # Tạo tên file output từ tên file input
    ten_file_kq = ten_file.replace("input", "output")
    
    # Ghi kết quả vào file output
    with open(ten_file_kq, 'w') as file:
        file.write(f"Thuật toán BubbleSort ({time_bubble:.6f} giây): \n")
        file.write(' '.join(map(str, arr_bubble)) + "\n")  # Ghi kết quả vào file

    print(f"Đã xử lý xong {ten_file} và ghi vào {ten_file_kq}")

# Xử lý từng file input
for i in range(1, 5):
    ghifile(f"input{i}.txt")
