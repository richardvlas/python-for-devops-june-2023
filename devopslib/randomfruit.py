from random import choices


def fruit():
    fruits = ["apple", "banana", "cherry", "durian"]
    return choices(fruits)[0]

def meal(beverage):
    my_fruit = fruit()
    print(f"My fruit is {my_fruit}")
    if my_fruit == "cherry":
        complete_meal = f"Your meal is a {my_fruit} and {beverage}"
        return complete_meal
    return f"Your meal is a steak and {beverage}"

if __name__ == "__main__":
    print(fruit())
