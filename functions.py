def square(side):
    area_square = side*side
    print("The area of the square is", area_square, "square units.")

side = int(input("Enter the length of the side of the square: "))
square(side)

def circle(radius):
    area_circle = 3.14*radius*radius
    print("The area of the circle is", area_circle, "square units.")

radius = int(input("Enter the radius of the circle: "))
circle(radius)