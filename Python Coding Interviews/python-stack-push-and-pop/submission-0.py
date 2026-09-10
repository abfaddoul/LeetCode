from typing import List


def push_values(stack: List[int], a: int, b: int) -> List[int]:
    stack.append(a)
    stack.append(b)
    return stack


def pop_value(stack: List[int]) -> int:
    return stack.pop()


def pop_two(stack: List[int]) -> List[int]:
    stack.pop()
    stack.pop()
    return stack


# do not modify below this line
print(push_values([1, 2], 3, 4))
print(push_values([], 10, 20))

print(pop_value([1, 2, 3]))
print(pop_value([10, 20, 30, 40]))

print(pop_two([1, 2, 3, 4]))
print(pop_two([5, 6, 7]))
