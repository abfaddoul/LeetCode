from collections import deque


def add_both_ends(
    q: deque[int],
    left: int,
    right: int
) -> deque[int]:
    q.append(right)
    q.appendleft(left)
    return q


def remove_both_ends(q: deque[int]) -> deque[int]:
    q.pop()
    q.popleft()
    return q


def pop_ends(q: deque[int]) -> tuple[int, int]:
    return (q.popleft(), q.pop())


# do not modify below this line
print(add_both_ends(deque([2, 3]), 1, 4))
print(add_both_ends(deque(), 10, 20))

print(remove_both_ends(deque([1, 2, 3, 4])))
print(remove_both_ends(deque([5, 6, 7])))

print(pop_ends(deque([1, 2, 3, 4])))
print(pop_ends(deque([10, 20, 30])))
