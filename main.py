from BankAccount import BankAccount 
def validation():
    try:
        user1 = BankAccount("Reem", 500)
        print("=== account Details ===")
        print(f"account Holder   {user1.get_account_holder()}")
        print(f"current Balance  {user1.get_balance()}")

        user1.deposit(2000)
        print(f"deposit completed successfully and here updated balance: {user1.get_balance()}")

        print("\nProcessing withdrawal of 5000...")
        user1.withdraw(5000)

    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    validation()