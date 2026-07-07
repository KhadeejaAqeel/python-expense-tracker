print("Welcome to Expense Tracker")

total = 0

while True:

    expense = input("Enter expense or type 'quit': ")

    if expense == "quit":
        break

    try:
        expense = int(expense)
    except ValueError:
        print("Please enter a valid number.")
        continue

    total = total + expense

    print("Current Total:", total)

print("Final Total Spent:", total)