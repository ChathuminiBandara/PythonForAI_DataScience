a = 200
print("Type of variable a : " , type(a) , "Value is " , a)

b = 2.1234
print("Type of variable b : " , type(b) , "Value is " , b)


c = 5+9j
print("Type of variable c : " , type(c) , "Value is " , c)

d = 2.5e4
e = -5.23e5
print("Type of variable d : " , type(d) , "Value is " , d)
print("Type of variable e : " , type(e) , "Value is " , e)

num_1 = 100
num_2 = 10.45
f = float(num_1)
g = int(num_2)

print("Type of the f variable is : ", f ," Type is : " , type(f))
print("Type of variable g : " , type(g) , "Value is " , g)

my_list = ["cat", "bot", "rat", "ant"]
print("Type of the my_list is" , type(my_list))
print("Catching and printing a index from the list :" , my_list[2])

my_list[2] = "robot"
print(my_list)

print("length of the my_List list is : ", len(my_list))
print("Starting from minus - from the end to start :" , my_list[-2])

number_list = [1,2,1,"kook",2,3,"ian",3,1,2,3,1,23]
print("Starting from the 0 index :" ,number_list[:4])
print("Starting from the mentioned index to the end :",number_list[4:])


initial_list = [1,"cat" , 10, "robot"]
initial_list[1:2] = ["Dog",19.0]

print(initial_list)

new_list = [1, "ian", 12, "Kamal", True]
print("the length of the old list is :" , len(new_list))
new_list.append("kamal")
print("the length of the new list is :" , len(new_list))
print(new_list)


new_list.insert(3, "Ian new value")
print(new_list , " new lists length : " , len(new_list))


new_list.extend(initial_list)
print(new_list)

print(new_list.pop(3))
del new_list[2]
# del my_list

my_list.clear()
print(len(my_list))