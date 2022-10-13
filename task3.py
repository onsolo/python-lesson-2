# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2


def getRowsIntersections(row_1, row_2):
    for i in row_1:
        count = 0
        for k in range(0, len(row_2)):
            if i == row_2[k]:
                count += 1
        print(f'{i} - {count}')


firs_string = input('Введите первую строку: ')
second_string = input('Введите вторую строку: ')

if second_string > firs_string:
    getRowsIntersections(firs_string, second_string)
else:
    getRowsIntersections(second_string, firs_string)
