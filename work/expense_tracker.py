def sample_expenses():
    return [
        ["Food", "Lunch", 60.0],
        ["Transport", "Train", 40.0],
        ["Food", "Drink", 30.0],
        ["Study", "Notebook", 50.0],
    ]

def show_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print("Category     Description          Amount")
    for category, description, amount in expenses:
        print(f"{category:<12} {description:<20} {amount:>7.2f}")


def total_expenses(expenses):
    total = 0.0
    # BUG FIX 1: range(len(expenses) - 1) skipped the last expense.
    for index in range(len(expenses)):
        total += expenses[index][2]
    return total


def filter_by_category(expenses, category):
    selected = []
    for expense in expenses:
        # BUG FIX 2: was "!=", which returned every category EXCEPT the one requested.
        if expense[0].lower() == category.strip().lower():
            selected.append(expense)
    return selected


def average_expense(expenses):
    # BUG FIX 3: an empty list caused ZeroDivisionError; return 0.0 instead.
    if not expenses:
        return 0.0
    return total_expenses(expenses) / len(expenses)


def show_summary(expenses):
    print(f"Count: {len(expenses)}")
    print(f"Total: {total_expenses(expenses):.2f} THB")
    print(f"Average: {average_expense(expenses):.2f} THB")


def show_menu():
    print("\nEXPENSE TRACKER")
    print("1. Show all expenses")
    print("2. Show summary")
    print("3. Filter by category")
    print("4. Show empty-list summary")
    print("0. Exit")


def main():
    expenses = sample_expenses()
    while True:
        show_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            show_expenses(expenses)
        elif choice == "2":
            show_summary(expenses)
        elif choice == "3":
            category = input("Category: ")
            selected = filter_by_category(expenses, category)
            show_expenses(selected)
            show_summary(selected)
        elif choice == "4":
            show_summary([])
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
