import random

def taofile(ten_file, so_luong, gioi_han):
    with open(ten_file, 'w') as f:
        for _ in range(so_luong):
            f.write(str(random.randint(0, gioi_han - 1)) + " ")

taofile('input1.txt', 10, 10)
taofile('input2.txt', 100, 100)
taofile('input3.txt', 500, 100)
taofile('input4.txt', 5000, 100)

print("Đã tạo thành công 4 file input.")