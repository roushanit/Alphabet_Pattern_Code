for r in range(6):
    for c in range(8):
        if (c==0 or c== 7) or ((r==3) and (c > 2 and c < 4)) or ((r==2) and (c > 1 and c < 3)) or ((r==1) and (c > 0 and c < 2)) or ((r==1) and (c > 4 and c < 6)) or ((r==2) and (c > 3 and c < 5)): 
            print("*",end='')
        else:
            print(" ",end='')
    print()
