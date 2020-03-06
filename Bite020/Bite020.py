class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager

    def __enter__(self):
        if self.balance < 0:
            print('debt')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass




def account():
    return Account()


a = account()
print(a.balance)