class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        if type(amount) == str:
            raise ValueError
        else:
            self._transactions.append(-amount)

    def __lt__(self, other):
        if self.balance < other:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.balance > other:
            return True
        else:
            return False

    def __le__(self, other):
        if self.balance <= other:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.balance >= other:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.balance == other:
            return True
        else:
            return False

    def __len__(self):
        return len(self._transactions)

    def __str__(self):
        return f'{self.name} account - balance: {self.balance}'

    def __getitem__(self, item):
        return self._transactions[item]




checking = Account('Checking')
checking + 10
checking + 10
checking + 3
checking - 8

print(list(checking))
# print(checking)
print(checking[0])