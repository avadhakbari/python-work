import math

def cylinder_surface_area(radius, height):
    base_area = math.pi * radius ** 2
    lateral_area = 2 * math.pi * radius * height
    return 2 * base_area + lateral_area

def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height



radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

surface_area = cylinder_surface_area(radius, height)
volume = cylinder_volume(radius, height)

print(f"The surface area of the cylinder is: {surface_area}")
print(f"The volume of the cylinder is: {volume}")
