class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <= len(self.balance) and account2 <= len(self.balance):
            if self.balance[account1 - 1] >= money and self.balance[account2 - 1] >= 0:
                self.balance[account1 - 1] -= money
                self.balance[account2 - 1] += money

                return True
            else:
                return False
        else:
            return False


    def deposit(self, account: int, money: int) -> bool:
        if account <= len(self.balance) and account >= 0:
            self.balance[account-1] += money
            return True
        else:
            return False
         

    def withdraw(self, account: int, money: int) -> bool:
        if account <= len(self.balance) and account >= 0:
        
            if self.balance[account-1] >= money:
                self.balance[account-1] -= money
                return True
            else:
                return False
        else:
            return False
            
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)