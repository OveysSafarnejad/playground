from collections import Counter


def solution(numbers: list) -> int:
    value_counts = Counter(numbers)
    left_counts = Counter()

    leader, leader_count = value_counts.most_common(1)[0]
    if leader_count <= (len(numbers) // 2):
        return 0

    left_size = 0
    right_size = len(numbers)
    equi_leader_count = 0

    for index, item in enumerate(numbers):
        left_size += 1
        right_size -= 1
        value_counts[item] -= 1
        if item in left_counts.keys():
            left_counts[item] += 1
        else:
            left_counts[item] = 1

        left_most_common = left_counts.most_common(1)[0]
        right_most_common = value_counts.most_common(1)[0]
        if left_most_common[1] > (left_size / 2) and right_most_common[1] > (right_size / 2) and \
                left_most_common[0] == right_most_common[0]:
            equi_leader_count += 1

    return equi_leader_count


def solution_2(numbers: list) -> int:
    value_counts = Counter(numbers)

    leader, leader_count = value_counts.most_common(1)[0]
    if leader_count <= (len(numbers) // 2):
        return 0

    left_size = 0
    right_size = len(numbers)
    left_leader_count = 0
    equi_leader_count = 0

    for index in range(len(numbers)):
        left_size += 1
        right_size -= 1
        if numbers[index] == leader:
            left_leader_count += 1
            leader_count -= 1

        if left_leader_count > left_size // 2 and leader_count > right_size // 2:
            equi_leader_count += 1

    return equi_leader_count


if __name__ == '__main__':
    # print(solution([4, 3, 4, 4, 4, 2]))
    print(solution_2([4, 3, 4, 4, 4, 2]))
