class BankAccount:

  def __init__(self,account_holder ,initial_balance=0) -> None :
    self.__account_holder=account_holder
    self.__balance=initial_balance

  def deposit(self,amount):
   if amount>0:
    self.__balance+=amount
    return self.__balance
   else:
     print("invaild amount")
    

  def withdraw (self,amount):   
      if amount>self.__balance:
        raise Exception("Insufficient funds")
      if amount <= 0:
        raise ValueError("Amount must be positive")
      self.__balance-=amount
      return self.__balance

   
  def get_balance(self):
     return self.__balance
   
  def get_account_holder(self):
     return self.__account_holder
  









