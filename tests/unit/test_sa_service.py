from app.services.svc_account import SAService


def test_if_get_all_method_exists(sa_service: SAService):

    exists = sa_service.get_all
    assert exists is not None


def test_if_add_method_exists(sa_service: SAService):

    exists = sa_service.add
    assert exists is not None


def test_if_update_method_exists(sa_service: SAService):

    exists = sa_service.update
    assert exists is not None


def test_if_delete_method_exists(sa_service: SAService):

    exists = sa_service.delete
    assert exists is not None
