m = int(input("Enter the marks u wanna check : "))
if m >= 100 or m < 0:
    print("Input Is out of range !")
elif 85 <= m <= 100:
    print("A")
elif 75 <= m:
    print("B")
elif 65 <= m:
    print("C")
elif 55 <= m:
    print("S")
else: 
    print("F")
