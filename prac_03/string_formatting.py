year = 1922
name = "Gibson L-5 CES"
cost = 16035.9

formatted_output = f"{year} {name} for about ${cost:,.0f}!"
print(formatted_output)

for i in range(11):
    result = 2 ** i
    print(f"2 ^ {i:<2} is {result:>4}")