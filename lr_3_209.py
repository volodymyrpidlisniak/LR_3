n = int(input('Enter the amount of times you want to print "#": '))

for i in range(n, 0, -1):
    print(i, '#' * i)