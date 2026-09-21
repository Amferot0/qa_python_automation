# Создай список «сырых» данных: raw_codes = ["200", "404", "abc", "500"].
# В цикле for попробуй преобразовать каждый элемент в int и вывести Код 200 обработан.
# При поимке ValueError выведи ⚠️ 'abc' — не число, пропускаем
# Главное требование: после «abc» цикл должен дойти до «500» и обработать его. Программа не должна упасть.
raw_codes = ["200", "404", "abc", "500"]

for raw_code in raw_codes:
    try:
        code = int(raw_code)
        print(f"Код {code} обработан")
    except ValueError:
        print(f"⚠️ {raw_code} — не число, пропускаем")

# Создай словарь user_profile = {"name": "qa_engineer", "role": "manual"}.
# Попробуй достать значение ключа "salary", 
# а при KeyError выведи Ключа 'salary' в профиле нет
user_profile = {
    "name": "qa_engineer",
    "role": "manual",
}

try:
    user_profile["salary"]
except KeyError:
    print("Ключа 'salary' в профиле нет")