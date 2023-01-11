print('Please enter the lengths of the three sides of a triangle: ') 
side1 = int(input('Side 1:')) 
side2 = int(input('Side 2:')) 
side3 = int(input('Side 3:'))
# Ask user to input lengths of 3 sides of a triangle

if side1 + side2 >= side3 and side1 + side3 >= side2 and side2 + side3 >= side1: 
    # Check if lengths satisfy triangle inequality theorem

    print('Valid triangle') 
    # Check for type of triangle
    if side1 == side2 == side3:
        print('Equilateral triangle')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('Isosceles triangle')
    else:
        print('Scalene triangle')
else:
    print('Not a valid triangle')