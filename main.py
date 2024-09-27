from abc import ABC, abstractmethod


# 1. Абстрактная фабрика напитков

class Drink(ABC):
    def __init__(self):
        self.base_price = 0
        self.name = "Напиток"

    @abstractmethod
    def get_base_ingredients(self):
        pass

    def get_price(self):
        return self.base_price

    def get_name(self):
        return self.name


class Coffee(Drink):
    def __init__(self):
        super().__init__()
        self.base_price = 30
        self.name = "Кофе"

    def get_base_ingredients(self):
        return "Вода, Кофейные зерна"


class Tea(Drink):
    def __init__(self):
        super().__init__()
        self.base_price = 25
        self.name = "Чай"

    def get_base_ingredients(self):
        return "Вода, чай"


class Cocktail(Drink):
    def __init__(self):
        super().__init__()
        self.base_price = 40
        self.name = "Безалкогольный коктейль"

    def get_base_ingredients(self):
        return "Газировка, Сироп"


class FreshJuice(Drink):
    def __init__(self):
        super().__init__()
        self.base_price = 50
        self.name = "Фруктовый фреш"

    def get_base_ingredients(self):
        return "Фрукты, Сок"


# 2. Декоратор для добавок
class DrinkDecorator(Drink):
    def __init__(self, drink):
        self.drink = drink

    def get_base_ingredients(self):
        return self.drink.get_base_ingredients()

    def get_price(self):
        return self.drink.get_price()

    def get_name(self):
        return self.drink.get_name()


class SugarDecorator(DrinkDecorator):
    def __init__(self, drink):
        super().__init__(drink)

    def get_price(self):
        return self.drink.get_price() + 10

    def get_name(self):
        return f"{self.drink.get_name()} с сахаром"


class MilkDecorator(DrinkDecorator):
    def __init__(self, drink):
        super().__init__(drink)

    def get_price(self):
        return self.drink.get_price() + 20

    def get_name(self):
        return f"{self.drink.get_name()} с молоком"


class CaramelDecorator(DrinkDecorator):
    def __init__(self, drink):
        super().__init__(drink)

    def get_price(self):
        return self.drink.get_price() + 25

    def get_name(self):
        return f"{self.drink.get_name()} с карамелью"


# 3. Фабричный метод для объёмов

class VolumeFactory(ABC):
    @abstractmethod
    def create_drink(self, drink: Drink):
        pass


class SmallVolumeFactory(VolumeFactory):
    def create_drink(self, drink: Drink):
        drink.base_price *= 1  # No change for small volume
        return drink


class MediumVolumeFactory(VolumeFactory):
    def create_drink(self, drink: Drink):
        drink.base_price *= 1.5
        return drink


class LargeVolumeFactory(VolumeFactory):
    def create_drink(self, drink: Drink):
        drink.base_price *= 2
        return drink


# Пример использования

def main():
    # Выбор напитка
    print("Выберите напиток: \n1 - Кофе, \n2 - Чай, \n3 - Коктейль, \n4 - Фреш")
    choice = input()

    if choice == "1":
        drink = Coffee()
    elif choice == "2":
        drink = Tea()
    elif choice == "3":
        drink = Cocktail()
    elif choice == "4":
        drink = FreshJuice()
    else:
        print("Неверный выбор")
        return

    # Выбор объема
    print("Выберите объем: \n1 - 0.4л, \n2 - 0.6л, \n3 - 0.8л")
    volume_choice = input()

    if volume_choice == "1":
        volume_factory = SmallVolumeFactory()
    elif volume_choice == "2":
        volume_factory = MediumVolumeFactory()
    elif volume_choice == "3":
        volume_factory = LargeVolumeFactory()
    else:
        print("Неверный выбор")
        return

    drink = volume_factory.create_drink(drink)

    # Добавки
    print("Хотите добавить сахар? (y/n)")
    sugarAnswer = input().lower()
    if sugarAnswer == 'y':
        drink = SugarDecorator(drink)
    elif sugarAnswer=='n':
        print("Сахар не добавляю")
    else:
        print("Ответьте да или нет пожайлуста")

    print("Хотите добавить молоко? (y/n)")
    if input().lower() == 'y':
        drink = MilkDecorator(drink)
    elif input().lower()=='n':
        print("Молоко не добавляю")
    else:
        print("Ответьте да или нет пожайлуста")

    print("Хотите добавить карамель? (y/n)")
    if input().lower() == 'y':
        drink = CaramelDecorator(drink)
    elif input().lower()=='n':
        print("Карамель не добавляю")

    # Итог
    print(f"Ваш заказ: {drink.get_name()}")
    print(f"Ингредиенты: {drink.get_base_ingredients()}")
    print(f"Цена: {drink.get_price()} руб.")


if __name__ == "__main__":
    main()
