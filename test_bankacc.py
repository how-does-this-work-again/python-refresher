import unittest
import bankacc

accountdeposittest = bankacc.Account("person", 100)
accountwithdrawtest = bankacc.Account("person", 100)
accountchecktest = bankacc.Account("person", 100)

class TestBank(unittest.TestCase):

    def test_deposit(self):
        self.assertEqual(accountdeposittest.deposit(10), "Deposited $10 to account #67(person). New balance: 110")
        self.assertEqual(accountdeposittest.deposit(0), "Deposited $0 to account #67(person). New balance: 110")
        self.assertEqual(accountdeposittest.deposit(100), "Deposited $100 to account #67(person). New balance: 210")

    def test_withdraw(self):
        self.assertEqual(accountwithdrawtest.withdraw(500), "ur poor lollll. Current balance: 100")
        self.assertEqual(accountwithdrawtest.withdraw(40), "Withdrew $40 from account #67(person). New balance: 60")
        self.assertEqual(accountwithdrawtest.withdraw(0), "Withdrew $0 from account #67(person). New balance: 60")

    def test_get_balance(self):
        self.assertEqual(accountchecktest.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()
