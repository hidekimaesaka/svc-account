from app.models.svc_account import ServiceAccount

from app.repositories.svc_account import SARepository


class SAService:

    def __init__(self):
        self.repo = SARepository()

    def get_all(self):
        svc_accounts = []
        query = self.repo.get_all_svc_accounts()

        for sa in query:
            svc_account = {}
            svc_account['id'] = sa.id
            svc_account['sa_name_1'] = sa.sa_name_1
            svc_account['sa_name_2'] = sa.sa_name_2
            svc_account['last_update_date'] = sa.last_update_date
            svc_account['expiration_date'] = sa.expiration_date
            svc_accounts.append(svc_account)

        return svc_accounts

    def add(self, data) -> ServiceAccount:
        new_svc_account = ServiceAccount(**data)
        created = self.repo.persist_svc_account(new_svc_account)

        return created

    def update(self, **data):
        sa_to_update = self.repo.get_svc_account_by_id(data.get('id'))
        for key, value in data.items():
            if key and value:
                sa_to_update.__setattr__(key, value)
        updated = self.repo.update_svc_account(sa_to_update)

        return updated

    def delete_by_id(self, id):
        svc_to_delete = self.repo.get_svc_account_by_id(id)
        deleted = self.repo.delete_svc_account(svc_to_delete)

        return deleted
