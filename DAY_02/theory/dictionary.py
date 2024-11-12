thisDict = {
    "name": "Sugar",
    "name": "Yam",
    "Weight": "2Kg",
    "Price": 130.98
}

print("Items :" ,thisDict ,"Type : " , type(thisDict) , "Lenght of the Dict : ", len(thisDict))
print("Accessing a custom key :" , thisDict["Weight"])

thisDict["Weight"] = "1209 Kg"
print("Accessing a custom key :" , thisDict["Weight"])

thisDict.update({
    "name": "IAN",
    "Price" : 1232.99
})

print("Dictionary after update : " , thisDict) 