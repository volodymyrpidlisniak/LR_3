n = int(input('Enter the number whose factorial you want to know: '))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(factorial)