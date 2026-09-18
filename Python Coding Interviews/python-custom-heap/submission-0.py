import heapq
from typing import List


def push_task(
    heap: List[tuple[int, str]],
    priority: int,
    task: str
) -> List[tuple[int, str]]:
    heapq.heappush(heap, (priority, task))
    return heap


def get_next_task(heap: List[tuple[int, str]]) -> str:
    priority, task = heap[0]
    return task


def pop_next_task(heap: List[tuple[int, str]]) -> str:
    priority, task = heapq.heappop(heap)
    return task
