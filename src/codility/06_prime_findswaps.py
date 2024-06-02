def solution(numbers_a: list, numbers_b: list) -> tuple:
    sum_a = sum(numbers_a)
    sum_b = sum(numbers_b)
    diff = sum_a - sum_b
    if diff % 2 == 1:
        return None, None

    if diff < 0:
        dict_b = {k: v for v, k in enumerate(numbers_b)}
        for item in numbers_a:
            target = item - diff//2
            if target in dict_b:
                return item, target
    else:
        dict_a = {k: v for v, k in enumerate(numbers_a)}
        for item in numbers_b:
            target = diff//2 + item
            if target in dict_a:
                return item, target


if __name__ == '__main__':
    res = solution(
        numbers_a=[1, 2, 6],
        numbers_b=[4, 3, 0]

    )
    print(res)
