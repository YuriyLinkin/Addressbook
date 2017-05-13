def test_delete_group(app, init_login, init_group, index):
   app.group.open_page()
   old_groups_list = app.group.get_list()
   app.group.delete_group_by_number(index)

   assert "Group has been removed." in app.message()
   app.group.return_group_page()
   # Verifying Deletion group in list
   new_groups_list = app.group.get_list()
   assert len(old_groups_list) - 1 == len(new_groups_list)
   old_groups_list.pop(index)
   assert old_groups_list == new_groups_list