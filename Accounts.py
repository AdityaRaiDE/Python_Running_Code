import random
class Account():
    BANK  = 'BITCOIN BANK PVT.LTD !!'
    def __init__(self,name,dob,adharcard,pancard,account_type = None):
        self.name = name
        self.dob = dob
        self.adharcard = adharcard
        self.pancard = pancard
        self.account_type = 'Current Account' if account_type is None else 'Saving Account'
    def activate(self,balance):
        if self.account_type == 'Saving Account':
            if balance == 0:
                raise Exception('Balance must be greater than 0 for saving account')
            self.balance = balance
        else:
            if balance < 0:
                raise Exception('Balance cannot be greater than 0 for current account')
        self.account_number = random.randint(1,1000000000)
        return f"{self.account_number} is activated"
    def deactivate(self):
        accont_number = self.account_number
        del self.account_number
        return f"{accont_number} is activated"
    def withdraw(self,amount):
        if self.account_type == 'Saving Account' and amount <= (self.balance - 100):
            return f"Atm withdrwals allowed for {amount}"
        elif self.account_type == 'Current Account' and amount <= self.balance :
            return f"Atm withdrwals allowed for {amount}"
        else:
            return f"Atm withdrwals not allowed for {amount}"
    def deposite(self,amount):
        if amount > 0 :
            self.balance = self.balance + amount
        else:
            raise Exception(f"Invalid amount {amount} deposited")
    def __add__(self,another_account):
        """ Method to merge both account"""
        if isinstance(another_account,Account):
            if(self.name == another_account.name and
               self.dob == another_account.dob and
               self.adharcard == another_account.adharcard and
               self.pancard == another_account.pancard ):
                self.balance = self.balance + another_account.balance
        else:
            raise Exception("Acccount cannot be merged check name,dob,adharcard & pancard")
    def __repr__(self):
        return f"Acccount({self.name},'{self.dob}','{self.adharcard}','{self.pancard}')"
    def __str__(self):
        return f"{self.name} has account {self.account_number} with {Account.BANK}"
