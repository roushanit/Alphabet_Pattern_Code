for r in range(7):  
    for c in range(7):  
        if ((r==0) and (c==0 or c==6)) or ((r==1) and (c==1 or c==5)) or ((r==2) and (c==2 or c==4)) or (r==c and r==3):
            print("*", end="")
        else:
            print(" ", end="")
    print()

