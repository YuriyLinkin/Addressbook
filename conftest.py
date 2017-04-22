from web_api.addressbook_api import AddressBookAPI
import pytest

@pytest.fixture
def app():
    app = AddressBookAPI()
    app.login(password="secret", login="admin")
    yield app
    app.logout()
    app.destroy()