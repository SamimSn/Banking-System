from datetime import date
import re
import sys


def main():
    Bank_Account_TUI.menu()


def deposit(acc, n):
    acc.deposit(n)

def calculate_years(acc):
    return date.today().year - acc._birth_date.year

def create_acc(id, name, birth_date, city, balance):
    return Bank_Account(id, name, birth_date, city, balance)


class Bank_Account:

    accounts = []
    id = 0

    def __init__(self, id, name: str, birth_date: date, city: str, balance: int):
        if 0 < balance < 50:
            raise Exception(f"\u001b[31m\n\n{name} --> (Account creation failed) Error: You need to open an account with at least 50$.\u001b[37m")
        if balance < 0:
            raise Exception(f"\u001b[31m\n\n{name} --> (Account creation failed) Error: You need to insert valid amount.\u001b[37m")
        self._balance = balance
        self._birth_date = birth_date
        self._name = name
        self._city = city
        if id == 0:
            self._id = Bank_Account.generate_id()
        else:
            self._id = id

    def __str__(self):
        return f"id: {self._id}, name: {self._name}, birth-date: {self._birth_date}, city: {self._city}, balance: {self._balance}$"

    @staticmethod
    def generate_id():
        Bank_Account.id += 1
        return Bank_Account.id

    @staticmethod
    def str_to_date(s: str):
        y,m,d = s.split("-")
        return date(int(y),int(m),int(d))

    @classmethod
    def calcPoints(cls):
        result = 0
        for account in cls.accounts:
            result += account.calcPoint()
        return result

    @classmethod
    def sort_by_balance(cls):
        for account in sorted(cls.accounts, key=lambda x : x._balance):
            print(account.__str__())

    @classmethod
    def sort_by_birth_date(cls):
        for account in sorted(cls.accounts, key=lambda x : x._birth_date):
            print(account.__str__())

    def calcPoint(self):
        return self._balance*2 - (date.today().year - self._birth_date.year)*(self._balance) / 100

    def deposit(self, n):
        if n > 0:
            self._balance += n
        else:
            raise Exception(f"\u001b[31m\n\n{self._name} --> Error: You need to insert valid amount.\u001b[37m")




class Bank_Account_TXT:

    @staticmethod
    def save():
        with open("bank_accounts.txt", "w") as file:
            for account in Bank_Account.accounts:
                file.write(f"{account.__str__()}\n")
        print("\u001b[32m\n\nSaved Successfully.\u001b[37m")

    @staticmethod
    def load():
        Bank_Account.accounts.clear()
        with open("bank_accounts.txt", "r") as file:
            for line in file:
                line = line[0:-2]
                attributes_datas = []
                for attribute in line.split(", "):
                    attributes_datas.append(attribute.split(": ")[1])
                id = int(attributes_datas[0])
                name = attributes_datas[1]
                birth_date = Bank_Account.str_to_date(attributes_datas[2])
                city = attributes_datas[3]
                balance = int(attributes_datas[4])
                Bank_Account.accounts.append(Bank_Account(id, name, birth_date ,city, balance))
                Bank_Account.id = id
        print("\u001b[32m\n\nLoaded Successfully.\u001b[37m")

