import uuid


class Client:
    def __init__(self, name, company, email, position, uid=None):
        self.uid = uid or str(uuid.uuid4())
        self.name = name
        self.company = company
        self.email = email
        self.position = position

    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ["uid", "name", "company", "email", "position"]
