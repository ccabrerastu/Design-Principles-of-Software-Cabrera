from src.animals.cat import Cat

def test_cat_speak():
    cat = Cat("Luna", 2)
    assert cat.speak() == "Meow!"
