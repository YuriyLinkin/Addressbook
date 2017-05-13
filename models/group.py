
class Group:
    def __init__(self, name_group=None, header_group=None, footer_group=None, id=None):
        self.name_group = name_group
        self.header_group = header_group
        self.footer_group = footer_group
        self.id = id

    def __repr__(self):
        return "id: {}, name:{}, header: {}, footer: {}".format(self.id, self.name_group, self.header_group, self.footer_group)

    def __eq__(self, other):
        if self.id is None or other.id is None:
            return self.name_group == other.name_group
        else:
            return self.id == other.id and self.name_group == other.name_group

    def __lt__(self, other):
        if self.id is None:
            return False
        elif other.id is None:
            return True
        else:
            return self.id < other.id

class Group1:
    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer

