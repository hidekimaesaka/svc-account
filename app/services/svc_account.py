from app.models.svc_account import ServiceAccount

from app.repositories.svc_account import SARepository


class SAService:

    def __init__(self):
        self.repo = SARepository()

    def get_all(self):
        ...

    def add(self) -> ServiceAccount:
        ...

    def update(self):
        ...

    def delete(self):
        ...
