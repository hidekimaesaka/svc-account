from sqlmodel import SQLModel

from app.adapters.db import Database

from app.models.svc_account import ServiceAccount # noqa

db = Database()


if __name__ == '__main__':
    SQLModel.metadata.create_all(db.engine)
