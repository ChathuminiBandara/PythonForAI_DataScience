# # 1st way
# import my_calculator.addition
# import my_calculator.substraction

# result1 = my_calculator.addition.add(3,2)
# result2 = my_calculator.substraction.subract(5,2) 

# print("Additon result :" , result1)
# print("Substracted result :" , result2)


# # 2nd way
# from my_calculator import substraction
# from my_calculator import addition

# result3 = addition.add(1,2)
# result4 = substraction.subract(3,2)

# print("Result on 2nd Way additon" ,result3)
# print("Result on 2nd Way substraction" ,result4)


# # 3rd way
# from my_calculator.addition import add
# from my_calculator.substraction import subract

# result5 = addition(3,4)
# result6 = subract(4,3)

# print("Result in 3rd way : ", result5)
# print("Result in 3rd way : ", result5)

from my_calculator import add, subract

result1 = add(4,3)
result2 = subract(5,4)
print(result1, result2)