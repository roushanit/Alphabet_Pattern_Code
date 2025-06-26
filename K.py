for r in range(7):
    for c in range(6):
        if (c==0) or ((c ==1) and (r== 3)) or ((c ==2) and (r== 2 or r==4)) or ((c ==3) and (r== 1 or r==5)) or ((c ==4) and (r== 0 or r==6)): 
            print("*",end='')
        else:
            print(" ",end='')
    print()
