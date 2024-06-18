def solution(numbers: list) -> int:
    numbers.sort()

    for index, item in enumerate(numbers):
        if index > len(numbers) - 3:
            break
        con_1 = item < numbers[index + 1] + numbers[index + 2]
        con_2 = numbers[index + 1] < item + numbers[index + 2]
        con_3 = numbers[index + 2] < item + numbers[index + 1]
        if con_1 and con_2 and con_3:
            return 1

    return 0


if __name__ == '__main__':
    print(solution([10, 2, 5, 1, 8, 20]))
    print(solution([10, 50, 5, 1]))
