for r in range(7):  
    for c in range(5):  
        if ((c == 0 or c == 4) and r!=6) or (r==6 and (c>0 and c<4)):
            print("*", end="")
        else:
            print(" ", end="")
    print()

