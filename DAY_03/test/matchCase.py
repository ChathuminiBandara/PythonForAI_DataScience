x = int(input("Enter the number you want to check: "))

match x:
    case 0:
        print("Zero")
    case _ if x < 0:
        print("Negative Number")
    case _ if x > 0:
        print("Positive Number")
    case _ if x > 1:
        print("Positive Number Greater Than 1")
    case _ if x < -1:
        print("Negative number less than negative one") 
    case _:
        print("Unmatched Case!")
       
