class Account:
    """
    A class representing details for an account object
    """

    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of an account object
        :param name: Person's account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Deposits money into account balance
        :param amount: Amount added
        :return: True if Deposit Successful or Else False
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Withdraws money from account balance
        :param amount: Amount removed
        :return: True is Withdraw is Successful or Else False
        """
        if amount <= 0:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to get an account's balance
        :return" Account's balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to get an account's name.
        :return: Account name.
        """
        return self.__account_name
