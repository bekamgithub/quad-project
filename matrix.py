
'''solving matrices using list'''


# SECTION ONE
column_one = [1, -2, 0]
column_two = [8, 0, 1]
column_three = [-2, 4, 6]

# SECTION TWO
column2_one = [3, 0]
column2_two = [1, 2]
column2_three = [-3, 4]

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
