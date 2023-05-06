class Account:
    bank = "KCB"
    def __init__(self,account_number,withdraw,deposit):
        self.account_number = account_number
        self.withdraw = withdraw
        self.deposit = deposit
    def balance(self):
        balance_amount = {self.deposit - self.withdraw}
        return f"{balance_amount}"
    def open_account(self):
        return f"John opened a {self.bank} account {self.account_number} and deposited {self.deposit}ksh"
    def deposit_amount(self):
        return f'{self.deposit} was deposited to this account number {self.account_number}'