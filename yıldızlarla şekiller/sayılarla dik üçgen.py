# sayılarla şekiller
n = int(input("n:"))

for satir in range(1,n+1):
    x = 0
    for sutun in range(1,satir+1):
        x += 1
        print(x,end=" ")
    print()