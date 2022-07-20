
#  ДЗ для первого семинара
def maxmin(a, b):
    if int(a) > int(b):
        print(f'Большее число {a}, меньшее число {b}')
    else:
        print(f'Большее число {b}, меньшее число {a}')


def max(a, b, c):
    if a > b:
        if a > c:
            print(f'Наибольшее число {c}')
        else:
            print(f'Наибольшее число {a}')
    else:
        if b > c:
            print(f'Наибольшее число {b}')
        else:
            print(f'Наибольшее число {c}')


def isEven(value):
    if int(value) % 2 == 0:
        print(f'Число {value} четное')
    else:
        print(f'Число {value} не четное')


def allEven(value):
    i = int(value)
    arr = []
    while i > 0:
        if i % 2 == 0:
            arr.append(i)
        i -= 1
    return arr


#  ДЗ для втрого семинара
def weekday(day):
    day = int(day)
    if day == 1 : print('Понедельник будний день')
    if day == 2 : print('Вторник будний день')
    if day == 3 : print('Среда будний день')
    if day == 4 : print('Четверг будний день')
    if day == 5 : print('Пятница будний день')
    if day == 6 : print('Суббота выходной день')
    if day == 7 : print('Воскресенье выходной день')


def num3(numbers):
    if len(numbers) > 2:
        num_3 = numbers[2]
        if num_3:
            print(f'Третья цифра {num_3}')
    else:
        print('Третьей цифры нет')




if __name__ == '__main__':
    a = input()
    num3(a)
