A = 2
B = 3
C = -2
pro = A * C
add = B
numbers = [-11, -10, -9, -8, -7, -6, -5, -4, -3, -
           2, -1,  1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# SECTION ONE
# here i wanted to find two numbers that when are added it gives B and when  multiplied it executes AC.
for i in numbers:
    for j in numbers:
        if j <= 0:
            continue
        if i * j != pro or i + j != add:
            continue
        print(i, "and", j)
        # SECTION TWO
 # here i wanted to find the GCf of A and i like what you did in number 3 factor by grouping.
        for k in numbers:
            if A % k != 0 or j % k != 0:
                continue
                # SECTION THREE
# here i wanted it to choose a negative value if surpose A was negative because in section two
 # it execute both positive and negative value and incase the the A value was positive it should choose a positive value.

            if A < 0:
                if k > 0:
                    continue
                print(k)

            elif A > 0:
                if k < 0:
                    continue
                print(k)
# so here is where i was stack when k executes to values  -1 and -2
# i don't a statement to make it choose the value like -2 if k executs more than one values
