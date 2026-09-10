#create the account class
class Account:
#set the account number and starting balance
    def __init__(self, account_number,  balance=0):
        self.account_number = account_number
        self.balance= balance
#add money to the account   
    def deposit(self, amount):
        
            self.balance += amount
            print(f"${amount} deposited .new balance: ${self.balance}") 
 #Remove money from the account       
    def withdraw(self, amount):
        if  amount > self.balance:
            print("Insufficient Funds!")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}") 
        
            
#display the current account balance
    def display_balance(self):
        print(f"Account{self.account_number} balance: ${self.balance}")

#creat the customer class 
class Customer:
#set the customer's name and account    
    def __init__(self, name, account):
         self.name = name
         self.account = account
#display the customer's information
    def display_customer_info(self):
        print(f"Customer Name: {self.name}")
        self.account.display_balance()     
#creat the transaction class
class Transaction:
#set the account,amount,and transaction type
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.process_transaction()
#process the transaction        
    def process_transaction(self):
        if self.transaction_type == "Deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "Withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type!")
            
#creat an account with an account number and starting balance
account1=Account(account_number=101, balance=100) 
customer1=Customer(name="Alice", account=account1)

#display the customer's account information
customer1.display_customer_info()

#creat a deposit transaction of $50
transaction1=Transaction(account1,50,"Deposit")
#creat a withdrawal transaction of $30
transaction2=Transaction(account1,30,"Withdraw")

#Display the customer's updated account information
customer1.display_customer_info()