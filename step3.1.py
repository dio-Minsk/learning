# Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение переданного списка
def modify_list(l):
    list_2 = []
    for i in l:
        if i % 2 == 0:
            list_2.append(int(i // 2))
    l.clear()
    for j in list_2:
        l.append(j)

#
#Срез позволяет изменить элементы списка, остальное делается генератором.
def modify_list(l):
    l[:] = [i//2 for i in l if i % 2 == 0]
