# QA Python Automation 🚀

[![Tests](https://github.com/Amferot0/qa_python_automation/actions/workflows/tests.yml/badge.svg)](https://github.com/Amferot0/qa_python_automation/actions/workflows/tests.yml)

Учебный проект: путь от ручного QA к автоматизации на Python.

📊 **[Живой Allure-отчёт](https://amferot0.github.io/qa_python_automation/)** — обновляется при каждом push.

## 🛠 Стек технологий

- **Язык:** Python 3.14
- **Тестирование API:** requests (Session, Bearer-токены)
- **Тестирование UI:** Playwright (Chromium)
- **Фреймворк:** pytest (фикстуры, параметризация, хуки)
- **Паттерны:** Page Object Model
- **Отчётность:** Allure
- **CI/CD:** GitHub Actions + GitHub Pages

## 📁 Структура проекта

**qa_python_automation/**
- `.github/workflows/` — конфигурация CI/CD
- `core/` — API-клиент и вспомогательный код
  - `api_client.py` — ApiClient с Session и авторизацией
- `pages/` — Page Object Model для UI
  - `login_page.py` — страница логина saucedemo.com
  - `products_page.py` — страница товаров
  - `cart_page.py` — страница корзины
- `tests/` — тестовая сюита (21 тест)
  - `conftest.py` — общие фикстуры и allure-хуки
  - `test_api.py`, `test_api_posts.py` — API-тесты
  - `test_api_client.py` — юнит-тесты клиента
  - `test_param.py`, `test_fixtures.py` — параметризация и фикстуры
  - `test_ui_login.py`, `test_ui_cart.py` — UI-тесты
- `lessons/` — учебные скрипты по Python
- `pytest.ini`, `requirements.txt`, `.gitignore`

## 🚀 Запуск тестов

```bash
pip install -r requirements.txt
playwright install chromium
pytest -v
```

UI-тесты с видимым браузером:

```bash
pytest tests/test_ui_login.py -v --headed --slowmo=400
```

## 📊 Что покрыто тестами

### API (jsonplaceholder.typicode.com)
- GET /users — список пользователей (10 записей)
- GET /users/9999 — негативный сценарий (404)
- POST /posts — создание поста (201)
- PUT /posts/1 — обновление поста
- DELETE /posts/1 — удаление ресурса
- Параметризация: один тест на 8 наборах данных

### UI (saucedemo.com)
- Успешный вход (standard_user) с проверкой страницы товаров
- Негативный вход (неверный пароль) с проверкой сообщения об ошибке
- Добавление товара в корзину с проверкой счётчика
- Проверка содержимого корзины

### Юнит-тесты
- Установка Bearer-токена в заголовки ApiClient

## 🎓 Освоенные темы

- Python: ООП, коллекции, функции, исключения
- HTTP/REST: методы, статус-коды, заголовки, авторизация
- pytest: фикстуры, conftest.py, параметризация, хуки
- Playwright: локаторы, ожидания, web-first assertions
- Page Object Model: классы страниц, композиция
- Git: ветки, merge, разрешение конфликтов
- CI/CD: GitHub Actions, permissions, артефакты, GitHub Pages
- Allure: декораторы, шаги, severity
- Нестабильные тесты: race conditions, явные ожидания

## 📝 Автор

**Maksim Dmitriev** — Junior QA Automation Engineer