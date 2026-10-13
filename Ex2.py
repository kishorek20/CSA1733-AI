
a = 0
b = 0

jug_a = int(input("Enter capacity of Jug A: "))
jug_b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

visited = []

while a != target and b != target and (a, b) not in visited:
    visited.append((a, b))

    if b == 0:
        b = jug_b
        print("Fill Jug B:", a, b)

    elif a == jug_a:
        a = 0
        print("Empty Jug A:", a, b)

    else:
        water = min(b, jug_a - a)
        a = a + water
        b = b - water
        print("Pour Jug B into Jug A:", a, b)

if a == target or b == target:
    print("Target amount reached!")
else:
    print("Target amount cannot be reached.")
