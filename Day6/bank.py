class BankConfig:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance


config = BankConfig()


class SMSAlert:

    def update(self, message):
        print("SMS:", message)


class AuditLog:

    def update(self, message):
        print("Audit:", message)


class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self._balance = balance
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):
        self._balance += amount
        self.notify(f"{self.owner} deposited {amount} ETB")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self.notify(f"{self.owner} withdrew {amount} ETB")
        else:
            print("Insufficient balance")

    def statement(self):
        print(self.owner, self.number, self._balance)


class SavingsAccount(Account):

    def add_interest(self):
        self.deposit(self._balance * config.interest_rate)


class CurrentAccount(Account):

    def withdraw(self, amount):
        if amount <= self._balance + config.overdraft_limit:
            self._balance -= amount
            self.notify(f"{self.owner} withdrew {amount} ETB")
        else:
            print("Overdraft exceeded")


class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind == "savings":
            return SavingsAccount(owner, number, balance)

        elif kind == "current":
            return CurrentAccount(owner, number, balance)

        else:
            raise ValueError("Invalid account type")


account = AccountFactory.create("savings", "Mahder", "101", 5000)

account.subscribe(SMSAlert())
account.subscribe(AuditLog())

account.deposit(1000)
account.withdraw(500)
account.add_interest()

account.statement()