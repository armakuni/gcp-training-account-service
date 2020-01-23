from account_service import app
from account_service.infrastructure.firestore_account_repository import \
    FireStoreAccountRepository
from account_service.infrastructure.rest_customer_client import \
    RestCustomerClient
from account_service.settings import Config

if __name__ == "__main__":
    account_repository = FireStoreAccountRepository(Config.ACCOUNT_NAMESPACE)
    customer_client = RestCustomerClient(Config.CUSTOMER_SERVICE_URL)
    app.create(
        account_repository=account_repository,
        customer_client=customer_client
    ).run(host='0.0.0.0', port=Config.PORT)
