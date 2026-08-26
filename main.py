rows = int(input("Enter the # of rows: "))
colums = int(input("Enter the # of colums: "))
symbol = input("Enter the symbol to use: ")

for _ in range(rows):
    for y in range(colums):
        print(symbol, end="")
    print()
