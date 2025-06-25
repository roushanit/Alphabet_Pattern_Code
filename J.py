for r in range(5):
    for c in range(8):
        if (c==4) or ((r==4) and (c < 5)) or (r==0 ): 
            print("*",end='')
        else:
            print(" ",end='')
    print()
