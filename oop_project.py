from bank_accounts import  *

Dave = BankAccount(2000, "Dave")
Sara = BankAccount(3000, "Sara")

Dave.getBalance()
Sara.getBalance()

Dave.Withdraw(10000)

Sara.Transfer(1000, Dave)

Dave.Withdraw(100)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.deposit(100)

Jim.Transfer(500, Sara)

Blaze = SavingsAcct(5000, "Blaze")

Blaze.Transfer(100, Jim)

##Pelo polimorfismo, podemos fazer transferência entre diferentes classes

if __name__=="__main__":
    for x in (Dave, Jim, Blaze):
        print(type(x)) #são tipos diferentes, mas têm ligação de herança, por isso podemos usar as operações dos pais com filhos

    try:
        raise BalanceException
    except Exception as error:
        print(type(error)) #tipo depende do arquivo onde estamos
