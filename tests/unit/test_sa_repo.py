from app.repositories.svc_account import SARepository

from app.models.svc_account import ServiceAccount


def test_if_persist_svc_account_method_exists(
        sa_repository: SARepository):
    exists = sa_repository.persist_svc_account
    assert exists is not None


def test_if_get_all_svc_accounts_method_exists(sa_repository: SARepository):
    exists = sa_repository.get_all_svc_accounts
    assert exists is not None


def test_if_persist_svc_account_method_is_persisting_data(
        sa_repository: SARepository, svc_account: ServiceAccount):

    result = sa_repository.persist_svc_account(svc_account)

    assert result is not None
    assert result.id == 1


def test_if_update_svc_account_method_exists(sa_repository: SARepository):
    exists = sa_repository.update_svc_account
    assert exists is not None


def test_if_delete_svc_account_method_exists(sa_repository: SARepository):
    exists = sa_repository.delete_svc_account
    assert exists is not None


def test_if_get_all_svc_accounts_method_is_returning_array(
        sa_repository: SARepository, svc_account: ServiceAccount):

    data = sa_repository.get_all_svc_accounts()

    assert data is not None


def test_if_get_all_svc_accounts_method_is_returning_array_of_obj(
        populated_repo: SARepository):

    data = populated_repo.get_all_svc_accounts()

    assert data is not None


def test_if_get_by_id_method_is_working_well(populated_repo: SARepository):
    # considering data populated on conftest.py
    # see the fixtures

    svc_1 = populated_repo.get_svc_account_by_id(1)

    assert svc_1.sa_name_1 == 'svc_account_1'


def test_if_update_method_is_updating(populated_repo: SARepository):

    svc_1 = populated_repo.get_svc_account_by_id(1)
    svc_1.sa_name_1 = 'svc_santos_fc_1'
    updated_svc = populated_repo.update_svc_account(svc_1)

    assert updated_svc.sa_name_1 == 'svc_santos_fc_1'


def test_if_delete_method_is_deleting(populated_repo: SARepository):

    svc_1 = populated_repo.get_svc_account_by_id(1)
    populated_repo.delete_svc_account(svc_1)

    svc_1_exists = populated_repo.get_svc_account_by_id(1)

    assert svc_1_exists is None
