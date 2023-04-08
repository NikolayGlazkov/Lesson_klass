class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 1000, "bonus": 200}


class Position(Worker):
    # получения полного имени сотрудника и дохода с учетом премии (get_total_income).
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        money = self._income["wage"]+self._income["bonus"]
        return (f"прибыль равна :{money}")

    def __str__(self):
        return f"Сотрудник: {self.get_full_name()}, Должность: {self.position}, {self.get_total_income()}"


position = Position("Иван", "Иванович", "Дивопс")
print(position)