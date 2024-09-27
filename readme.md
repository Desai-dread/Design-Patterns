# Магомедомедов Гаджи 231-322
Расширенная кофейня

Для начала мы создаем класс добавляя ему абстрактный метод
используя библеотеку abc (Abstract Base Class)

```python
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
```

