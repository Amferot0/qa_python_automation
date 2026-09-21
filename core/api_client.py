import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")   # убираем лишний слэш на конце
        self.session = requests.Session() # объект, который помнит всё между запросами: cookies,
                                            # соединение и заголовки по умолчанию.
        self.session.headers.update({"User-Agent": "qa-automation-bot/1.0"})

    def set_token(self, token):
        self.session.headers["Authorization"] = f"Bearer {token}"

    def login(self, username, password):
        response = self.session.post(
            f"{self.base_url}/login",
            json={"username": username, "password": password},
        )
        self.set_token(response.json()["token"])
        return response

    def get_users(self):
        return self.session.get(f"{self.base_url}/users") # получаем список пользователей

    def get_user(self, user_id):
        return self.session.get(f"{self.base_url}/users/{user_id}") # получаем пользователя

    def get_post(self, post_id):
        return self.session.get(f"{self.base_url}/posts/{post_id}") # получаем пост

    def create_post(self, payload):
        return self.session.post(f"{self.base_url}/posts", json=payload) # добавляем пост

    def delete_post(self, post_id):
        return self.session.delete(f"{self.base_url}/posts/{post_id}") # удаляем пост

    # Если надо использовать f-строку
    # Правило: f-строка — это инструмент сборки ТЕКСТА (str). 
    # Используй её, когда результатом должна быть строка. 
    # Если программе нужна структура другого типа (dict, list, число) — собирай её напрямую.