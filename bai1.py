import math

def snt(n):
    if n<2:
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

n=int(input("Nhap so nguyen n"))
if snt(n):
    print(f"{n} la snt")
else:
    print(f"{n} ko phai snt")
