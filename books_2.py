def factorial(x):
    y = 1
    z = 0
    for i in range(1, x):
        y *= i
    number = str(y)
    for j in number:
        if j == 0:
            z += 1
    return z
    
a = int(input())

b = factorial(a)

print(b)
