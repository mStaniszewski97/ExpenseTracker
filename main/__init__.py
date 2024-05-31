import datetime

from expense import Expense


def main():
    expense_file_name = "expenses.csv"
    print("Welcome to expense tracker app")
    n = int(input("How many individual costs would you like to enter?"))
    for i in range(0, n):
        user_expense = get_user_expense()
        save_expense_to_file(user_expense, expense_file_name)

    summarize_expenses(expense_file_name)


def get_user_expense():
    print("Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_description = input("Optional expense description: ")
    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, amount=expense_amount, category=selected_category, date_added=datetime.date.today(),
                description=expense_description
            )
            return new_expense
        else:
            print("Invalid category. Please try again!")


def save_expense_to_file(user_expense: Expense, expense_file_path):
    print("🎯 Saving user expense to", expense_file_path)
    with open(expense_file_path, "a") as file:
        file.write(
            f"{user_expense.name},{user_expense.amount},{user_expense.category},{user_expense.date_added}"
            f",{user_expense.description}\n")


def summarize_expenses(expense_file_path):
    print("Summarizing User Expenses:")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category, expense_date_added, expense_description = line.strip().split(
                ",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
                date_added=expense_date_added,
                description=expense_description
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for i in range(0, len(expenses)):
        user_expense = expenses[i]
        key = user_expense.category
        if key in amount_by_category:
            amount_by_category[key] += user_expense.amount
        else:
            amount_by_category[key] = user_expense.amount
        print(
            f"{i+1}.{user_expense.name},{user_expense.amount},{user_expense.category},{user_expense.date_added},{user_expense.description}")

    print("Expenses By Category:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"Total Spent: ${total_spent:.2f}")


if __name__ == "__main__":
    main()
