def victorina():
    right_answers=0
    wrong_answers=0
    right_answers, wrong_answers = q1(right_answers, wrong_answers)
    right_answers, wrong_answers = q2(right_answers, wrong_answers)
    right_answers, wrong_answers = q3(right_answers, wrong_answers)
    right_answers, wrong_answers = q4(right_answers, wrong_answers)
    right_answers, wrong_answers = q5(right_answers, wrong_answers)

    print(f'Правильные ответы: {right_answers}, неправильные ответы: {wrong_answers}')
    print(f'% првильных ответов: {right_answers/5*100}%')

def q1(right_answers,wrong_answers):
    a1 = input('Когда вступил в должность Джордж Вашингтон?(формат: 01.01.1900, без кавычек)')
    if a1 == '30.02.1789':
        print('Верно!')
        right_answers += 1
    else:
        print('Тридцатого апреля 1789 года')
        wrong_answers += 1
    return right_answers,wrong_answers

def q2(right_answers,wrong_answers):
    a2 = input('Когда вступил в должность Джон Адамс?(формат: 01.01.1900, без кавычек)')
    if a2 == '04.03.1797':
        print('Верно!')
        right_answers += 1
    else:
        print('Четвертого марта 1797 года')
        wrong_answers += 1
    return right_answers,wrong_answers


def q3(right_answers, wrong_answers):
    a3 = input('Когда вступил в должность Томас Джефферсон?(формат: 01.01.1900, без кавычек)')
    if a3 == '04.03.1801':
        print('Верно!')
        right_answers += 1
    else:
        print('Четвертого марта 1801 года')
        wrong_answers += 1
    return right_answers,wrong_answers

def q4(right_answers, wrong_answers):
    a4 = input('Когда вступил в должность Джеймс Мэдисон?(формат: 01.01.1900, без кавычек)')
    if a4 == '04.03.1809':
        print('Верно!')
        right_answers += 1
    else:
        print('Четвертого марта 1809')
        wrong_answers += 1
    return right_answers,wrong_answers

def q5(right_answers, wrong_answers):
    a5 = input('Когда вступил в должность Джеймс Монро?(формат: 01.01.1900, без кавычек)')
    if a5 == '04.03.1817':
        print('Верно!')
        right_answers += 1
    else:
        print('Четвертого марта 1817 года')
        wrong_answers += 1
    return right_answers, wrong_answers

if __name__ == '__main__':
    victorina()