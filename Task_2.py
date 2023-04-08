class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        # масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см
        self.asphalt_weight_per_square_meter = 25
        self.asphalt_thickness = 0.05 #толщина слоя по умолчанию

    def asphalt_mass_calculation(self):
        asphalt_mass = (self._length * self._width *
                        (self.asphalt_weight_per_square_meter*self.asphalt_thickness))
        print(
            f"Для покрытиявсего дорожного полотна, необхадимо,{asphalt_mass/1000} тонн асфальта.")


person = Road(20, 5000)
# задаем новое значение толщины
person.asphalt_thickness = float(input("введите толщину в метрах :"))
person.asphalt_mass_calculation()
