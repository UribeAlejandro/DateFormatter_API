import pytest
from starlette.testclient import TestClient

from src.main import create_application


@pytest.fixture(scope="module")
def test_app():
    # set up
    app = create_application()
    with TestClient(app) as test_client:
        # testing
        yield test_client

    # tear down
