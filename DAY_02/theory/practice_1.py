my_tuple_1 = (10, 8, 20, 5)
my_tuple_2 = (5, 9, -1)

my_tuple_3 = list(my_tuple_1)
my_tuple_3.remove(20)
my_tuple_4 = list(my_tuple_2)
my_tuple_4.extend(my_tuple_3)
my_tuple_4.sort()
my_tuple_5 = tuple(my_tuple_4)
print(my_tuple_4)