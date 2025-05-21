day = input("Enter a day: ").lower()

match day:
    case "saturday" | "sunday":
        print("It's the weekend! Relax time.")
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("It's a workday. Stay productive!")
    case _:
        print("That's not a valid day.")
