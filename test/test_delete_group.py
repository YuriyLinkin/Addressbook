import pytest
from models.group import Group

@pytest.fixture
def init_group(app):
   if not app.is_groups_present():
      test_group = Group(name_group='test')
      app.create_group(test_group)


def test_delete_group(app, init_login, init_group):
   app.open_page()
   app.delete_group_by_number(0)
   # TODO: Verify message
   assert "Group has been removed." in app.message()
   app.return_group_page()
   # TODO: Deletion group in list
