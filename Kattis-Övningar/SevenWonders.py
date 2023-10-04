str = input("Enter your cards here: ").upper()
str = [*str]
x = 0
y = 0
z = 0
points = 0

for i in str:
    if i == 'T':
        x += 1
    elif i == 'G':
        y += 1
    elif i == 'C':
        z += 1

points = x**2 + y**2 + z**2
while x > 0 and y > 0 and z > 0:
    if x >= 1 and y >= 1 and z >= 1:
        points += 7
    x -= 1
    y -= 1
    z -= 1
print(f"You got {points} points!")