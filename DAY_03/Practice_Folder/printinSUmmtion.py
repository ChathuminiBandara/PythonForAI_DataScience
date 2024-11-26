total = 0  

while True:
    x = int(input("Enter the number you want to add (0 to stop): "))
    if x == 0:
        break
    total += x  

print("The total sum is:", total)
