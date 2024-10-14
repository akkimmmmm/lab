def yzor(rows):
    for i in range(rows):
        for j in range(rows - i):
            print(" ", end=" ")
        for j in range(2 * i + 1):
            print("*", end=" ")
        for j in range(2 * (rows - i - 1)):
            print(" ", end=" ")
        for j in range(2 * i + 1):
            print("*", end=" ")
        print()

    for i in range(rows - 1, -1, -1):
        for j in range(rows - i):
            print(" ", end=" ")
        for j in range(2 * i + 1):
            print("*", end=" ")
        for j in range(2 * (rows - i - 1)):
            print(" ", end=" ")
        for j in range(2 * i + 1):
            print("*", end=" ")
        print()

yzor(6)