
if __name__ == "__main__" :

    print("Calculate Area for Respective Shapes")
    shape = input("Enter the name of shape for which you want to find area: ")


def calculate_area(shape):    #driver code
    shape = shape.lower()


if shape == "rectangle":
	l = int(input("Enter Length of Rectangle: "))
	b = int(input("Enter Breadth of Rectangle: "))
	
	# checking & calculation of rectangle for its area
	area_Rec = l * b
	print("The area of rectangle is: ", l, "*", b, "=", area_Rec)

elif shape == "square":
	s = int(input("Square's side length: "))
	
	area_Squ = s * s
	print("The area of square is: ", s, "*", s, "=", area_Squ)

elif shape == "triangle":
	h = int(input("Triangle's height: "))
	b = int(input("Triangle's breadth: "))
	
	area_Tri = 0.5 * b * h
	print("The area of triangle is: ", 0.5, "*", b, "*", h, "=", area_Tri)

elif shape == "circle":
	r = int(input("Radius of the Circle: "))
	pi = 3.14
		
	area_Cir = pi * r * r
	print("The area of circle is: ", pi, "*", r, "*", r, "=", area_Cir)
		
elif shape == 'parallelogram':
	b = int(input("Parallelogram's base length: "))
	h = int(input("Parallelogram's height length: "))

	area_Para = b * h
	print("The area of parallelogram is: ", b, "*", h, "=", area_Para)
	
else:
	print("Sorry! This shape is not available in the code I Made")

        # function calling
calculate_area(shape)
