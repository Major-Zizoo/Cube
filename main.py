def cube(number):
    return number*number*number

def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
    
number=int(input("Enter number:"))
print(by_three(number))