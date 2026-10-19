n = int(input('Enter the number of pounds you want to convert to kg: '))

for pounds in range(1, n + 1):
    kg = pounds * 0.453
    print(f"{pounds} {kg:.2f}")