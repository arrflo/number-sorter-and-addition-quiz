# Program 1: Number Sorter


# Create a program that ask 4 numbers.
def getNumber ():
    _first = int(input("First Number:"))
    _second = int(input("Second Number:"))
    _third = int(input("Third Number:"))
    _fourth = int(input("Fourth Number:"))
    return _first, _second, _third, _fourth


#other function
def display (arrangement):
    print (f"The arrangement of the four numbers from highest to lowest is as follows: {arrangement}.")


# function for if-else, tas yung sa arrangement
def getNumberSorter(a,b,c,d):
    # a ang highest
    if a >= b and a >= c and a >= d:  
        #b>c>d  
        if b >= c >= d:
            return a, b, c, d
        else: #b>d>c
            if b >= d >= c:
                return a, b, d, c
            else: #c>b>d
                if c >= b >= d:
                    return a, c, b, d
                else: #c>d>b
                    if c >= d >= b:
                        return a, c, d, b
                    else: #d>b>c
                        if d >= b >= c:
                            return a, d, b, c
                        else: #d>c>b
                                return a, d, c, b
    else: # b ang highest
        if b >= a and b >= c and b >= d:
            #a>c>d
            if a >= c >= d:
                return b, a, c, d
            else: #a>d>c
                if a >= d >= c:
                   return b, a, d, c
                else: #c>a>d 
                    if c >= a >= d:
                        return b, c, a, d
                    else: #c>d>a 
                        if c >= d >= a:
                            return b, c, d, a
                        else: #d>a>c
                            if d >= a >= c:
                                return b, d, a, c
                            else:   #d>c>a
                                    return b, d, c, a   
        else: # c ang highest
            if c >= a and c >= b and c >= d:
                #a>b>d
                if a >= b >= d:
                    return c, a, b, d
                else: #a>d>b
                    if a >= d >= b:
                        return c, a, d, b
                    else: #b>a>d 
                        if b >= a >= d:
                            return c, b, a, d
                        else: #b>d>a 
                            if b >= d >= a:
                                return c, b, d, a
                            else: #d>a>b
                                if d >= a >= b:
                                    return c, d, a, b
                                else:   #d>b>a
                                        return c, d, b, a
            else: # d ang highest
                # d >= a and d >= b and d >= c:
                 #a>b>c
                if a >= b >= c:
                    return d, a, b, c
                else: #a>c>b
                    if a >= c >= b:
                        return d, a, c, b
                    else: #b>a>c 
                        if b >= a >= c:
                            return d, b, a, c
                        else: #b>c>a 
                            if b >= c >= a:
                                return d, b, c, a
                            else: #c>a>b
                                if c >= a >= b:
                                    return d, c, a, b
                                else: #c>b>a
                                    return d, c, b, a  

# Print the 4 numbers from highest to lowest using only if-else statement.
first, second, third, fourth = getNumber()
arrange = getNumberSorter (first, second, third, fourth)
display (arrange)
