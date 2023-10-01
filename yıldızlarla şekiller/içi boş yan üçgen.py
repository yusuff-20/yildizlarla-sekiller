# yıldızlarla şekiller
n = int(input("lütfen tablo ölçütünü giriniz:"))
for i in range(1,n):
    print((n-i)*" ","*",(n-i)*" ")
for i in range(n-1,0,-1):
    print((n-i)*" ","*",(n-i)*" ")