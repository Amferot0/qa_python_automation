# Создай класс TestUser с атрибутами username, 
# password и is_admin (сделай is_admin=False значением по умолчанию, 
# как мы делали с параметрами функций)
class TestUser:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

# Добавь метод get_credentials(), который возвращает словарь {"username": ..., "password": ...}
# — такие словари потом пойдут в тело API-запроса на логин
    def get_credentials(self):
        return {"username": self.username, "password": self.password} # Запомни разделение: f-строка — для сообщений человеку, словарь — для данных программе.

# Добавь метод get_role(), который возвращает строку "admin", если is_admin истинно, иначе "user"
    def get_role(self):
        if self.is_admin:
            return "admin"
        else:
            return "user"

# Создай два объекта: обычного пользователя и админа (второму передай is_admin=True)
user1 = TestUser("Паша", "qwerty")
user2 = TestUser("Одмэн", "p1a2s3s4w5o6r7d8", True)

# Выведи для каждого: username и роль через get_role()
print(user1.username, user1.get_role())
print(user2.username, user2.get_role())

print(user1.get_credentials())