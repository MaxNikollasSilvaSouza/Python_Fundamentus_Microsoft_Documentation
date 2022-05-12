
print("First Number:")
try:
    first_number = int(input())
    print("Second Number:")
    second_number = int(input())
    sum = first_number + second_number
    
    print('Sum: ' + str(sum))
except ValueError:
    print('It was not possible to perform the calculation as what was entered is not valid!')

    