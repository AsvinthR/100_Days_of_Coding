age = input("What is your current age? ")

age_num = int(age)

years_left = 90 - age_num
days_remaining = years_left * 365
weeks_remaining = years_left * 52
months_remaining = years_left * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
