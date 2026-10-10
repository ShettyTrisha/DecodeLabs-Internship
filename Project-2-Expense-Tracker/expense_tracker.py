# ---------------------------------------
#        PERSONAL EXPENSE TRACKER
# ---------------------------------------

expenses = []


def add_expense():
    print("\n----- ADD EXPENSE -----")

    try:
        amount = float(input("Enter expense amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        print("\nCategories:")
        print("1. Food")
        print("2. Travel")
        print("3. Shopping")
        print("4. Education")
        print("5. Other")

        category_choice = input("Choose category: ")

        categories = {
            "1": "Food",
            "2": "Travel",
            "3": "Shopping",
            "4": "Education",
            "5": "Other"
        }

        if category_choice in categories:
            category = categories[category_choice]
        else:
            category = "Other"

        description = input("Enter short description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

        print("\nExpense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    print("\n----- EXPENSE HISTORY -----")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['category']} - "
            f"₹{expense['amount']:.2f} - "
            f"{expense['description']}"
        )


def view_total():
    print("\n----- TOTAL SPENT -----")

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print(f"Total Spent: ₹{total:.2f}")


def category_summary():
    print("\n----- CATEGORY SUMMARY -----")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] = summary[category] + amount
        else:
            summary[category] = amount

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def delete_expense():
    print("\n----- DELETE EXPENSE -----")

    if len(expenses) == 0:
        print("No expenses available to delete.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)

            print(
                f"Deleted: {deleted['category']} - "
                f"₹{deleted['amount']:.2f}"
            )
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# Main program

while True:

    print("\n================================")
    print("       PERSONAL EXPENSE TRACKER")
    print("================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. Category Summary")
    print("5. Delete Expense")
    print("6. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        view_total()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("\nThank you for using Personal Expense Tracker!")
        break

    else:
        print("\nInvalid choice. Please select 1-6.")
