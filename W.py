for r in range(6):  
    for c in range(9):  
        if (c== 0 or c== 6) or ((r==4) and (c==2 or c==4)) or ((r==5) and (c==1 or c==5))or (r==c and r==3):
            print("*", end="")
        else:
            print(" ", end="")
    print()

