class Worker:
    def __init__(self, name, surname, position):
        self._validate_input(name, surname, position)  # вызов метода для проверки входных параметров
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 1000, "bonus": 200}

    def _validate_input(self, name, surname, position):
        if not isinstance(name, str):
            raise ValueError("вы ввели не строку")
        if not isinstance(surname, str):
            raise ValueError("вы ввели не строку")
        if not isinstance(position, str):
            raise ValueError("вы ввели не строку")


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

# пример неправильного ввода переменной (тип переменной - int)
try:
    position2 = Position(123123, "Иванович", "Дивопс")
except ValueError as e:
    print(e)
