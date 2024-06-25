class Expense:
    def __init__(self, name, employeeID, category, amount):
        self.name = name
        self.employee_ID = employeeID
        self.category = category
        self.amount = amount


file_path = "expense.csv"  # lets say company has provided 10000 per month as budget
budget = 10000


def main():
    print("🎰Running employee expense tracker!")
    print("📊Getting expense details")
    user_input = add_expense()  # getting input for expense.
    save_expense(user_input, file_path)  # write and save expense
    summarize_expense(file_path)


def add_expense():
    enter_name = input("📛Enter employee name:")
    enter_employee_id = input("👤Enter your employee ID:")
    enter_amount: float = float(input("🈷️Enter expense amount:"))
    enter_category = [
        "Travel",
        "laptop",
        "meal",
        "Headset",
        "Stationary",
        "hard disk",
        "Mobile",
        "Accommodation",
    ]  # created list here so user can select it.
    print("Select the category: ")
    for i, category in enumerate(enter_category):
        print(
            f"{i + 1}. {category}"
        )  # to make sure number starts from 1 adding +1 here
    # adding while loop if in case user selects other than the given list.
    while (
        True
    ):  # now need to prompt employee to select from category so using value range
        value_range = f"[1- {len(enter_category)}]"
        # -1 is as we know according to python index is 0
        # adding integer to avoid if in case user adds alphabets
        selectedindex = int(input(f"⌖Enter a category name{value_range}: ")) - 1
        # now creating if statement to make sure person is selecting within the range
        if selectedindex in range(len(enter_category)):
            # i have imported class from expense.py however category is not selected yet so creating new variable to get it as we have only expense category and select index
            updated_category = enter_category[selectedindex]
            updated_expense = Expense(
                name=enter_name,
                employeeID=enter_employee_id,
                amount=enter_amount,
                category=updated_category,
            )
            return updated_expense
        else:
            print("Invalid category. Please try again")


def save_expense(
    expense: Expense, file_path
):  # to get the class details we can mention Expense class name in row 49
    print(f"Saving expense details: {expense} to {file_path}")
    # to open the file and to append
    with open(file_path, "a") as f:
        f.write(
            f"{expense.name},{expense.employee_ID},{expense.category},{expense.amount}\n"
        )


def summarize_expense(file_path):
    print("Summarizing expense details")
    expenses: list[Expense] = []
    with open(file_path, "r") as f:
        lines = f.readlines()
    # its creating space between each lines so need to use strip method and split to avoid extra lines in between
    for line in lines:
        # here i need to mention expense details .  in def add expenses so that i can get the variables else it wil through the error
        (
            expense_name,
            expense_employee_id,
            expense_category,
            expense_amount,
        ) = line.strip().split(",")
        line_expense = Expense(
            name=expense_name,
            employeeID=expense_employee_id,
            category=expense_category,
            amount=float(expense_amount),
        )
        expenses.append(line_expense)


# what tasks to be completed
# 1.now need all the expense in category wise so creat dict
# 2.finally need to check for the final budget how much amount is left with the team after all the deductions so we are summarizing that as well
# 3.per day expenses
# 4. if  Total expense goes to -ve then we need to send a warning message
# 5. prepar bar chart  or any type of chart with this


# just to get the main lines in different colour using below def
def green(text):
    return f"\033[92m{text}\033[0m"


def yellow(text):
    return f"\033[33m{text}\033[0m"


def red(text):
    return f"\033[31m{text}\033[0m"


if __name__ == "__main__":
    main()
