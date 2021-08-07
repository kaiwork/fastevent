from main import app
from main import get_current_user
from fastapi.testclient import TestClient


class AuthBypasser: 
    """AuthBypasser Class for testing."""

    def __init__(self):
        """Testing data to show is authenticated."""
        self.user_id = "is authenticated"


def auth_bypass():
    """
    Mock auth bypasser to be passed into the authenticated test.

    Returns:
        AuthBypasser: A simple class to send back the required attribute
    """
    return AuthBypasser()


client = TestClient(app)


def test_get_current_user_not_authenticated():
    """
    Test unauthenticated request to get user data.

    Returns:
        an unauthenticated response
    """
    response = client.get("/user/")
    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}


def test_get_current_user_authenticated():
    """
    Test authenticated request to get user data.

    Returns:
        a authenticated response which is a mock of the user data sent back
    """
    app.dependency_overrides[get_current_user] = auth_bypass
    response = client.get("/user/")
    assert response.status_code == 200
    assert response.json() == {'id': 'is authenticated'}
