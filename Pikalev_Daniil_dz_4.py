class Car:


    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.color} {self.name} поехал(а)!'


    def stop(self):
        return f'{self.color} {self.name} остановился(ась)!'


    def turn_left(self):
        return f'{self.color} {self.name} повернул(а) налево'


    def turn_right(self):
        return f'{self.color} {self.name} повернул(а) направо'


    def show_speed(self):
        return f'{self.speed} км/ч - текущая скорость'


class TownCar(Car):


    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        print(f'Текщая скорость {self.name} равняется {self.speed} км/ч')
        if self.speed > 60:
            return f'Скорость превышена'
        else:
            return f'Скорость в пределах допустимой'


class WorkCar(Car):


    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        print(f'Текщая скорость {self.name} равняется {self.speed} км/ч')
        if self.speed > 40:
            return f'Скорость превышена'
        else:
            return f'Скорость в пределах допустимой'


class SportCar(Car):


    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):


    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


ford = TownCar(70, 'black', 'Ford', False)
kamaz = WorkCar(38, 'white', 'KAMAZ', False)
ferrari = SportCar(120, 'red', 'Ferrari', False)
lada = PoliceCar(80, 'blue', 'Lada', True)

print(f'{ford.show_speed()}\n')
print(f'Когда {ford.turn_left()} за ним погнался полицейская {lada.name}\n')
print(f'Лада это полицеская машина? {lada.is_police}\n')
print(f'{kamaz.show_speed()}\n')
print(f'Какая красивая {ferrari.color} {ferrari.name}')