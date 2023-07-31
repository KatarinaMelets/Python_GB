#Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
#Диаметр не превышает 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.

from math import pi


number = float(input('Введите диаметр круга: '))
circumference_length = pi * number
circle_area = pi * pow(number / 2, 2)
print(f'Длинна окружности = {circumference_length:.42f} \n'
      f'Площадь круга = {circle_area:.42f}')