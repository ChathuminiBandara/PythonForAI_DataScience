a = int(input("Enter the a wanna check: "))
b = int(input("Enter the b wanna check: "))
c = int(input("Enter the c wanna check: "))

if a > b and a > c:
    print("The biggest number is a :", a)
elif b > c:
    print("The biggest number is b :", b)
else:
    print("The biggest number is c :", c)
