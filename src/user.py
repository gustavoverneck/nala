class User:
    def __init__(self, id=None, name=None, email=None, password=None, role="user"):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return (f"User(id={self.id}, username='{self.name}', email='{self.email}', "
                f"role='{self.role}')")

    def update_email(self, new_email: str):
        self.email = new_email

    def update_password(self, new_password: str):
        self.password = new_password

    def update_role(self, new_role: str):
        self.role = new_role