from tests.conftest import test_app  # noqa


def test_health(test_app):  # noqa
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Date Formatter!"}
