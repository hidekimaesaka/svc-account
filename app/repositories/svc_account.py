from app.models.svc_account import ServiceAccount

from app.adapters.db import Database

from sqlmodel import select


class SARepository:
    def __init__(self):
        self.database = Database()

    def persist_svc_account(self,
                            svc_account: ServiceAccount) -> ServiceAccount:
        with self.database.session as session:
            session.add(svc_account)
            session.commit()

            session.refresh(svc_account)
            return svc_account

    def get_all_svc_accounts(self) -> list[ServiceAccount]:
        with self.database.session as session:
            query = select(ServiceAccount)
            result = session.exec(query).all()

            return result

    def get_svc_account_by_id(self, id) -> ServiceAccount:
        with self.database.session as session:
            query = select(ServiceAccount).filter(ServiceAccount.id == id)
            result = session.exec(query).first()
            return result

    def update_svc_account(self,
                           svc_account: ServiceAccount) -> ServiceAccount:
        with self.database.session as session:
            session.merge(svc_account)
            session.commit()

            return svc_account

    def delete_svc_account(self, svc_account: ServiceAccount):
        with self.database.session as session:
            session.delete(svc_account)
            session.commit()

            return svc_account
