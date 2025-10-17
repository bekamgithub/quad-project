import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
add = b
product = a * c
number_list = [-11, -10, -9, -8, -7, -6, -5, -
               4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


number_list_two = [-11, -10, -9, -8, -7, -6, -5, -
                   4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in number_list:

    for j in number_list_two:
        if i * j != product or i + j != add:
            continue
        print(i, j)
