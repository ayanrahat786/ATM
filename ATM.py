class ATM:
    def __init__(self, total_money, banknotes):
        self.total_money = total_money
        self.banknotes = banknotes

    def withdraw_money(self, user, amount):
        if amount > user.balance:
            return "Declined: Insufficient funds."
        
        amount = amount//2

        remaining_amount = amount
        withdrawal_banknotes = []


        notes = sorted(self.banknotes.keys(), reverse=True)

        for banknote in notes:
            while remaining_amount >= banknote and self.banknotes[banknote] > 0:
                withdrawal_banknotes.append(banknote)
                remaining_amount -= banknote
                self.banknotes[banknote] -= 1

        

        
        for i in notes:
            if i<=amount:
                notes.remove(i)
                break

        remaining_amount = amount

        for banknote in notes:
            while remaining_amount >= banknote and self.banknotes[banknote] > 0:
                withdrawal_banknotes.append(banknote)
                remaining_amount -= banknote
                self.banknotes[banknote] -= 1


        if remaining_amount > 0:
            return "Declined: ATM does not have enough banknotes to fulfill the withdrawal."

        user.balance -= 2*amount
        return withdrawal_banknotes


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


def main():
    
    total_money = 0
    banknotes = {500:5, 200: 10, 100: 20, 50: 30, 20: 10, 10:10}
    for key, value in banknotes.items():
        total_money += key * value


    atm = ATM(total_money, banknotes)

    user2 = User("Bob", 10000)

    while True:
        print("\n===== Welcome to the ATM =====")
        print("Select an option:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")

        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            print(f"Balance for {user2.name}: {user2.balance}€")

        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            withdrawal_result = atm.withdraw_money(user2, amount)
            if isinstance(withdrawal_result, str):
                print(withdrawal_result)
            else:
                print(f"Withdrawn banknotes: {withdrawal_result}")

        elif choice == 3:
            print("Exiting the ATM. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
