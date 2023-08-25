# Функции с переменным число аргументов
def var_args(*args):
    """
    :param args: только целые числа,
    :return: кортеж - число аргументов и сумму как целое число
    """
    summ = 0
    for arg in args:
        summ += arg
    return len(args), summ, args


def named_args(**kwargs):
    print(kwargs)


def any_func_refer(n):
    n[1] = 0
    print(n)


qnt, summa, lst = var_args(1, 2, 3, 4, 5)
print('Число аргументов:', qnt)
print('Сумма:', summa)
print('Числа на входе:', *lst)

# вызов named_args (key-word args)
named_args(first='первый', second='второй', third='третий')

array = [5, 25, 625]
any_func_refer(array)
