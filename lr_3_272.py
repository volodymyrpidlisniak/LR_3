a = int(input('Enter a: '))
b = int(input('Enter b: '))

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print(a)