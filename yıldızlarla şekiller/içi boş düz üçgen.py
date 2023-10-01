# yıldızlarla şekiller
n = int(input("lütfen tablo ölçütünü giriniz:"))

print((n)*" ","*",(n)*" ")

for i in range(1,n):
    print((n-i)*" ","*"," "*(2*i-1),"*",(n-i)*" ")