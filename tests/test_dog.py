from src.animals.dog import Dog

def test_dog_speak():
    dog = Dog("Buddy", 3)
    assert dog.speak() == "Woof!"
