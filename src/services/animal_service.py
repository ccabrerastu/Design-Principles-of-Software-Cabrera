from typing import List
from src.animals.animal import Animal

class AnimalService:
    def __init__(self, animals: List[Animal]):
        self._animals = animals

    def introduce_animals(self) -> List[str]:
        return [f"{animal.get_info()} says {animal.speak()}" for animal in self._animals]
