def factorial(x):
    y = 1
    for i in range(1, x):
        y *= i
    return y
    
a = int(input())

b = factorial(a)

print(b)
