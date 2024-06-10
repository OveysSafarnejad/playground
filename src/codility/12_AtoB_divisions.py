def solution(start: int, end: int, divisor: int) -> int:
    if start == end:
        return int(start % divisor == 0)
    rem = start % divisor
    if rem != 0:
        start += divisor - rem

    end -= end % divisor

    if start <= end:
        return ((end - start) // divisor) + 1
    return 0


if __name__ == '__main__':
    print(solution(start=6, end=11, divisor=2))
    print(solution(start=11, end=345, divisor=17))
    print(solution(20, 20, 5))
    print(solution(10, 10, 5))
    print(solution(11, 13, 2))

