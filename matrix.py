
'''solving matrices using list'''
'''   try this 
[1, -2, 0]     [3, 0]
[8, 0, 1]   X  [1, 2]   =  ?
[-2, 4, 6]     [-3, 4]                   
 '''

# SECTION ONE
column_one = [float(input("a1: ")), float(input("a2: ")), float(input("a3: "))]
column_two = [float(input("b1: ")), float(input("b2: ")), float(input("b3: "))]
column_three = [float(input("c1: ")), float(
    input("c2: ")), float(input("c3: "))]

# SECTION TWO
column2_one = [float(input("d1: ")), float(
    input("d2: "))]
column2_two = [float(input("e1: ")), float(
    input("e2: "))]
column2_three = [float(input("f1: ")), float(
    input("f2: "))]

# SECTION THREE
cone = column2_one[0]*column_one[0] + column2_two[0] * \
    column_one[1] + column2_three[0]*column_one[2]
ctwo = column2_one[0]*column_two[0] + column2_two[0] * \
    column_two[1] + column2_three[0]*column_two[2]
cthree = column2_one[0]*column_three[0] + column2_two[0] * \
    column_three[1] + column2_three[0]*column_three[2]

# SECTION THREE
cone1 = column2_one[1]*column_one[0] + column2_two[1] * \
    column_one[1] + column2_three[1]*column_one[2]
ctwo2 = column2_one[1]*column_two[0] + column2_two[1] * \
    column_two[1] + column2_three[1]*column_two[2]
cthree3 = column2_one[1]*column_three[0] + column2_two[1] * \
    column_three[1] + column2_three[1]*column_three[2]
print(f" {' '}{cone}  {cone1}\n {''} {ctwo}  {ctwo2}\n {cthree} {cthree3}")
