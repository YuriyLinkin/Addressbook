"""""
from models.group import Group1



def test_updated_AB_api(app_):
    upd_group = Group1(name="Yuriy_group", header="header_y_group", footer="footer_y_group")

    app_.open_groups()
    app_.choose_changing_group()
    app_.modify_group(upd_group)
    app_.updated_group()
    app_.return_group_page()

"""""
from models.group import Group
import pytest

# test_groups = [
#     Group(name_group="groupAuto", header_group="groupAuto_header", footer_group="groupAuto_footer"),
#     Group(name_group="123", header_group="098", footer_group="56577")
#     ]
#
# @pytest.mark.parametrize('index', [0, -1], ids=['first', 'last'])
# @pytest.mark.parametrize('test_group', test_groups, ids=['groups_with_letteres', 'groups_with_digit'])

def test_modify_by_number(app, init_login, init_group, test_groups, index):
   data_to_modification = test_groups #Croup(name_group='testNamE')
   app.group.open_page()
   old_groups = app.group.get_list()
   app.group.modify_by_number(index, data_to_modification)

   assert "Group record has been updated." in app.message()
   app.group.return_group_page()

   new_groups = app.group.get_list()
   if data_to_modification.name_group is not None:
       old_groups[index].name = data_to_modification.name_group

   assert len(old_groups) == len(new_groups)
   assert sorted(new_groups) == sorted(old_groups)

test_modify_by_number()