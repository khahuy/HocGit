import time


def docfile(ten_file):
    with open(ten_file, 'r') as file:
        return list(map(int, file.read().split()))  # sửa từ 'spilt()' thành 'split()'

# Thuật toán Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Thuật toán Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Thuật toán Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Thuật toán Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def ghifile(ten_file):
    arr = docfile(ten_file)

    # Tạo tên file output từ tên file input
    #ten_file_kq = ten_file.replace("input", "output")
    ten_file_kq = f"output{ten_file[5]}"

    # Tạo 1 bản sao của arr
    arr_bubble = arr[:]
    arr_selection=arr[:]
    arr_quick=arr[:]
    arr_insertion=arr[:]

    start = time.time()  # Bước 1: Lưu thời gian bắt đầu
    bubble_sort(arr_bubble)  # Bước 2: Thực hiện sắp xếp với thuật toán Bubble Sort
    time_bubble = time.time() - start  # Bước 3: Tính toán thời gian đã trôi qua

    start=time.time()
    selection_sort(arr_selection)
    time_selection=time.time() - start

    start=time.time()
    insertion_sort(arr_insertion)
    time_insertion=time.time() - start

    stat=time.time()
    quick_sort(arr_quick)
    time_quick=time.time() - start
    
    with open(ten_file_kq.replace(".txt", "_output.txt"), 'w', encoding='utf-8') as file:
        file.write(f"Bubble Sort: {' '.join(map(str, arr_bubble))}\n")
        file.write(f"Selection Sort: {' '.join(map(str, arr_selection))}\n")
        file.write(f"Insertion Sort: {' '.join(map(str, arr_insertion))}\n")
        file.write(f"Quick Sort: {' '.join(map(str, arr_quick))}\n")

    print(f"Đã xử lý xong {ten_file} và ghi vào {ten_file_kq.replace('.txt', '_output.txt')}")

# Xử lý từng file input
for i in range(1, 5):
    ghifile(f"input{i}.txt")
