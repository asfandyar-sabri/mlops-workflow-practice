balance = 0;

class Wallet:
    def __init__(amount):
        balance = amount;
        
    def addAmount(amount):
        balance = balance + amount;
    
    def removeAmount(amount):
        balance = balance - amount;
        
    def getAmount():
        return balance;