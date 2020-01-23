class Account:
    def __init__(self, account_status, customer_id, account_number=None):
        self.account_number = account_number
        self.account_status = account_status
        self.customer_id = customer_id
