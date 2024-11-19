x = [4,3,2]

match x:
    case [x,y]:
        print("in the x y pattern : ",x*y)
    case [x,y,z]:
        print("in the x y z pattern : ",x+ y+ z) 
    case _:
        print("list dsnt contain 2 or 3!")
       
