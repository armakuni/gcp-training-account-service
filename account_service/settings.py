import os


class Config:
    PORT = int(os.getenv('PORT', 5001))
    ACCOUNT_NAMESPACE = os.getenv('ACCOUNT_NAMESPACE', 'accounts')
    CUSTOMER_SERVICE_URL = os.getenv('CUSTOMER_SERVICE_URL',
                                     'http://localhost:5000')
