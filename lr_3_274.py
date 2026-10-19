a = int(input('Enter a: '))
b = int(input('Enter b: '))

quotient = 0
remainder = a

while remainder >= b:
    remainder -= b
    quotient += 1

print(quotient, remainder)