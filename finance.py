def calculate(principal, interest_rate, years):
    amount = principal * pow((1 + interest_rate), years)
    return amount


principal = float(input("Enter the deposit: "))
interest_rate = float(input("Enter the rate: "))
years = float(input("Enter the years: "))

if principal < 0 or interest_rate < 0 or years < 0:
    print("Error! All values must be greater than zero")
else:
    print(f"{calculate(principal, (interest_rate / 100), years):.2f}")
