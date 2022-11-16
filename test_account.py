from account import *

class Test:

    def setup_method(self):
        self.p1 = Account('John')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'John'
        assert self.p1.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(-10) is False
        assert self.p1.get_balance() == 0

        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == 0

        assert self.p1.deposit(10) is True
        assert self.p1.get_balance() == 10

    def test_withdraw(self):
        self.p1.deposit(10)
        assert self.p1.withdraw(20) is False
        assert self.p1.get_balance() == 10

        assert self.p1.withdraw(5) is True
        assert self.p1.get_balance() == 5
        assert self.p1.withdraw(-10) is False
        assert self.p1.get_balance() == 5

        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == 5






