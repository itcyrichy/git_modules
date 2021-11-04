from test import get_dels,simple_del_max,simplicity_check
def some_func(a=input('Введите целое число от 1 до 1000: ')):
    f = False
    r = False
    i = 0

    while not f:
        try:
            if i == 0:
                a = int(a)
                f = True
            else:
                a = int(input('Введите целое число от 1 до 1000: '))
                f = True
        except:
            print('Неверный формат. Введите целое число от 1 до 1000: ')
            i += 1

    while not r:
        if a>1000 or a<1:
            print('неверный диапазон, выберите число от 1 до 1000')
            a = int(input('Введите целое число от 1 до 1000: '))
        else:
            r = True
            pass

    simple = simplicity_check(a)
    if simple:
        simple = 'Простое'
    else:
        simple = 'Сложное'

    deliteli = get_dels(a)
    simple_dels,max_simp_del = simple_del_max(deliteli)
    return a,simple,deliteli,max_simp_del

print(some_func())
