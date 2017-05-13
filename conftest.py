from web_api.addressbook_api import AddressBookAPI
from web_api.updated_AB_api import AddressBookAPI_2
import pytest
import random
from data.test_groups import test_groups
from models.group import Group


@pytest.fixture(scope="session")
def app():
    app = AddressBookAPI()
    yield app
    app.destroy()

@pytest.fixture(scope="session")
def init_login(app):
    app.session.login(password="secret", login="admin")
    yield
    app.session.logout()

@pytest.fixture(scope="session")
def app_():
    app_var = AddressBookAPI_2()
    app_var.login(password="secret", login="admin")
    yield app_var
    app_.logout()

@pytest.fixture
def init_group(app, init_login):
   if not app.group.is_groups_present():
      test_group = Group(name_group='test')
      app.group.create_group(test_group)


@pytest.fixture(params=[0,'random',-1], ids=['first', 'random шт the middle', 'last'])
def index( request, app):
   if request.param == 'random':
      return random.randrange(1, app.group.count()-1)
   return request.param


@pytest.fixture(params=test_groups, ids=[repr(g) for g in test_groups])
def test_group(request):
    return request.param



