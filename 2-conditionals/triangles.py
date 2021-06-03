# This method asks for the lengths of the sides of a triangle,
# and reports the the three angles.

# To use math functions, import the math library.
import math

def main():
    print("Type in three side lengths of a triangle to find the three angles.")
    a = int(input("First side length: "))
    b = int(input("Second side length: "))
    c = int(input("Third side length: "))
    
    if not is_triangle(a, b, c):
        raise ValueError("This shape is not a triangle! Try again...")
    
    print(determine_angle(a, b, c)) # angle C
    print(determine_angle(b, c, a)) # angle A
    print(determine_angle(c, a, b)) # angle B

# For the shape to be a triangle, no one side may be
# equal to or longer than the sum of the other two sides.
# This method will determine this.
def is_triangle(a, b, c):
    return not(a >= b + c) and not(b >= a + c) and not(c >= a + b)

# This method uses the Law of Cosines to determine the angles.
def determine_angle(a, b, c):
    value1 = math.pow(a, 2) + math.pow(b, 2) - math.pow(c, 2)
    value2 = 2 * a * b
    return value1 / value2

main()