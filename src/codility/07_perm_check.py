from collections import Counter


def solution(numbers) -> int:
    c = Counter(numbers)

    if max(c.keys()) > len(numbers):
        return 0
    if max(c.values()) > 1:
        return 0

    return 1


if __name__ == '__main__':
    res = solution(numbers=[1, 2, 2, 5])
    print(res)
