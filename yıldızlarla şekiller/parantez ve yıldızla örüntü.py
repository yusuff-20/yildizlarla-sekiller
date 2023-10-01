sayi = int(input("Sayı giriniz:"))

for i in range(sayi):
    print(" "*(sayi-i),"(",end="")
    print("*"*(i*2),end="")
    print(")")

for i in range(sayi,-1,-1):
    print(" "*(sayi-i), "(",end="")
    print("*"*(i*2),end="")
    print(")")


n = int(input("bir sayı giriniz:"))
yeni_n = int(str(n)[::-1])

for i in range(n):
    islem = int(str(yeni_n)[i])*(10**i)
    print(islem)