import random

# Các thuật toán sắp xếp
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Đọc dữ liệu từ file
def read_file(file_name):
    with open(file_name, 'r') as file:
        data = list(map(int, file.read().split()))
    return data

# Ghi kết quả vào file
def write_file(file_name, data):
    with open(file_name, 'w') as file:
        file.write("Bubble Sort: " + " ".join(map(str, data[0])) + "\n")
        file.write("Selection Sort: " + " ".join(map(str, data[1])) + "\n")
        file.write("Insertion Sort: " + " ".join(map(str, data[2])) + "\n")
        file.write("Quick Sort: " + " ".join(map(str, data[3])) + "\n")

# Xử lý thuật toán và lưu kết quả
def sort_and_save(input_file, output_file):
    data = read_file(input_file)
    
    # Lưu trữ kết quả của từng thuật toán
    results = []
    
    # Bubble Sort
    bubble_data = data.copy()
    bubble_sort(bubble_data)
    results.append(bubble_data)
    
    # Selection Sort
    selection_data = data.copy()
    selection_sort(selection_data)
    results.append(selection_data)
    
    # Insertion Sort
    insertion_data = data.copy()
    insertion_sort(insertion_data)
    results.append(insertion_data)
    
    # Quick Sort
    quick_data = data.copy()
    quick_sorted = quick_sort(quick_data)
    results.append(quick_sorted)
    
    # Ghi kết quả vào file
    write_file(output_file, results)

# Danh sách các file input và output
input_files = ['input1.txt', 'input2.txt', 'input3.txt', 'input4.txt']
output_files = ['output1.txt', 'output2.txt', 'output3.txt', 'output4.txt']

# Xử lý và ghi kết quả
for i in range(4):
    sort_and_save(input_files[i], output_files[i])

print("Đã hoàn thành việc sắp xếp và ghi kết quả vào các file output.")
