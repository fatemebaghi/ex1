def Area(A,B,C,D,E):
    if D == 0:
        p = (A+B+C)/2
        return (p*(p-A)*(p-B)*(p-C))**0.5
    elif D != 0:
        p1 = (A+B+E)/2
        p2 = (C+D+E)/2
        return ((p1*(p1-A)*(p1-B)*(p1-E))**0.5)+((p2*(p2-C)*(p2-D)*(p2-E))**0.5)


