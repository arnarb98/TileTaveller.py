def check_north(x,y):
    north = True
    if y == 3 or (y == 2 and x == 2):
        north = False
    return north

def check_east(x,y):
    east = False
    if(x == 1 and y == 2):
        east = True
    if(x == 1 and y == 3):
        east = True
    if(x == 2 and y == 3):
        east = True
    return east

def check_south(x,y):
    south = True
    if(y == 1):
        south = False
    if(x == 2 and y == 3):
        south = False
    return south

def check_west(x,y):
    west = False
    if(x == 2 and y == 3):
        west = True
    if(x == 3 and y == 3):
        west = True
    if(x == 2 and y == 2):
        west = True
    return west

def prompt_user(x,y):
    print("You can travel: ", end = "")
    if check_north(x,y) == True:
        print("(N)orth ", end = "")
    if check_east(x,y) == True:
        print("(E)ast ", end = "")
    if check_south(x,y) == True:
        print("(S)outh ", end = "")
    if check_west(x,y) == True:
        print("(W)est ", end = "")

x = 1
y = 1

while(x != 1 and y != 3):
    prompt_user(x,y)
    check_east(x,y)
    check_north(x,y)
    check_south(x,y)
    check_west(x,y)
    x = str(input("Direction: "))

print("Victory!")

