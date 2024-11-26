my_list = [3, 8, 15, 10, 9, 7,14]
new_list = []

# for my in my_list:
#     if isinstance(my, int) and my % 2 == 0:  
#         new_list.append(my)

# print(new_list)


# -------------


for x in my_list:
    if x % 2 ==0:
        continue
    else:
        print(x)