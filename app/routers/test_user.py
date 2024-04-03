from app.conftest import admin_test_user


def test_self_route(authenticated_test_client):
    response = authenticated_test_client.get("users/self")

    assert response.status_code == 200

    json_response = response.json()
    assert json_response["username"] == admin_test_user["username"]
    assert json_response["email"] == admin_test_user["email"]
    assert json_response["full_name"] == admin_test_user["full_name"]
    assert json_response["role"] == admin_test_user["role"]
    assert json_response["is_active"] == admin_test_user["is_active"]
