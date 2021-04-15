import random
def Rand2(a,b):
    x=random.randint(a,b)
    if x % 2==0:
        return x
    elif x % 2 !=0 and a<=x<b:
        return x+1
    elif x % 2 !=0 and x==b:
        return x-1
