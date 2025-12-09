# 1. From x and y
v1 = Vector2Math(12, x=3, y=4)
print("v1 vector:", v1.vector)
print("v1 magnitude:", v1.magnitude)
print("v1 angle:", v1.angle)

# 2. From angle and hypot
v2 = Vector2Math(12, angle=45, hypot=math.sqrt(2))
print("v2 vector:", v2.vector)
print("v2 magnitude:", v2.magnitude)
print("v2 angle:", v2.angle)

# 3. Subtraction
a = Vector2Math(12, angle=30, hypot=10)
b = Vector2Math(12, 0, 5)
c = a - b
print("a - b vector:", c.vector)

# 4. Addition
d = a + b
print("a + b vector:", d.vector)

# 5. Representation
print("Vector representation:", d)
