class Investment:
    def __init__(self, iid, name, invType, amount, return_rate):
        self.iid = iid
        self.name = name
        self.invType = invType
        self.amount = amount
        self.return_rate = return_rate  

    def calculate_return(self):
        return (self.amount * self.return_rate) / 100
        
    def total_value(self):
       return self.amount + self.calculate_return()
    
    def display(self):
        print(f"Investment ID: {self.iid}")
        print(f"Name: {self.name}")
        print(f"Type: {self.invType}")
        print(f"Amount: {self.amount}")
        print(f"Return Rate: {self.return_rate}%")
        print(f"Calculated Return: {self.calculate_return()}")
        print(f"Total Value: {self.total_value()}")

class InvestmentSystem:
    def __init__(self):
         self.investments = []

    def find_investment(self, iid):
        for investment in self.investments:
            if investment.iid == iid:
                return investment
        return None
    def add_investment(self):
        iid = int(input("Enter Investment ID: "))
        name = input("Enter Investment Name: ")
        invType = input("Enter Investment Type: ")
        amount = float(input("Enter Investment Amount: "))
        return_rate = float(input("Enter Return Rate: "))

        investment = Investment(iid, name, invType, amount, return_rate)
        self.investments.append(investment)
        print("Investment Added successfully!")

    #View Investments
    def View_investments(self):
        if not self.investments:
            print("Investment Not Found ")
            return
        print("\nId: \t Name: \t Type: \t Amount: \t Return \t Value")
        print("---------------------------------------------------")

        for inv in self.investments:
            inv.display()

    # Search Investment
    def Search_investment(self):
        iid = int(input("Enter Investment ID to search: "))
        investment = self.find_investment(iid)
        if investment:
            print("Investment Found:")
            investment.display()
        else:
            print("\nInvestment Not Found.")

    # Calculate Return
    def calculate_return(self):
        iid = int(input("Enter Investment ID to calculate return: "))
        investment = self.find_investment(iid)
        if investment:
            print(f"Expected Return for Investment {investment.iid}: {investment.calculate_return()}")
        else:
            print("Investment Not Found.")

    def total_investment(self):
        total = sum(investment.total_value() for investment in self.investments)
        print(f"Total Investment Value: {total}")

    def total_profit(self):
        profit = sum(investment.calculate_return() for investment in self.investments)
        print(f"Total Expected Profit: {profit}")

    # Delete Investment
    def delete_investment(self):
        iid = int(input("Enter Investment ID to delete: "))
        investment = self.find_investment(iid)
        if investment:
            self.investments.remove(investment)
            print(f"Investment {investment.iid} deleted successfully!")
        else:
            print("Investment Not Found.")

# ======== Main Program ========

system = InvestmentSystem()

system.add_investment()
system.View_investments()
system.Search_investment()
system.calculate_return()
system.total_investment()
system.total_profit()
system.delete_investment()
