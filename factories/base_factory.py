from abc import ABC, abstractmethod

class ComboFactory(ABC):
    @abstractmethod
    def create_burger(self):
        pass

    @abstractmethod
    def create_drink(self):
        pass

    @abstractmethod
    def create_side(self):
        pass

    @abstractmethod
    def create_dessert(self):
        pass