class Bank_Account_TUI:

    @staticmethod
    def press_enter_to_continue():
        input("\n\n\n------Press Enter to continue")

    @staticmethod
    def display_menu():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("1-Print one account")
        print("2-Print all accounts")
        print("3-Create new account")
        print("4-Update an account")
        print("5-Delete an account")
        print("6-Sort accounts by balance")
        print("7-Sort accounts by birth date")
        print("8-Claculate point")
        print("9-Calculate points of all accounts")
        print("10-Deposit to an account")
        print("11-Save")
        print("12-Load")
        print("13-exit")

    @classmethod
    def menu(cls):
        cls.display_menu()
        answer = input("\n\n\nChoose option by number: ").strip()
        match answer:
            case "1":
                cls.print_account()
            case "2":
                cls.print_accounts()
            case "3":
                cls.create_account()
            case "4":
                cls.update_account()
            case "5":
                cls.delete_account()
            case "6":
                cls.sort_by_balance()
            case "7":
                cls.sort_by_birth_date()
            case "8":
                cls.calculate_point()
            case "9":
                cls.calculate_points()
            case "10":
                cls.deposit()
            case "11":
                if len(Bank_Account.accounts) != 0:
                    Bank_Account_TXT.save()
                else:
                    print("\u001b[31m\n\n <-----NO ACCOUNT!----->\u001b[37m")
            case "12":
                    try:
                        Bank_Account_TXT.load()
                    except ValueError:
                        pass
            case "13":
                sys.exit("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-----EXIT-----")
            case _:
                pass
        cls.press_enter_to_continue()
        cls.menu()

    @staticmethod
    def id_picker():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Available ids ->")
        ids = []
        for account in Bank_Account.accounts:
            ids.append(account._id)
            print(f"id: {account._id}")
        print("\n")
        while True:
            try:
                answer = int(input("ID: "))
                if answer not in ids:
                    continue
                return answer
            except:
                continue

    @classmethod
    def print_account(cls):
        if len(Bank_Account.accounts) != 0:
            id = cls.id_picker()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            for account in Bank_Account.accounts:
                if account._id == id:
                    print(account)
                    break
        else:
            print("\u001b[31m\n\n <-----NO ACCOUNT!----->\u001b[37m")


    @classmethod
    def print_accounts(cls):
        if len(Bank_Account.accounts) != 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            for account in Bank_Account.accounts:
                print(account)
        else:
            print("\u001b[31m\n\n <-----NO ACCOUNT!----->\u001b[37m")

    @classmethod
    def create_account(cls):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        try:
            cls.account_input()
        except:
            pass

    @classmethod
    def update_account(cls):
        if len(Bank_Account.accounts) != 0:
            id = cls.id_picker()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            for account in Bank_Account.accounts:
                if account._id == id:
                    account._name = input("Enter a new name: ")
                    account._city = input("Enter a new city: ")
                    print(f"\u001b[31m\n\nUpdated successfully\u001b[37m")
                    break
        else:
            print("\u001b[31m\n\n <-----NO ACCOUNT!----->\u001b[37m")


    @classmethod
    def delete_account(cls):
        if len(Bank_Account.accounts) != 0:
            id = cls.id_picker()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            for account in Bank_Account.accounts:
                if account._id == id:
                    Bank_Account.accounts.remove(account)
                    print(f"\u001b[31m\n\nRemoved {account._name} successfully\u001b[37m")
                    break
        else:
            print("\u001b[31m\n\n <-----NO ACCOUNT!----->\u001b[37m")


    @classmethod
    def sort_by_balance(cls):
        if len(Bank_Account.accounts) != 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Sorted accounts by (balance$) ->\n\n")
            Bank_Account.sort_by_balance()
        else:
            print("\u001b[31m\n\n <-----NO ACCOUNT!----->\u001b[37m")

    @classmethod
    def sort_by_birth_date(cls):
        if len(Bank_Account.accounts) != 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Sorted accounts by (birth date) ->\n\n")
            Bank_Account.sort_by_birth_date()
        else:
            print("\u001b[31m\n\n <-----NO ACCOUNT!----->\u001b[37m")

    @classmethod
    def calculate_point(cls):
        if len(Bank_Account.accounts) != 0:
            id = cls.id_picker()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            for account in Bank_Account.accounts:
                if account._id == id:
                    print(f"{account._name}'s point is -> {account.calcPoint()}")
                    break
        else:
            print("\u001b[31m\n\n <-----NO ACCOUNT!----->\u001b[37m")

    @classmethod
    def calculate_points(cls):
        if len(Bank_Account.accounts) != 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(f"Total points from all users is -> {Bank_Account.calcPoints()}")
        else:
            print("\u001b[31m\n\n <-----NO ACCOUNT!----->\u001b[37m")

    @classmethod
    def deposit(cls):
        if len(Bank_Account.accounts) != 0:
            id = cls.id_picker()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            while True:
                try:
                    n = int(input("How much to deposit: "))
                    break
                except:
                    continue
            for account in Bank_Account.accounts:
                if account._id == id:
                    try:
                        account.deposit(n)
                        print("\u001b[32m\n\nDeposited successfully \u001b[37m")
                    except Exception as e:
                        print(e)
                break
        else:
            print("\u001b[31m\n\n <-----NO ACCOUNT!----->\u001b[37m")

    @staticmethod
    def account_input():
        name = input("What's your name: ").strip()
        while True:
            birth_date = input("When's your birthday (YYYY-MM-DD): ").strip()
            if match := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", birth_date):
                y,m,d = match.groups()
                try:
                    birth_date = date(int(y), int(m), int(d))
                except:
                    continue
                break
            else:
                continue
        city = input("What city do you live in: ").strip()
        while True:
            try:
                balance = int(input("How much to deposit (consider --AT LEAST-- 50$): "))
                break
            except:
                continue
        try:
            acc = Bank_Account(0, name, birth_date, city, balance)
            Bank_Account.accounts.append(acc)
            print(f"\u001b[32m\n\n{name} --> Added to the system\u001b[37m")
        except Exception as e:
            print(e)
            raise Exception


if __name__ == "__main__":
    main()
