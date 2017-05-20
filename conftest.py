from web_api.addressbook_api import AddressBookAPI
from web_api.updated_AB_api import AddressBookAPI_2
import pytest
import json
import random
import os.path
from db_api.addressbook_orm import AddressbookORM
from data.test_groups import test_groups
from models.group import Group

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--config", action="store", default="config.json")


@pytest.fixture(scope="session")
def config(request):
    file_name = request.config.getoption("--config")
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name )
    with open (file_name) as f:
        return json.load(f)

@pytest.fixture(scope="session")
def app(request, config):
    browser = request.config.getoption("--browser")
    app = AddressBookAPI(browser=browser, base_url=config["web"]['base_url'])
    yield app
    app.destroy()

@pytest.fixture(scope="session")
def db (config):
    dbfixture = AddressbookORM(**config['db'])
    yield dbfixture
    #dbfixture.destroy()

@pytest.fixture(scope="session")
def init_login(app, config):
    app.session.login(login=config["web"]["login"], password=config["web"]["password"])
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



