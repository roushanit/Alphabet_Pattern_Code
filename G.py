for r in range(7):
    for c in range(5):
        if (c==0) or ((r==0 or r==6) and (c > 0)) or ((r==3) and (c > 1)) or ((c == 4 and (r == 4 or r == 5))): 
            print("*",end='')
        else:
            print(" ",end='')
    print()
