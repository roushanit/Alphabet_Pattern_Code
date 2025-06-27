for r in range(6):  
    for c in range(7):  
        if c == 0 or c == 6 or (r == c and c <= 4):
            print("*", end="")
        else:
            print(" ", end="")
    print()

