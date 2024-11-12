a = int(input("Enter the a wanna check: "))
b = int(input("Enter the b wanna check: "))
c = int(input("Enter the c wanna check: "))

if a == b == c:
    print("All numbers are equal:", a)
elif a >= b and a >= c:
    if a == b:
        print("The largest numbers are a and b:", a)
    elif a == c:
        print("The largest numbers are a and c:", a)
    else:
        print("The largest number is a:", a)
elif b >= c:
    if b == c:
        print("The largest numbers are b and c:", b)
    else:
        print("The largest number is b:", b)
else:
    print("The largest number is c:", c)
