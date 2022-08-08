            # ЗАДАНИЕ 1

# def func1(string):
#     return string.lower()

# def func2(string):
#     return string.upper()

# string = "welcome to UKRAINE"

# print(list(map(func1, string.split())))
# print(tuple(map(func2, string.split())))


                    # Задание 2

# def squre(x):
#     return x*x

        # # Необходимо возвести в квадрат все простые числа в списке используя функцию map

# def is_prime(x):
#     for i in range(2, x//2 + 1):
#         if x % i == 0:
#             return False
#     return True

# def check(x):
#     if is_prime(x):
#         return squre(x)
#     else:
#         return 0

# print(list(map(check, range(2, 101))))


                # Задание 3
        # Есть файл, в котором много англоязычных текстовых строк. 

# import sys
# filename = open(sys.argv[1])
# words = filename.read().replace(",", "").replace("-", "").replace("!", "").replace(".", "").split()
# set_words = set(words)

        # Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!

            # Решение 1  (через несколько "определяемых" функций)
# def words_count(words):
#     return list(map(words.count, set_words))

# def name_wordscount(words):
#     return list(i for i in set_words)
# def concat(words):
#     return list(zip(name_wordscount(words), words_count(words)))
# print(concat(words))

            # Решение 2  ( через list_comprehension, ZIP )
# print(list(zip(set_words, (words.count(i) for i in set_words))))

            # Решение 3  (через функции MAP, ZIP )
# l = list(zip(set_words, list(map(words.count, set_words))))
# print(l)

# filename.close()