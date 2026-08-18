class TestUser:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def get_info(self):
        return f"{self.username} (админ: {self.is_admin})"

user1 = TestUser("ivan", "12345")
user2 = TestUser("admin", "qwerty", True)

print(user1.username)    # чей логин? self'а user1 → ivan
print(user2.username)    # admin
print(user1.get_info())
print(user2.get_info())