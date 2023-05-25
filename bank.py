class Account:
    bank = "KCB"
    def __init__(self,account_number,deposits,withdrawals,loan_balance):
        self.account_number = account_number
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def check_Balance(self):
        self

    def balance(self):
        balance_amount = {self.deposit - self.withdraw}
        return f"{balance_amount}"
    def open_account(self):
        return f"John opened a {self.bank} account {self.account_number} and deposited {self.deposit}ksh"
    def deposit_amount(self):
        return f'{self.deposit} was deposited to this account number {self.account_number}'
    



class Account:
    bank = "KCB"

    def __init__(self, account_number):
        self.account_number = account_number
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def check_balance(self):
        balance_amount = sum(self.deposits) - sum(self.withdrawals)
        return f"Account balance: {balance_amount}"

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            transaction_type = transaction["narration"]
            amount = transaction["amount"]
            print(f"{transaction_type} - {amount}")

    def deposit(self, amount):
        transaction = {"amount": amount, "narration": "deposit"}
        self.deposits.append(transaction)

    def withdrawal(self, amount):
        transaction = {"amount": amount, "narration": "withdrawal"}
        self.withdrawals.append(transaction)

    # Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount
    def borrow_loan(self):
        self.sum_deposits=self.deposits*self.amount_deposited
        self.loan_requested=8000
        if self.loan_balance=0:
            return (f"customer can borrow")
        elif self.loan_requested>100 and 1/3*self.sum_deposits:
            return(f"customer can borrow")
        elif self.deposits>=10:
            return (f"customer can borrow")
        print self.loan_balance+=self.loan_requested
# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance
    def repay_loan(self):
        self.loan_repay=4000
        print(f"{self.loan_balance}-{self.loan_repay} is the
        current loan balance and the current account balance is
         {self.loan_repay}-{self.loan_balance}+{self.account_balance}")

    def transfer(self, amount, destination_account):
        if amount <= sum(self.deposits):
            self.withdrawal(amount)
            destination_account.deposit(amount)
            return "Transfer successful."
        else:
            return "Insufficient funds for transfer."
