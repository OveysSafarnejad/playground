def solution(counter_size: int, operations: list) -> list:
    counters = [0] * counter_size
    applied = -1
    max_counter = 0
    for operation in operations:
        if operation > counter_size:
            applied = max_counter
            continue

        counters[operation - 1] = max(counters[operation - 1], applied) + 1
        max_counter = max(max_counter, counters[operation - 1])

    for index, item in enumerate(counters):
        if applied > item:
            counters[index] = applied
    return counters


if __name__ == '__main__':
    res = solution(counter_size=5, operations=[3, 4, 4, 6, 1, 4, 4])
    print(res)
