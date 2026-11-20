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
│ └── products_page.py # Страница товаров
├── tests/ # Тестовая сюита
│ ├── conftest.py # Общие фикстуры (api, allure hooks)
│ ├── test_api.py # API-тесты (GET, POST, DELETE)
│ ├── test_api_client.py # Юнит-тесты ApiClient
│ ├── test_param.py # Параметризованные тесты
│ ├── test_fixtures.py # Тесты работы фикстур
│ └── test_ui_login.py # UI-тесты логина
├── lessons/ # Учебные скрипты по Python
├── .gitignore
├── pytest.ini # Конфигурация pytest
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
pytest tests/test_api.py -v

# Запуск UI-тестов с видимым браузером
pytest tests/test_ui_login.py -v --headed --slowmo=400

# Генерация Allure-отчёта локально
pytest --alluredir=allure-results

CI/CD
Тесты автоматически запускаются в GitHub Actions при каждом push в ветку main:
Устанавливается Python и зависимости
Прогоняются все тесты (API + UI)
Генерируется Allure-отчёт
Отчёт деплоится на GitHub Pages
📊 Примеры тестов
API-тесты (jsonplaceholder.typicode.com)
GET /users — проверка списка пользователей
POST /posts — создание поста с валидацией ответа
DELETE /posts/1 — удаление ресурса
Негативные сценарии (404)
Параметризованные тесты с разными наборами данных
UI-тесты (saucedemo.com)
Успешный вход (standard_user)
Негативный вход (неверный пароль)
Проверка отображения сообщений об ошибках
🎓 Что изучено
Основы Python (ООП, работа с данными, функции)
HTTP и REST API (методы, статус-коды, заголовки)
Библиотека requests (Session, авторизация через Bearer-токены)
pytest (фикстуры, параметризация, хуки)
Playwright для UI-автоматизации
Page Object Model
Git и GitHub (работа с ветками, разрешение конфликтов)
CI/CD на GitHub Actions
Allure Framework для отчётности
📝 Автор
Maksim Dmitriev — Junior QA Automation Engineer