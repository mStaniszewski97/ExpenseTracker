class Expense:

    def __init__(self, name, amount, category, date_added, description=None):
        self.name = name
        self.amount = amount
        self.category = category
        self.date_added = date_added
        self.description = description