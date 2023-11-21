class Category:

  def __init__(self,category):
    self.ledger = []
    self.category = category

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    self.ledger.append({"amount": -amount, "description": description})

  def check_funds(self, amount):
    sum_of_ledge = 0
    for item in self.ledger:
      sum_of_ledge += item["amount"]
    return sum_of_ledge < amount

  def get_balance(self):
    pass

  def transfer(self):
    pass


def create_spend_chart(categories):
  print(categories)
