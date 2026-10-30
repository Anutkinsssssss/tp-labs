from abc import ABC, abstractmethod


# Общий класс для всех объектов игры
class GameObject:
    def __init__(self, object_id, name, x, y):
        self._id = object_id
        self._name = name
        self._x = x
        self._y = y

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getX(self):
        return self._x

    def getY(self):
        return self._y


# Юнит — игровой объект, у которого есть здоровье
class Unit(GameObject):
    def __init__(self, object_id, name, x, y, hp):
        super().__init__(object_id, name, x, y)
        self._hp = float(hp)

    def isAlive(self):
        return self._hp > 0

    def getHp(self):
        return self._hp

    def receiveDamage(self, damage):
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным")
        self._hp = max(0, self._hp - damage)


# Интерфейс для объектов, которые умеют атаковать
class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass


# Интерфейс для объектов, которые умеют передвигаться
class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass


# Лучник
class Archer(Unit, Attacker, Moveable):
    def attack(self, unit):
        if self.isAlive():
            unit.receiveDamage(20)

    def move(self, x, y):
        self._x = x
        self._y = y


# Постройка
class Building(GameObject):
    def __init__(self, object_id, name, x, y, built):
        super().__init__(object_id, name, x, y)
        self._built = built

    def isBuilt(self):
        return self._built

    def build(self):
        self._built = True


# Крепость
class Fort(Building, Attacker):
    def attack(self, unit):
        if self.isBuilt():
            unit.receiveDamage(30)


# Дом на колёсах
class MobileHouse(Building, Moveable):
    def move(self, x, y):
        if self.isBuilt():
            self._x = x
            self._y = y


# Проверка работы классов
if __name__ == "__main__":
    archer = Archer(1, "Лучник", 0, 0, 50)
    enemy = Unit(2, "Противник", 3, 4, 80)
    fort = Fort(3, "Крепость", 10, 10, True)
    house = MobileHouse(4, "Дом на колёсах", 5, 5, False)

    print("Объект:", archer.getId(), archer.getName())
    print("Координаты лучника:", archer.getX(), archer.getY())
    print("Лучник жив:", archer.isAlive())
    print("Здоровье противника:", enemy.getHp())

    archer.attack(enemy)
    print("После атаки лучника:", enemy.getHp())

    fort.attack(enemy)
    print("После атаки крепости:", enemy.getHp())

    archer.move(2, 3)
    print("Новые координаты лучника:", archer.getX(), archer.getY())

    print("Дом построен:", house.isBuilt())
    house.build()
    house.move(7, 8)
    print("Дом построен:", house.isBuilt())
    print("Новые координаты дома:", house.getX(), house.getY())