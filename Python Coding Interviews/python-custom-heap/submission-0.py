import heapq
from typing import List


def push_task(
    heap: List[tuple[int, str]],
    priority: int,
    task: str
) -> List[tuple[int, str]]:
    pass


def get_next_task(heap: List[tuple[int, str]]) -> str:
    pass


def pop_next_task(heap: List[tuple[int, str]]) -> str:
    pass


# do not modify below this line
print(push_task([(2, "B"), (5, "E")], 1, "A"))
print(push_task([(3, "C"), (7, "G")], 2, "B"))

print(get_next_task([(1, "A"), (3, "C"), (2, "B")]))
print(get_next_task([(2, "B"), (5, "E"), (4, "D")]))

print(pop_next_task([(1, "A"), (3, "C"), (2, "B")]))
print(pop_next_task([(2, "B"), (5, "E"), (4, "D")]))
