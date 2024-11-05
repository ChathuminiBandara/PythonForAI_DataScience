my_list_1 = [-10, -18, 12, 5, 7, 12, -3]
my_list_2 = [8, 4, -3, 9, 2, 11]

my_list_2.extend(my_list_1)
print("Before sorted list : " , my_list_2)
my_list_2.sort()
print("sorted list : " , my_list_2 )

position_of_median = (len(my_list_2)+1)/2
position_of_median = int(position_of_median)
median = position_of_median -1
print("Median is : " ,  my_list_2[median])

position_of_q1 = (len(my_list_2)+1)/4
position_of_q1 = int(position_of_q1)
value_of_position_of_q1 = my_list_2[position_of_q1]
print("Q1 is : " ,  value_of_position_of_q1)


position_of_q3 = (len(my_list_2)+1)/4
position_before_q3 = int((position_of_q3)*3)
position_after_q3 = int((position_of_q3)*3)+1
real_position_of_q3 = (position_before_q3 + position_after_q3)/2
print("real position of q3 ",real_position_of_q3)
real_position_of_q3 = int(real_position_of_q3)
value_of_position_of_q3 = my_list_2[real_position_of_q3]
print("Q3 is : " ,  value_of_position_of_q3)
