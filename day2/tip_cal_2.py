print("Welcome to the tip calculator!")
Total_bill = float(input("What was the total bill? $ "))
percentage_of_tip = int(input("What's the percentage of the tip you wanna give 10, 12 or 15? "))
number_of_people_to_split = int(input("How many people do you want to split the bill with? "))

each_person_to_pay = ((Total_bill + (percentage_of_tip / 100)) / number_of_people_to_split )

print(f"each person has to pay : " , each_person_to_pay)