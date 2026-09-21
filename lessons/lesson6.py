import json

# Создай словарь product: "name": "Сумка", "price": "8999.99" (строкой!), "quantity": "35" (тоже строкой)
raw = '{"name": "Сумка", "price": "8999.99", "quantity": "35"}'
product = json.loads(raw)

# Сохрани его в файл product.json через json.dump (с indent=4 и encoding="utf-8")
with open("product.json", "w", encoding="utf-8") as f:
    json.dump(product, f, ensure_ascii=False, indent=4)

# Прочитай файл обратно в переменную loaded_product через json.load
with open("product.json", "r", encoding="utf-8") as f:
    loaded_product = json.load(f)

# Преобразуй price в float, quantity в int и выведи f-строкой: Сумка: 8999.99 руб., 35 шт
loaded_product["price"] = float(loaded_product["price"])
loaded_product["quantity"] = int(loaded_product["quantity"])
print(f'{loaded_product["name"]}: {loaded_product["price"]} руб., {loaded_product["quantity"]} шт') # правило переносимости: внутри f-строки используй другие кавычки или вынеси в переменную

# Дополнительно: создай строку raw_response = '{"status": 200, "ok": true}', 
# распарсь её json.loads и выведи type() результата. Посмотри, во что превратилось true
raw_response = '{"status": 200, "ok": true}'
response = json.loads(raw_response)
print(response["ok"], type(response["ok"])) # Печатаем значение ключа "ok", чтобы проверить именно True, а после получаем тип значения того же ключа