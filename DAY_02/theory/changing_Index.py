my_Tuple_1 = ("Rat", "Cat","Dog")
my_Tuple_2 = list(my_Tuple_1)
print("Current type of the my_Tuple_2 after covertion of the list :", type(my_Tuple_2))
my_Tuple_2[2] = "KAMAL"
my_Tuple_1 = tuple(my_Tuple_2)
print("Current type of the my_Tuple_2 after covertion of the tuple :", type(my_Tuple_1))