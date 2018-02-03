from math import sqrt
def answer(area):
    intlist =[]
    while area >= 1:
        length = int(sqrt(area))
        intlist.append(int(length**2)) #appending the current largest square area possible to the list
        area = int(area-length**2) #changing the area value by deducting the current largest area
    return intlist    