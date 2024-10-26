from sqlmodel import SQLModel

from pytest import fixture

from datetime import datetime

from app import create_app

from app.services.svc_account import SAService

from app.repositories.svc_account import SARepository

from app.adapters.db import Database

from app.models.svc_account import ServiceAccount


@fixture
def client_fixture():
    app = create_app()
    return app.test_client()


@fixture
def sa_service():
    service = SAService()
    return service


@fixture
def database():
    db = Database('sqlite:///:memory:')
    SQLModel.metadata.create_all(db.engine)
    return db


@fixture
def sa_repository(database) -> SARepository:
    repository = SARepository()
    repository.database = database
    return repository


@fixture
def empty_svc_account():
    return ServiceAccount


@fixture
def svc_account():
    sc = ServiceAccount()
    sc.sa_name_1 = 'svc_account_1'
    sc.sa_name_2 = 'svc_account_2'
    sc.last_update_date = datetime.now()
    sc.expiration_date = datetime.now()

    return sc


@fixture
def populated_repo(database):

    new_repo = SARepository()
    new_repo.database = database

    svc_account_1 = ServiceAccount()
    svc_account_1.sa_name_1 = 'svc_account_1'
    svc_account_1.sa_name_2 = 'svc_account_11'
    svc_account_1.last_update_date = datetime.now()
    svc_account_1.expiration_date = datetime.now()
    new_repo.persist_svc_account(svc_account_1)

    svc_account_2 = ServiceAccount()
    svc_account_2.sa_name_1 = 'svc_account_2'
    svc_account_2.sa_name_2 = 'svc_account_22'
    svc_account_2.last_update_date = datetime.now()
    svc_account_2.expiration_date = datetime.now()
    new_repo.persist_svc_account(svc_account_2)

    return new_repo


@fixture
def sa_service_populated(populated_repo):
    service = SAService()
    service.repo = populated_repo
    return service


@fixture
def svc_account_dict():

    svc_account = {
        "id": 1,
        "sa_name_1": "bababa",
        "sa_name_2": "bobobo",
        "last_update_date": datetime.now(),
        "expiration_date": datetime.now()
    }

    return svc_account
