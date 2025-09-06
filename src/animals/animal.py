from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @abstractmethod
    def speak(self) -> str:
        pass

    def get_info(self) -> str:
        return f"{self._name}, {self._age} years old"
