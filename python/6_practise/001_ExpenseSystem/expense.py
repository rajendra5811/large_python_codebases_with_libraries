class Expense:
      def __init__(self, eid, title, amount, category, date):
          self.eid = eid
          self.title = title
          self.amount = amount
          self.category = category
          self.date = date

      def display(self):
        print(f"Expense ID: {self.eid}")
        print(f"Title: {self.title}")
        print(f"Amount: {self.amount}")
        print(f"Category: {self.category}")
        print(f"Date: {self.date}") 

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        eid = input("Enter Expense ID: ")
        title = input("Enter Title: ")
        amount = float(input("Enter Amount: "))
        category = input("Enter Category: ")
        date = input("Enter Date (YYYY-MM-DD): ")

        expense = Expense(eid, title, amount, category, date)
        self.expenses.append(expense)
        print("Expense added successfully!")

    def View_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
            return

        print("\nID\tTitle\tAmount\tCategory\tDate")
        print("------------------------")
        for expense in self.expenses:
            print(f"{expense.eid}\t{expense.title}\t{expense.amount}\t{expense.category}\t{expense.date}")

    def search_category(self):
        category = input("Enter Category to search: ")
        found = False
        print("\nID\tTitle\tAmount\tCategory\tDate")
        print("------------------------")

        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                print(f"{expense.eid}\t{expense.title}\t{expense.amount}\t{expense.category}\t{expense.date}")
                found = True
        if not found:
            print(f"No expenses found in category")   

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: {total}")

    def set_budget(self):
        self.budget = float(input("Enter your budget: "))
        print(f"Budget set Successfully!")

    def remaining_budget(self):
        total = sum(expense.amount for expense in self.expenses)
        remaining = self.budget - total
        print(f"Remaining Budget: {remaining}")
   
    def delete_expense(self):
        eid = input("Enter Expense ID to delete: ")
        for expense in self.expenses:
            if expense.eid == eid:
                self.expenses.remove(expense)
                print("Expense deleted successfully!")
                return
        print("Expense ID not found.")

system = ExpenseManager()
system.add_expense()
system.View_expenses()
system.search_category()
system.total_expenses()
system.set_budget()
system.remaining_budget()
system.delete_expense()
