from random import randint

from google.cloud import firestore

from account_service.domain.account import Account
from account_service.domain.errors import AccountNotFound


class FireStoreAccountRepository:
    def __init__(self, account_collection):
        db = firestore.Client()
        self.account_repo = db.collection(account_collection)

    def store(self, account):
        # don't use in production, simple id generator for demo purposes
        new_account_number = str(randint(10000000, 99999999))
        doc_ref = self.account_repo.document(new_account_number)

        doc_ref.set({"account_number": new_account_number,
                     u"account_status": account.account_status,
                     u"customer_id": account.customer_id})
        account.account_number = new_account_number

    def fetch_by_account_number(self, account_number):
        doc_ref = self.account_repo.document(account_number)
        doc = doc_ref.get()

        account_json = doc.to_dict()
        if account_json is not None:
            return Account(account_number=account_json["account_number"],
                           account_status=account_json["account_status"],
                           customer_id=account_json["customer_id"])
        else:
            raise AccountNotFound()
