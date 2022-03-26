#####################
### Happy Numbers ###
#####################

def sumSquareOfDigits(n):
    #print("Summing the square of the digits", end="")
    sum = 0
    while n != 0:
        print(". ",end="")
        sum = sum + (n % 10)**2
        n = n // 10

    return sum

def isHappy(n):
    happy = True
    values = []
    while n != 1: # As long as we don't reach 1 as value or a result is repeated, we keep going
        value = sumSquareOfDigits(n)
        if value in values: # Repeated result, number can't possibly be happy
            happy = False
            break
        else: # This value is not in the list yet, so we add it to the list
            values.append(value)
            n = value

    return happy

number = int(input("Please enter an integer: "))
# Now send number to isHappy() and print result
print(isHappy(number))
