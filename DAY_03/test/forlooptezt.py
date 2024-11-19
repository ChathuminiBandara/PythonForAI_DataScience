my_list = [1, 2, 3, 4, 5]
my_new = []

for my in my_list:
    my_new.append(my * my)

print(my_new)

# list comprehension 

print([my**2 for my in my_list ])
