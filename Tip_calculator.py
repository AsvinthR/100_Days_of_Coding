print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?\n> "))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15?\n> "))
split = int(input("How many people are there to split the bill with?\n> "))

result = (total_bill * ((100 + tip_percent)/100)) / split
result = round(result, 2)
result = "{:.2f}".format(result)
print(f"Your split per person will be ${result}.")