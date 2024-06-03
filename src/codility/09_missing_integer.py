from collections import Counter


def solution(numbers: list) -> int:
    counter = Counter(numbers)
    for int_item in range(1, 1_000_000):
        if not counter[int_item]:
            return int_item
    return -1


if __name__ == '__main__':
    res = solution(numbers=[-1, -3])
    print(res)
