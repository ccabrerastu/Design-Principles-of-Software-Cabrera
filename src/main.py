from src.animals.dog import Dog
from src.animals.cat import Cat
from src.services.animal_service import AnimalService

def main():
    # Crear animales
    dog = Dog("Buddy", 3)
    cat = Cat("Luna", 2)

    # Pasar los animales al servicio
    service = AnimalService([dog, cat])

    # Obtener las presentaciones
    introductions = service.introduce_animals()

    # Mostrar en consola
    for intro in introductions:
        print(intro)

if __name__ == "__main__":
    main()
