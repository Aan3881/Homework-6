#Задача 30:  Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

a1, d, n = int(input("Введите число:")), int(input("Введите ещё раз число:")), int(input("И ещё раз:"))
progressive = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*progressive)