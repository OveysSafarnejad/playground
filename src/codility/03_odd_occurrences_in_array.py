def solution(numbers) -> int:
    arr_size = len(numbers) if numbers else None

    if arr_size == 0 or arr_size is None or max(numbers) > arr_size + 1:
        return 1

    values = {}
    for item in numbers:
        values[item] = True

    for num in range(1, arr_size + 2):
        if num not in values.keys():
            return num


if __name__ == "__main__":
    res = solution(numbers=[])
    print(res)
