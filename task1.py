# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def getFactorial(number):
    fact = 1
    for number in range(1, number + 1):
        fact *= number
    return fact


def getFactorialList(number):
    fact_list = []
    for i in range(1, number + 1):
        fact_list.append(getFactorial(i))
    return fact_list


n = int(input('Введите N: '))
print(getFactorialList(n))
