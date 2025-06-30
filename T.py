for r in range(7):  
    for c in range(5):  
        if r == 0 or ((c==2) and (r>0 and r<5)):
            print("*", end="")
        else:
            print(" ", end="")
    print()

