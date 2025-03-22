class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance=initialAmount
        self.name=acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    ###########Protected:

    def _ViableTransaction(self, amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has balance of {self.balance:.2f}.")
        
    ############Public:

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        print("\n**************\n\nBeginning deposit...")
        self.balance +=amount
        print("\nDeposit complete.")
        self.getBalance()


    def Withdraw(self, amount):
        try:
            print("\n**************\n\nBeginning withdraw...")
            self._ViableTransaction(amount)
            self.balance-=amount
            print("Withdraw complete!")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw was interrupted: {error}")


    def Transfer(self, amount, account):
        try:
            print("\n**************\n\nBeginning transaction...")
            self._ViableTransaction(amount)
            self.Withdraw(amount)
            account.deposit(amount)
            print("Transfer complete!")
            self.getBalance()
        except BalanceException as error:
            print(f"Transfer was interrupted: {error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += amount*1.05
        print("\nDeposit complete.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        #self.name = "Joseph" we can overrride super
        self.fee = 5
    
    def Withdraw(self, amount):
        try:
            print("\n**************\n\nBeginning withdraw...")
            self._ViableTransaction(amount+self.fee)
            self.balance-=(amount+self.fee)
            print("Withdraw complete!")
            self.getBalance()
        except BalanceException as error:

            print(f"Withdraw was interrupted: {error}")

if __name__=="__main__":
    Dave = BankAccount(2000, "Dave")
    Jim = InterestRewardsAcct(1000, "Jim")
    Blaze = SavingsAcct(5000, "Blaze")


    for x in (Dave, Jim, Blaze):
        print(type(x)) #são tipos diferentes, mas têm ligação de herança, por isso podemos usar as operações dos pais com filhos

    Blaze.getBalance()


    try:
        raise BalanceException
    except Exception as error:
        print(type(error))



