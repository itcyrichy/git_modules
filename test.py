
def get_dels(n):
    deliteli=[]
    for i in range(1,n+1):
        if n%i==0:
            deliteli.append(i)
    return deliteli

def simplicity_check(n):
    if n == 1:
        return True
    else:
        d = 2
        while n % d != 0:
            d += 1
        return d == n

def simple_del_max(deliteli):
    from functools import reduce
    a=[]
    for i in deliteli:
        if simplicity_check(i)==True:
            a.append(i)
        else:
            pass
    return a,reduce(lambda x,y:max(x,y),a)
