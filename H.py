for r in range(7):
    for c in range(7):
        if (c==0 or c==6) or (r==3): 
            print("*",end='')
        else:
            print(" ",end='')
    print()
