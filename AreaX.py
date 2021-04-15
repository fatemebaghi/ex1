def Area(A,B,C):
    p = (A+B+C)/2
    return (p*(p-A)*(p-B)*(p-C))**0.5


def AreaX(A,B,C,D):
    if A == 0 :
        return Area(B,C,D)
    elif B == 0 :
        return Area(A,C,D)
    elif C == 0 :
        return Area(A,B,D)
    elif D == 0 :
        return Area(A,B,C)
