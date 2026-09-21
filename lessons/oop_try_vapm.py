class Vampire:
    def __init__(self, first_name, last_name, clan, generation, age_status):
        self.first_name = first_name
        self.last_name = last_name
        self.clan = clan
        self.generation = generation
        self.age_status = age_status

    def get_credentials(self):
        return {"first_name": self.first_name,
                "last_name": self.last_name, 
                "clan": self.clan, "generation": self.generation, 
                "age_status": self.age_status}

    def is_elder(self):
        return self.generation < 10 # возвращает булевое значение при условии

    def get_info(self):
        return f'{self.first_name} {self.last_name} | {self.clan} | {self.generation} поколение | {self.age_status}'

vampire1 = Vampire("Александр", "Строгалев", "Вентру", 12, "Неонат")
vampire2 = Vampire("Сьюзи", "Озепомон", "Носферату", 12, "Неонат")
vampire3 = Vampire("Скрипач", "неизвестно", "Тореадор", 9, "Служитель")

print(vampire3.get_info())
print(vampire3.is_elder())