# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
ax = float(input('Введите точку Ax : '))
ay = float(input('Введите точку Ay : '))
bx = float(input('Введите точку Bx : '))
by = float(input('Введите точку By : '))

import math
distance = round(math.sqrt((bx - ax)**2 + (by - ay)**2), 2)
print(f'A ({ax},{ay}) B ({bx},{by}) -> {distance}')

