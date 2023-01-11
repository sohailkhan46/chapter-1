x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
# The Ternary Operator

largest = x if (x > y and x > z) else (y if (y > x and y > z) else z) 
print("The largest number is: ", largest) 


# The multiple if -else operator
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if (x > y and x > z):
    largest = x
elif (y > x and y > z):
    largest = y
else:
    largest = z

print("The largest number is: ", largest)