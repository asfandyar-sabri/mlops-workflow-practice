
global balance = 0;
class Wallet:
    def __init__(self, amount):
        balance = amount;
        
    def addAmount(self, amount):
        balance = balance + amount;
    
    def removeAmount(self, amount):
        balance = balance - amount;
        
    def getAmount():
        return balance;
