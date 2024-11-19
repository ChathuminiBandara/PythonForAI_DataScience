a = [1,4]

match a:
    case _ if len(a) == 0:
        print("List is empty !")
    case  [x]:
        print("List got 1 element !")
    case [x,y]:
        print("List got 2 elements !") 
    case _:
        print("Something Else!")
       