def kalp():
    for satir in range(6):
        for sutun in range(7):
            if (satir == 0 and sutun % 3 != 0) or (satir == 1 and sutun % 3 == 0) or (satir - sutun == 2) or (satir + sutun == 8):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
kalp()
