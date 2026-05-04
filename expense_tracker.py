import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def create_file_if_not_exists():
    """
    Creates the CSV file if it does not already exist.
    The file stores all expense records.
    """
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense():
    """
    Adds a new expense record to the CSV file.
    """
    print("\n--- Add New Expense ---")

    category = input("Enter category (Food, Transport, Education, etc.): ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    description = input("Enter description: ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


def view_expenses():
    """
    Displays all saved expenses.
    """
    print("\n--- Expense List ---")

    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) <= 1:
            print("No expenses found.")
            return

        for index, row in enumerate(rows):
            if index == 0:
                continue

            date, category, amount, description = row
            print(f"{index}. Date: {date}")
            print(f"   Category: {category}")
            print(f"   Amount: {amount} TL")
            print(f"   Description: {description}")
            print("-" * 40)


def show_total_expense():
    """
    Calculates and displays the total expense amount.
    """
    total = 0

    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print("\n--- Total Expense ---")
    print(f"Total amount spent: {total:.2f} TL")


def show_category_summary():
    """
    Shows total expenses grouped by category.
    """
    category_totals = {}

    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    print("\n--- Category Summary ---")

    if not category_totals:
        print("No expenses found.")
        return

    for category, total in category_totals.items():
        print(f"{category}: {total:.2f} TL")


def main_menu():
    """
    Main menu of the expense tracker application.
    """
    create_file_if_not_exists()

    while True:
        print("\n==============================")
        print(" Personal Expense Tracker")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Expense")
        print("4. Show Category Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total_expense()
        elif choice == "4":
            show_category_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()
