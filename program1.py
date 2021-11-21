# Program 1: Number Sorter


# Create a program that ask 4 numbers.
def getNumber ():
    _first = int(input("First Number:"))
    _second = int(input("Second Number:"))
    _third = int(input("Third Number:"))
    _fourth = int(input("Fourth Number:"))
    return _first, _second, _third, _fourth

# function for if-else, tas yung sa arrangement
def getNumberSorter(a, b, c, d):
    a = first
    b = second
    c = third
    d = fourth
    if a > b > c > d:
        print (f"{a}, {b}, {c}, {d}")



first, second, third, fourth = getNumber()
arrange = getNumberSorter (first, second, third, fourth)
print (f"The arrangement of the four numbers from highest to lowest is as follows: {arrange}.")
# Print the 4 numbers from highest to lowest using only if-else statement.
# function to na gagawin ko mamaya >> arrange (first, second, third, fourth)