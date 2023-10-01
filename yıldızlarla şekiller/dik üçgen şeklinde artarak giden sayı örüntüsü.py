# sayılarla şekiller
n = int(input("n:"))
x = 0
for satir in range(1,n+1):
    for sutun in range(1,satir+1):
        x += 1
        print(x,end=" ")
    print( )