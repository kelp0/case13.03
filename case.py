#Работу выполнили: Лысенко Матвей 70%, Скороходов Михаил 40% гр.21704.1
import turtle
from math import sqrt
def get_color_choice(): #функция выбора цвета
    print('Допустимые цвета заливки: ')
    print('Фиолетовый')
    print('Красный')
    print('Зеленый')
    print('Светло-синий')
    print('Синий')
    print('Желтый')
    a = input('Пожалуйста, введите цвет: ')
    a = a.lower()
    if a == 'фиолетовый':
        return 'purple'
    elif a == 'красный':
        return 'red'
    elif a == 'зеленый':
        return 'green'
    elif a == 'светло-синий':
        return 'cyan'
    elif a == 'синий':
        return 'blue'
    elif a == 'желтый' or a == 'жёлтый':
        return 'yellow'
    else:
        a = input('Не является верным значением. Пожалуйста, повторите попытку: ')
        return get_color_choice()
def get_num_hexagons(): #Функция выбора количества шестиугольников в ряду
    b = input('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ')
    while ValueError:
        try:
            b = int(b)
            break
        except ValueError:
            b = input('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ')
    while not 4 <= int(b) <= 20:
        b = input('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ')
        while ValueError:
            try:
                b = int(b)
                break
            except ValueError:
                b = input('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ')
    return int(b)
def draw_hexagon(x,y,side_len,color): #Функция рисования шестиугольника
    turtle.speed(1000)
    turtle.setposition(x,y)
    turtle.fillcolor(color)
    turtle.up()
    turtle.left(90)
    turtle.down()
    turtle.begin_fill()
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.end_fill()
    turtle.right(90)
    turtle.up()
i = 1
j = 1
x = 0
y = 0
num = get_num_hexagons()
color1 = get_color_choice()
color2 = get_color_choice()
side_len = 500/num/2
s = 3*sqrt(3)*side_len*side_len/2
move = sqrt(s*2/sqrt(3))
move2 = side_len*side_len - (side_len*side_len/4)
ccc = ''
while j != num+1: #Цикл, смещающий turtle по оси ординат
    while i != num+1: #Цикл, описывающий линию шестиугольников
        if i % 2 == 1:
            color = color1
        elif i % 2 == 0:
            color = color2
        draw_hexagon(x,y,side_len,color)
        x += move
        i += 1
    i = 1
    x = x - (num)*move
    if j % 2 == 1:
        y = y - side_len
        y = y - side_len/2
        x = x - sqrt(side_len*side_len - (side_len*side_len/4))
    elif j % 2 == 0:
        y = y - side_len
        x = x + sqrt(move2)
        y = y - side_len/2
    if j % 2 == 0:
        ccc = color1 #Смена цвета для получения необходимого орнамента
        color1 = color2
        color2 = ccc
    j += 1
