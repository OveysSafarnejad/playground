# You are given a non-empty, zero-indexed array A of n (1 < n < 100 000) integers
# a0, a1 -> an−1 (0 < a(i) < 1 000). This array represents number of mushrooms growing on the
# consecutive spots along a road. You are also given integers k and m (0 < k, m < n).
# A mushroom picker is at spot number k on the road and should perform m moves. In
# one move she moves to an adjacent spot. She collects all the mushrooms growing on spots
# she visits. The goal is to calculate the maximum number of mushrooms that the mushroom
# picker can collect in m moves.


def solution(mushrooms: list, pos_start: int, moves: int) -> int:
    max_end = min(pos_start + moves, len(mushrooms) - 1)

    prev_left = max(pos_start - moves, 0)
    right = pos_start
    left = prev_left

    curr_sum = sum(mushrooms[left:right + 1])
    max_sum = curr_sum

    while right < max_end and left <= pos_start:
        right += 1
        #  right first  approach
        right_diff = right - pos_start
        # the reason for 2* is that we have to go to the right and return back
        left_1 = max(pos_start - (moves - 2 * right_diff), 0)

        #  left first approach
        # here we don't have a 2* because we go to the right just once after returning from the back
        left_diff = (moves - right_diff) // 2
        left_2 = max(pos_start - left_diff, 0)

        #  calculate correct left
        left = min(left_1, left_2)

        curr_sum += mushrooms[right]

        if left > prev_left:
            dif_start = left - prev_left
            curr_sum = curr_sum - mushrooms[prev_left]
            if dif_start == 2:
                curr_sum = curr_sum - mushrooms[prev_left + 1]

        max_sum = max(curr_sum, max_sum)
        prev_left = left

    return max_sum


if __name__ == '__main__':
    res = solution([1, 2, 3, 4, 5], 2, 3)
    print(res)
