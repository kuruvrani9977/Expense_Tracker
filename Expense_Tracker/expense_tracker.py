expenses = []

while True:
    print("\n" + "=" * 40)
    print("        EXPENSE TRACKER")
    print("=" * 40)

    print("\nMenu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append([name, amount])

        print("\nExpense added successfully!")

    elif choice == "2":
        print("\nYour Expenses:")

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            for expense in expenses:
                print(expense)

    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice")
        while True:
            break