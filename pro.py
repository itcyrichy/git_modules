from test import get_dels
n=100
def kanon(n):
    listik = [1]
    for i in range(2,abs(n)+1):
        while n%i==0:
            listik.append(i)
            n = n/i
    return listik

razlozhenie = kanon(n)
print(razlozhenie)
print(f'Максимальный делитель числа (само число): {max(get_dels(n))}, \
максимальный делитель из кононического разложения: {max(razlozhenie)}')