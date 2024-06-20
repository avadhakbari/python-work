def area_of_parallelogram(base,height):
    return base * height

b = int(input("enter base of area :"))
h = int(input("enter height of area :"))

area = area_of_parallelogram(b,h)

print(f"total area of parallelgram is {area}")