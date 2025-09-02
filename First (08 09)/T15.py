for A in range(100):
    for i in range(100):
        if ((i<27 and i>5) == (not(max(i,5)>10))) and (4+A>i) and (A<4+i) and (4<A+i):
            break
    else: print(A)
