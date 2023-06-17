from random import choices


def fruit():
    fruits = ["apple", "banana", "cherry", "durian"]
    return choices(fruits)[0]


if __name__ == "__main__":
    print(fruit())
