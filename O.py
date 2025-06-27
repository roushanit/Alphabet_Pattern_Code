for r in range(6):  
    for c in range(6):  
        if (c == 0 or c == 5) or ((r== 0 or r==5) and (c > 0 or c < 5)):
            print("*", end="")
        else:
            print(" ", end="")
    print()

