class Account:
    """
    A class representing details for an account object
    """
    def __init__(self, name):
    """
    Constructor to create initial state of an account object
    :param account_name: Person's account name
    :param account_balance: Person's account balance
    """
        self.__account_name = Account('001-John')
        self.__account_balance = 0
    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True
    def withdraw(self, amount):
        if amount <= 0:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance += amount
            return True
    def get_balance(self):
        """

        Method to get an account's balance
        :return" Account's balance
        """
        return self.__account_balance
    def get_name(self):
        """

        Method to get an account's name.
        :return: Account name.
        """
        return self.__account_name


