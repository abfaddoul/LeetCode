from sortedcontainers import SortedDict
from typing import List


def create_sorted_dict(data: dict[int, str]) -> SortedDict:
    sdata = SortedDict()
    for key, value in data.items():
        sdata[key] = data[key]
    return sdata

def get_sorted_keys(data: dict[int, str]) -> List[int]:
    sdata = SortedDict()
    res = []
    for key, value in data.items():
        sdata[key] = data[key]
    for key, value in sdata.items():
        res.append(key)
    return res


def add_value(
    data: dict[int, str],
    key: int,
    value: str
) -> SortedDict:
    sdata = SortedDict()
    for k, val in data.items():
        sdata[k] = data[k]
    sdata[key] = value
    return sdata

# do not modify below this line
print(create_sorted_dict({3: "C", 1: "A", 2: "B"}))
print(create_sorted_dict({5: "E", 2: "B", 4: "D"}))

print(get_sorted_keys({3: "C", 1: "A", 2: "B"}))
print(get_sorted_keys({10: "J", 4: "D", 7: "G"}))

print(add_value({3: "C", 1: "A"}, 2, "B"))
print(add_value({5: "E", 2: "B"}, 3, "C"))
