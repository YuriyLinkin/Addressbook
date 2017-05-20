from pytest_bdd import given, then, when, scenario
from models.group import Group

@scenario("group.feature", "Add new group")
def test_add_new_group():
    pass

@given("a group list")
def old_groups_list(db):
    return db.get_group_list()

@given("a group with <name>, <header>, <footer>")
def new_group(name, header, footer):
    return Group(name_group=name, header_group=header, footer_group=footer)

@when("I add a new group to the list")
def add_new_group(app, init_login, new_group):
    app.group.open_page()
    app.group.create_group(new_group)
    app.group.return_group_page()


@then("a new group list is equal to the old list with new group")
def verify_group_adding(db):
    new_groups_list = db.get_group_list()

    assert len(old_groups_list) + 1 == len(new_groups_list)
    old_groups_list.append(new_group)
    assert sorted(old_groups_list) == sorted(new_groups_list)