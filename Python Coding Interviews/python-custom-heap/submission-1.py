import heapq
from typing import List


def push_task(
    heap: List[tuple[int, str]],
    priority: int,
    task: str
) -> List[tuple[int, str]]:
    heapq.heapify(heap)
    heapq.heappush(heap, (priority, task))
    return heap


def get_next_task(heap: List[tuple[int, str]]) -> str:
    heapq.heapify(heap)
    priority, task = heap[0]
    return task


def pop_next_task(heap: List[tuple[int, str]]) -> str:
    heapq.heapify(heap)
    priority, task = heapq.heappop(heap)
    return task
