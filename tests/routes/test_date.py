from datetime import datetime

import pytest

from tests.conftest import test_app  # noqa


@pytest.mark.run(order=1)
def test_counter_initial(test_app):  # noqa
    response = test_app.get("/date/counter")
    assert response.status_code == 200
    assert response.json()["count"] == 1


@pytest.mark.run(order=2)
def test_date(test_app):  # noqa
    now = datetime.now()
    response = test_app.post("/date", json={"timestamp": True})

    assert response.status_code == 200
    assert response.json()["date"] == now.strftime("%Y-%m-%d %H:%M:%S")

    response = test_app.post("/date", json={"timestamp": False})
    assert response.status_code == 200
    assert response.json()["date"] == now.strftime("%Y-%d-%m")


@pytest.mark.run(order=3)
def test_counter_after(test_app):  # noqa
    response = test_app.get("/date/counter")
    assert response.status_code == 200
    assert response.json()["count"] == 4
