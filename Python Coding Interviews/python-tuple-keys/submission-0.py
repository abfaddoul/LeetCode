def create_point_map(
    x: int,
    y: int,
    value: str
) -> dict[tuple[int, int], str]:
    point = {}
    point[(x,y)] = value
    return point


def get_point(
    data: dict[tuple[int, int], str],
    x: int,
    y: int
) -> str:
    return data[(x,y)]


def add_point(
    data: dict[tuple[int, int], str],
    x: int,
    y: int,
    value: str
) -> dict[tuple[int, int], str]:
    data[(x,y)] = value
    return data


# do not modify below this line
print(create_point_map(1, 2, "A"))
print(create_point_map(3, 4, "B"))

print(get_point({(1, 2): "A", (3, 4): "B"}, 1, 2))
print(get_point({(1, 2): "A", (3, 4): "B"}, 3, 4))

print(add_point({(1, 2): "A"}, 3, 4, "B"))
print(add_point({(1, 2): "A"}, 1, 2, "C"))
