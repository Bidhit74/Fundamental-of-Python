# ✅ Bank Management System
# 🔹 Features: Create account, Deposit money, Withdraw money, Show account details

class BankAccount:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance  # Encapsulation

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited.")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn.")
        else:
            print("Insufficient balance")

    def show_info(self):
        print("\n📄 Account Information:")
        print(f"👤 Name: {self.name}")
        print(f"🏦 Account No: {self.acc_no}")
        print(f"💰 Balance: ₹{self.__balance}\n")

# --- Main Menu ---
print("🔐 Welcome to Bidhit Bank !!")
name = input("Enter your name: ")
acc_no = input("Enter your account number: ")
account = BankAccount(name, acc_no)

while True:
    print("\n📋 Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Account Info")
    print("4. Exit")

    choice = input("Choose an option (1–4): ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: ₹"))
        account.deposit(amt)

    elif choice == "2":
        amt = float(input("Enter amount to withdraw: ₹"))
        account.withdraw(amt)

    elif choice == "3":
        account.show_info()

    elif choice == "4":
        print("Thank you for using Bidhit Bank! 👋")
        break

    else:
        print("❌ Invalid choice. Please try again.")


# ✅ OOPs Used:
# Class/Object – BankAccount
# Encapsulation – __balance is private
# Methods – deposit, withdraw, info
# 📌 Features Covered:
# ✅ OOPs concepts: class, object, encapsulation
# ✅ User input-based interaction
# ✅ Repeated menu using while True loop
# ✅ Helpful messages + emoji UI 💡