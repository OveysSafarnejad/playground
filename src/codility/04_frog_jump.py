from math import ceil


def solution(origin, destination, jump) -> int:
    if origin > destination or not jump > 0:
        raise ValueError
    distance = destination - origin
    min_jumps = ceil(distance / jump)

    return min_jumps


if __name__ == "__main__":
    res = solution(90, 90, 0.1)
    print(res)
