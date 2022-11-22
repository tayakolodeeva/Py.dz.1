# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = int(input('Введите X = '))
y = int(input('Введите Y = '))

if x > 0 and y > 0:
    print(f'x = {x}; y = {y}; -> 1')
elif x < 0 and y > 0:
    print(f'x = {x}; y = {y}; -> 2')
elif x < 0 and y < 0:
    print(f'x = {x}; y = {y}; -> 3')
elif x > 0 and y < 0:
    print(f'x = {x}; y = {y}; -> 4')
else :
    print('Точка не находится ни в одной плоскости :(')
