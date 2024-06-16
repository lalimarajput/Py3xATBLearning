#WAP that classifies a triangle based on its side length

# Triangle Classifier

def classify_triangle(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "Invalid triangle sides"
    if side1 == side2 == side3:
        return "Eq"  # Equilateral
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Iso"  # Isosceles
    else:
        return "Scalene"  # Scalene

# Example usage:
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

triangle_type = classify_triangle(side1, side2, side3)
print(f"The triangle is: {triangle_type}")