def create_dictionary(name: str, age: int) -> dict[str, int]:
    return {name: age}


def get_age(ages: dict[str, int], name: str) -> int:
    return ages[name]


def add_or_update(
    ages: dict[str, int],
    name: str,
    age: int
) -> dict[str, int]:
    ages[name] = age
    return ages


# do not modify below this line
print(create_dictionary("Alice", 25))
print(create_dictionary("Bob", 30))

print(get_age({"Alice": 25, "Bob": 30}, "Alice"))
print(get_age({"Alice": 25, "Bob": 30}, "Bob"))

print(add_or_update({"Alice": 25}, "Bob", 30))
print(add_or_update({"Alice": 25, "Bob": 30}, "Alice", 26))
