

class Account:      #При всички случаи работи 100/100 в Judge, но ако се добавят долните коментари като част от инстанцията САМО тука не работи!
    def __init__(self, owner:str, amount:int = 0): #, transactions:list = []
        self.owner = owner
        self.amount = amount
        self._transactions = [] #transactions
    
    @property
    def balance(self):
        '''sum = self.amount
        for _transaction in self._transactions:
            sum  += _transaction
            
        return sum'''
        return sum(self._transactions) + self.amount
    
    def handle_transaction(self, transaction_amount):
        if self.balance+transaction_amount<0:
            raise ValueError("sorry cannot go in debt!")
        
        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"
    
    def add_transaction(self, amount):
        if type(amount)!=int:
            raise ValueError("please use int for amount")
        
        if self.balance+amount<0:
            raise ValueError("sorry cannot go in debt!")
        
        
        return self.handle_transaction(amount)
        
        
    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"
    
    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"
    
    def __len__(self):
        return len(self._transactions)
    
    def __getitem__(self, index:int):
        return self._transactions[index]
    
    def __reversed__(self):
        return reversed(self._transactions)
    
    def __gt__(self, other:object):     # >
        return self.balance>other.balance
    
    def __le__(self, other):       # <=
        return self.balance<=other.balance
    
    def __eq__(self, other):    # ==
        return self.balance==other.balance
    
    def __add__(self, new):   # +
        new_transactions = self._transactions + new._transactions
        starting_amount = self.amount + new.amount
        
        #return Account(f"{self.owner}&{new.owner}", starting_amount, new_transactions)
        new_account =  Account(f"{self.owner}&{new.owner}", starting_amount)
        new_account._transactions = new_transactions
        
        return new_account
    
acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
