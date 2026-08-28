def calculate(principal, interest_rate, years):
    amount = principal

    for year in range(1, years + 1):
        amount *= 1 + interest_rate
    return amount


principal = float(input("Enter the deposit: "))
interest_rate = float(input("Enter the rate: "))
years = int(input("Enter the years: "))

if principal < 0 or interest_rate < 0 or years < 0:
    print("Error! All values must be greater than zero")
else:
    print(f"{calculate(principal, (interest_rate / 100), years):.2f}")
