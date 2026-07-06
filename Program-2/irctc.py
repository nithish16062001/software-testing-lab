import random

passengers = []

# Input details for 6 passengers
for _ in range(6):
    passenger = []

    passenger.append(input("Enter passenger name: "))
    passenger.append(int(input("Enter Age: ")))
    passenger.append(input("Enter Gender (M/F): ").upper())

    if passenger[2] == 'F' and passenger[1] >= 18:
        passenger.append(input("Pregnancy Status [Yes/No]: "))
    else:
        passenger.append("N/A")

    passengers.append(passenger)

print("\nWelcome to IRCTC!\n")

# Allocate seat and fare discount
for p in passengers:

    if p[2] == "M":
        if p[1] >= 60:
            seat = random.choice(["Lower", "SideLower"])
            fareDiscount = "25%"

        elif p[1] <= 3:
            seat = random.choice(["Lower", "SideLower"])
            fareDiscount = "100%"

        else:
            seat = random.choice(
                ["Lower", "SideLower", "SideUpper", "Middle", "Upper"]
            )
            fareDiscount = "0%"

    elif p[2] == "F":
        if p[1] >= 58:
            seat = random.choice(["Lower", "SideLower"])
            fareDiscount = "25%"

        elif p[1] <= 3:
            seat = random.choice(["Lower", "SideLower"])
            fareDiscount = "100%"

        elif p[3].lower() == "yes":
            seat = random.choice(["Lower", "SideLower"])
            fareDiscount = "50%"

        else:
            seat = random.choice(
                ["Lower", "SideLower", "SideUpper", "Middle", "Upper"]
            )
            fareDiscount = "0%"

    else:
        seat = "Not Assigned"
        fareDiscount = "N/A"

    # Display Passenger Details
    print("-------------------------------")
    print("Passenger Name :", p[0])
    print("Age            :", p[1])
    print("Gender         :", p[2])
    print("Pregnancy      :", p[3])
    print("Seat Allocated :", seat)
    print("Fare Discount  :", fareDiscount)