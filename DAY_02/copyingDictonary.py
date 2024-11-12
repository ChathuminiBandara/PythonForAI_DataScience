thisDict = {
    "name": "Sugar",
    "name": "Yam",
    "Weight": "3Kg",
    "Price": 130.98
}

dict_2 = thisDict.copy()
thisDict["name"] = "kamal1"
print( "Dictonary 1 : ",thisDict, "Dictonary 2 : ",dict_2)


this_Constructo_Dict_1 = {
    "name": "Sugar",
    "name": "Yam",
    "Weight": "3Kg",
    "Price": 130.98
}

new_Constructo_Dict_1 = dict(this_Constructo_Dict_1)
print( "Dictonary by Dict constructor : ",new_Constructo_Dict_1)
print( "Keys of the thisDict :",thisDict.keys())