from victorina import victorina

play = True
i = 0
while play:
    if i == 0:
        victorina()
    answ = input('Чтобы начать сначала, напишите "опять", чтобы выйти, нажмите "выход": ')
    if answ == 'опять':
        i += 1
        victorina()
    elif answ == 'выход':
        play = False
    else:
        i += 1
        pass

