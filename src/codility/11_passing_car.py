def solution(cars: list) -> int:
    total, counter = 0, 0
    for index in range(len(cars), 0, -1):
        if cars[index - 1] == 1:
            counter += 1
            continue
        else:
            total += counter
            if total > 1_000_000_000:
                return -1

    return total


if __name__ == '__main__':
    res = solution(cars=[0, 1, 0, 1, 1])
    print(res)
