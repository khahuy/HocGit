def bubble_sort(arr):
    n = len(arr)
    a = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def selection_sort(arr):
    n = len(arr)
    a = arr.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def doc_va_sap_xep(ten_file, thuat_toan):
    """
    Đọc file input, sắp xếp và in kết quả.

    Args:
        ten_file (str): Tên file input.
        thuat_toan (function): Hàm sắp xếp.
    """
    with open(ten_file, 'r') as f:
        data = f.read().strip().split()
        arr = [int(x) for x in data]

    arr_sorted = thuat_toan(arr)
    print(f"Kết quả sắp xếp {ten_file} bằng {thuat_toan.__name__}:")
    print("10 phần tử đầu tiên sau sắp xếp:", arr_sorted[:10])
    print("-" * 30)

# Đọc và sắp xếp các file input bằng 4 thuật toán
ds_thuat_toan = [bubble_sort, selection_sort, insertion_sort, quick_sort]

for ten_file in ['input1.txt', 'input2.txt', 'input3.txt', 'input4.txt']:
    for thuat_toan in ds_thuat_toan:
        doc_va_sap_xep(ten_file, thuat_toan)
