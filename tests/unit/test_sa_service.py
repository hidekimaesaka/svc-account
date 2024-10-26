from app.models.svc_account import ServiceAccount

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


def test_if_delete_by_id_method_exists(sa_service: SAService):

    exists = sa_service.delete_by_id
    assert exists is not None


def test_if_get_all_svc_is_working_well(sa_service_populated: SAService):

    result = sa_service_populated.get_all()

    assert result is not None


def test_if_add_method_is_working_well(
        sa_service_populated: SAService, svc_account_dict: ServiceAccount):

    created = sa_service_populated.add(svc_account_dict)

    assert created is not None


def test_if_update_method_is_working_well(
        sa_service_populated: SAService):

    svc_to_update = sa_service_populated.get_all()[0]
    print(svc_to_update)
    svc_to_update['sa_name_1'] = 'Santos Futebol Clube'

    sa_service_populated.update(**svc_to_update)

    updated = sa_service_populated.get_all()[0]

    assert updated['sa_name_1'] == 'Santos Futebol Clube'


def test_if_delete_by_id_method_is_working_well(
        sa_service_populated: SAService):

    svc_to_delete = sa_service_populated.get_all()[0]

    deleted = sa_service_populated.delete_by_id(svc_to_delete.get('id'))

    assert deleted is True
