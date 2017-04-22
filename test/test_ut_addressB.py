

from models.group import Group

def test_ut_addressB(app):
    test_group = Group(name_group="groupAuto", header_group="groupAuto_header", footer_group="groupAuto_footer")
    app.open_homepage()
    app.login()
    app.open_page()
    app.create_group(test_group)
    # TODO: Verify message for group creation
    app.return_group_page()
    app.logout()







