print("welcome to rollercode ride")
height = int(input("What's your height"))

if height >= 120:
    print("You are allowed to take a ride")
    age = int(input("what's is ur age"))
    if age >=18:
        print("you need to pay 14 rupees")
    if age >=12:
        print("you need to pay 9 rupees")
    else:
        print("you need to pay 7 rupees")
else:
    print(" sorry , you are not allowed to ride")