fibonacci = []
a, b = 0, 1

for i in range(20):
    fibonacci.append(a)
    a, b = b, a + b

print(fibonacci)
