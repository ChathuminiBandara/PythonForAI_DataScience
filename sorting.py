sort_list = ["Dog", "carrot", "apple", "banana"]
print("Reversed List : ", sort_list.reverse())
sort_list.sort()
print(sort_list)

sort_list = ["Dog", "carrot", "apple", "banana"]
sort_list.sort(key=str.lower)
print(sort_list)

sort_list.sort(reverse=True)
print(sort_list)