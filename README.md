# QA Python Automation 🚀

[![Tests](https://github.com/Amferot0/qa_python_automation/actions/workflows/tests.yml/badge.svg)](https://github.com/Amferot0/qa_python_automation/actions/workflows/tests.yml)

Учебный проект: путь от ручного QA к автоматизации на Python с использованием современных инструментов и лучших практик индустрии.

📊 **[Живой Allure-отчёт](https://amferot0.github.io/qa_python_automation/)** — автоматически обновляется при каждом push.

## 🛠 Стек технологий

- **Язык:** Python 3.14
- **Тестовый фреймворк:** pytest
- **API-тестирование:** requests (с Session и Bearer-токенами)
- **UI-тестирование:** Playwright (Chromium)
- **Паттерны:** Page Object Model, фикстуры pytest
- **Отчётность:** Allure Framework
- **CI/CD:** GitHub Actions с автодеплоем отчёта на GitHub Pages
- **Контроль версий:** Git, GitHub

## 📁 Структура проекта

qa_python_automation/
├── .github/workflows/ # GitHub Actions workflow
├── core/ # API-клиент и вспомогательный код
│ ├── init.py
│ └── api_client.py # ApiClient с Session и авторизацией
├── pages/ # Page Object Model для UI
│ ├── init.py
│ ├── login_page.py # Страница логина saucedemo.com
│ ├── products_page.py # Страница товаров
│ └── cart_page.py # Страница корзины
├── tests/ # Тестовая сюита
│ ├── conftest.py # Общие фикстуры (api, allure hooks)
│ ├── test_api.py # API-тесты (GET, DELETE)
│ ├── test_api_client.py # Юнит-тесты ApiClient
│ ├── test_api_posts.py # API-тесты POST/PUT
│ ├── test_param.py # Параметризованные тесты
│ ├── test_fixtures.py # Тесты работы фикстур
│ ├── test_ui_login.py # UI-тесты логина
│ └── test_ui_cart.py # UI-тесты корзины
├── lessons/ # Учебные скрипты по Python
├── .gitignore
├── pytest.ini # Конфигурация pytest
├── requirements.txt # Зависимости проекта
└── README.md

## 🚀 Запуск тестов

### Локально

```bash
# Установка зависимостей
pip install -r requirements.txt

# Установка браузера для Playwright
playwright install chromium

# Запуск всех тестов
pytest -v

# Запуск только API-тестов
pytest tests/test_api.py tests/test_api_posts.py -v

# Запуск только UI-тестов
pytest tests/test_ui_login.py tests/test_ui_cart.py -v

# Запуск UI-тестов с видимым браузером
pytest tests/test_ui_login.py -v --headed --slowmo=400

# Генерация Allure-отчёта локально
pytest --alluredir=allure-results
```
CI/CD
Тесты автоматически запускаются в GitHub Actions при каждом push в ветку main:
Устанавливается Python и зависимости из requirements.txt
Прогоняются все тесты (API + UI)
Генерируется Allure-отчёт
Отчёт деплоится на GitHub Pages
📊 Примеры тестов
API-тесты (jsonplaceholder.typicode.com)
GET /users — проверка списка пользователей (10 записей)
GET /users/9999 — негативный сценарий (404)
POST /posts — создание поста с валидацией ответа (201)
PUT /posts/1 — обновление существующего поста
DELETE /posts/1 — удаление ресурса
Параметризация: один тест прогоняется на 8 наборах данных (разные эндпоинты и статусы)
UI-тесты (saucedemo.com)
Успешный вход (standard_user) с проверкой заголовка страницы
Негативный вход (неверный пароль) с проверкой сообщения об ошибке
Добавление товара в корзину с проверкой счётчика
Проверка содержимого корзины — количество товаров
Юнит-тесты
Проверка установки Bearer-токена в заголовки ApiClient
🎓 Что изучено
Основы Python (ООП, работа с данными, функции)
HTTP и REST API (методы, статус-коды, заголовки, авторизация)
Библиотека requests (Session, Bearer-токены)
pytest (фикстуры, параметризация, хуки, conftest.py)
Playwright для UI-автоматизации (локация элементов, ожидания, web-first assertions)
Page Object Model (базовые страницы, композиция)
Git и GitHub (ветки, разрешение конфликтов, merge)
CI/CD на GitHub Actions (workflow, permissions, артефакты)
Allure Framework для отчётности (декораторы, шаги, severity)
Работа с flaky-тестами (явные ожидания, race conditions)
🔧 Борьба с нестабильными тестами
Проект включает примеры решения типичных проблем UI-тестирования:
Race conditions: явные ожидания через wait_for() и web-first assertions (expect)
Network timeouts: параметр wait_until="domcontentloaded" вместо load
Flaky-тесты: разделение E2E-сценариев на независимые проверки
📝 Автор
Maksim Dmitriev — Junior QA Automation Engineer
Проект постоянно развивается. Следите за обновлениями в [Actions](https://github.com/Amferot0/qa_python_automation/actions?spm=a2ty_o01.29997173.0.0.1358c921ZM8jNZ).