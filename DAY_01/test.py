my_list_1 = [-10, -18, 12, 5, 7, 12, -3]
my_list_2 = [8, 4, -3, 9, 2, 11]


my_list_2.extend(my_list_1)

print("Before sorted list : " , my_list_2)
my_list_2.sort()
print("sorted list : " , my_list_2 )

length = len(my_list_2)
print("length is :" , length)

print("Median is : " ,  my_list_2[6])

oneQ = int(length/4)

q1 = my_list_2[oneQ]
print("q1 : " ,q1)

q3 = 3*int(length/4)
print("q3 :" ,my_list_2[q3])