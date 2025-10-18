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

        num_list = [-9, -8, -7, -6, -5, -4, -
                    3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
        x1 = a
        x2 = j
        x3 = i
        x4 = -2
        for p in num_list:
            if x1 % p != 0 or x2 % p != 0 or p == 1 or p == -1 or p == -2:
                continue

            x11 = x1/p

            x21 = x2/p
            x211 = -x21
            X = x211 / x11
            print("X: ", X)
            for q in num_list:
                if x3 % q != 0 or x4 % q != 0 or q == 1 or q == -2:
                    continue
                q1 = -q
                X1 = q1 / p
                print("X: ", X1)
                # elif len(q)==2 and q == 1:
                #     continue
