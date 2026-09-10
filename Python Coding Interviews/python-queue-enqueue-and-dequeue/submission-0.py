from collections import deque


def enqueue_values(queue: deque[int], a: int, b: int) -> deque[int]:
    queue.append(a)
    queue.append(b)
    return queue


def dequeue_value(queue: deque[int]) -> int:
    return queue.popleft()


def dequeue_two(queue: deque[int]) -> deque[int]:
    queue.popleft()
    queue.popleft()
    return queue


# do not modify below this line
print(enqueue_values(deque([1, 2]), 3, 4))
print(enqueue_values(deque(), 10, 20))

print(dequeue_value(deque([1, 2, 3])))
print(dequeue_value(deque([10, 20, 30, 40])))

print(dequeue_two(deque([1, 2, 3, 4])))
print(dequeue_two(deque([5, 6, 7])))
