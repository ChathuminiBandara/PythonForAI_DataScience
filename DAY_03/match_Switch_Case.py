response_Code = 404
match response_Code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 404:
        print("404 Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Something went Wrong !")