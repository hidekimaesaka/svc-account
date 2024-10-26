from datetime import datetime

from app.models.svc_account import ServiceAccount


def test_service_account_model_can_be_instancied_with_a_dict(
        empty_svc_account: ServiceAccount):

    svc_account_dict = {
        'sa_name_1': 'svc_account_name',
        'sa_name_2': 'svc_account_name_2',
        'last_update_date': datetime.now(),
        'expiration_date': datetime.now()
    }

    new_svc_account = empty_svc_account(**svc_account_dict)

    assert new_svc_account.sa_name_1 == svc_account_dict.get('sa_name_1')
    assert new_svc_account.sa_name_2 == svc_account_dict.get('sa_name_2')
    assert new_svc_account.last_update_date == svc_account_dict.get(
        'last_update_date')
    assert new_svc_account.expiration_date == svc_account_dict.get(
        'expiration_date')
