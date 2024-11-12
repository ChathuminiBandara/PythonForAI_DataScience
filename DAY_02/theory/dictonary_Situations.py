thisDict = {
    "name": "Sugar",
    "name": "Yam",
    "Weight": "2Kg",
    "Price": 130.98
}
print("The older dictonary : " , thisDict)

thisDict["Color"] = "White"
print("New dictonary : " , thisDict)

thisDict.pop("Weight")
print("New dictonary : " , thisDict)

thisDict.popitem()
print("New dictonary : " , thisDict)
thisDict.clear()

# del thisDict
print(len(thisDict))

