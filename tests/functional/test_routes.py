from flask.testing import FlaskClient


def test_route_health_exists(client_fixture: FlaskClient):
    route = '/health'
    res = client_fixture.get(route)
    assert res.status_code != 404


def test_svc_account_get_all_route_exists(client_fixture: FlaskClient):
    route = '/svc_accounts'
    res = client_fixture.get(route)

    assert res.status_code != 404


def test_svc_account_create_route_exists(client_fixture: FlaskClient):
    route = '/svc_accounts/new'
    res = client_fixture.get(route)

    assert res.status_code != 404


def test_svc_account_update_route_exists(client_fixture: FlaskClient):
    route = '/svc_accounts/update'
    res = client_fixture.get(route)

    assert res.status_code != 404


def test_svc_account_delete_route_exists(client_fixture: FlaskClient):
    route = '/svc_accounts/delete'
    res = client_fixture.get(route)

    assert res.status_code != 404
