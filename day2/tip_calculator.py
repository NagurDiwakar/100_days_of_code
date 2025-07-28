print("Welcome to the tip calculator!")
Total_bill = float(input("What was the total bill? $ "))
percentage_of_tip = int(input("What's the percentage of the tip you wanna give 10, 12 or 15? "))
number_of_people_to_split = int(input("How many people do you want to split the bill with? "))

# Calculate tip amount: bill * (percentage / 100)
tip_amount = Total_bill * (percentage_of_tip / 100)
total_with_tip = Total_bill + tip_amount
each_person_bill = total_with_tip / number_of_people_to_split

# Format to 2 decimal places
print(f"Each person should pay: ${each_person_bill:.2f}")