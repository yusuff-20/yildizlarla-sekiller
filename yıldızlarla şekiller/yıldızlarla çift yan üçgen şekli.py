def kalp():
    for i in range(6, -7, -1):
        for j in range(0, 7 - abs(i)):
            if (i == 0) & (j == 0):
                print(" ", end=" ")
            else:
                print("*", end=" ")
        for k in range(0, abs(i)):
            print(" ", end=" ")
        for l in range(0, 7 - abs(i)):
            print("*", end=" ")
        print()
kalp()