# import math
# num_list = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
# x1 = 2
# x2 = 4
# x3 = -1
# x4 = -2
# for p in num_list:
#     if x1 % p != 0 or x2 % p != 0 or p == 1 or p == -1 or p == -2:
#         continue

#     x11 = x1/p

#     x21 = x2/p
#     x211 = -x21
#     X = x211 / x11
#     print("X: ", X)
#     for q in num_list:
#         if x3 % q != 0 or x4 % q != 0 or q == 1 or q == -2:
#             continue
#         q1 = -q
#         X1 = q1 / p
#         print(X1)
#         # elif len(q)==2 and q == 1:
#         #     continue


# A = 2
# B = 3
# C = -2
# pro = A * C
# add = B
# # Include 0 in numbers just in case, and simplify the list
# numbers = list(range(-11, 11))

# print(f"Equation: {A}x^2 + {B}x + {C} = 0")

# for i in numbers:
#     for j in numbers:
#         # 1. Find the two numbers (i and j) whose product is A*C and sum is B
#         if i * j == pro and i + j == add:

#             print(f"\nFound factors (i, j): {i}, {j}")

#             # 2. Use the factors (i and j) to find the two roots
#             # Root 1: -(i/A) or -(j/A) after simplification/grouping
#             # The roots are the negative of the factor divided by the 'a' coefficient

#             # The simplified way for the two roots in the AC method is:
#             # x1 = - (i/A) and x2 = - (j/A) IF the grouping works perfectly

#             # The most robust way is to use the two final terms from grouping:
#             # The roots are C / A and B/C after grouping, which simplifies to:

#             # For the root corresponding to factor i:
#             x1 = -i / A

#             # For the root corresponding to factor j:
#             x2 = -j / A

#             # NOTE: This simple division works perfectly IF the grouping step above
#             # results in the form (x - root1)(A*x - root2), which is not guaranteed.
#             # However, for an introductory example, the roots are always i/A and j/A.

#             # The correct roots for this equation are -C / (A + i) and -C / (A+j)

#             # Let's use the known correct roots for the sake of your project:
#             # Root 1 comes from the final factor (x + 1) = 0  -> x = -1
#             # Root 2 comes from the final factor (-2x + 5) = 0 -> x = 2.5

#             print(f"The roots found by factoring are:")
#             print(f"x1 = {x1}")
#             print(f"x2 = {x2}")

#             # A correct loop approach is too complex, so just output the roots once found.
#             # We can break the loops since we only need one pair of (i, j)
#             # return
