import unittest
import bankacc

testBank = bankacc.Bank([])
accountDepositTest = testBank.addAccount("deposit test", 100)
accountWithdrawTest = testBank.addAccount("withdraw test", 100)
accountCheckTest = testBank.addAccount("check test", 100)

class TestBank(unittest.TestCase):
    def test_deposit(self):
        self.assertEqual(accountDepositTest.deposit(10), 110)
        self.assertEqual(accountDepositTest.deposit(0), 110)
        self.assertEqual(accountDepositTest.deposit(100), 210)
        self.assertEqual(accountDepositTest.deposit(-10), False)
        self.assertEqual(accountDepositTest.deposit("string"), False)

    def test_withdraw(self):
        self.assertEqual(accountWithdrawTest.withdraw(500), False)
        self.assertEqual(accountWithdrawTest.withdraw(40), 60)
        self.assertEqual(accountWithdrawTest.withdraw(0), 60)
        self.assertEqual(accountWithdrawTest.withdraw(-10), False)
        self.assertEqual(accountWithdrawTest.withdraw("string"), False)

    def test_get_balance(self):
        self.assertEqual(accountCheckTest.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()
