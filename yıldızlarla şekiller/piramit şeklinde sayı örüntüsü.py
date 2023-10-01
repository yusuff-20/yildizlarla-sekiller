n = int(input("lütfen tablo ölçütünü giriniz:"))
for i in range(n):
    print(" "*(n-i-1),end=" ")
    for j in range(i+1):
        print(i+1,"",end=" ")
    print()