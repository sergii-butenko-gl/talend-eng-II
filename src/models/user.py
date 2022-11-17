class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def create_in_database(self):
        print("USER CREATED IN DATABASE")
        return True

    def remove_from_database(self):
        print("USER REMOVED FROM DATABASE")
        return True
