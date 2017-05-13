import pymysql
from model.group import Group

class AddressbookDB:
    def __init__(self, host, port, user, password, db):
        self.connection = pymysql.connect(host=host, port=port, user=user, db=db, password=password, charset='utf8')

    def get_group_list(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT group_id, group_name, group_header, group_footer FROM group_list;"
            cursor.execute(sql)
            for row in cursor:
               group_list.append (Group (id=row[0], name_group=row[1], header_group=row[2], footer_group=row[3]))
        self.connection.commit()
        return group_list

    def destroy(self):
        self.connection.close()
