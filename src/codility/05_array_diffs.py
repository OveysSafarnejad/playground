def solution(numbers: list) -> int:
    left = 0
    right = sum(numbers)
    min_diff = None
    for p in range(1, len(numbers)):
        left += numbers[p-1]
        right -= numbers[p-1]
        current = abs(left - right)
        min_diff = min(current, min_diff) if min_diff is not None else current

    return min_diff


if __name__ == "__main__":
    res = solution(numbers=[1, 1, 1, 1])
    print(res)
