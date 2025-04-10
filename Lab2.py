a = 3 

b = 4
while b <= 6:
    if a <= b:
        z = 3 * a**2 - 2 * b
    else:
        z = 6 * a * b - 3 * a
    print(f"b = {b}, z = {z}")
    b += 0.2
