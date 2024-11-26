a = [1]

match x:
    case _ if len(a) == 0:
        print("List is empty !")
    case _ if len(a) == 1:
        print("List got 1 element !")
    case _ if len(a) == 2:
        print("List got 2 elements !") 
    case _:
        print("Something Else!")
       
# ----------------------------------

a = [1,4]

match a:
    case []:
        print("List is empty !")
    case  [x]:
        print("List got 1 element !")
    case [x,y]:
        print("List got 2 elements !") 
    case _:
        print("Something Else!")
          