my_list_1 = [1, 2, 3, ["a", "b"]]
my_list_2 = my_list_1.copy()

print(my_list_2)

my_list_1[1] = "KAMAL"
print(my_list_1)
print("My_List_3 by copy :" , my_list_2)


my_list_3  = list(my_list_1)
print("My_List_3 by constructor:" , my_list_3)

# joining by +
my_list_5 = my_list_1 + my_list_3
print("List joining by +  :",my_list_5)