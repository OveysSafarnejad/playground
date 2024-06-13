# Why Slices of Length 2 and 3?
#
# Short Slices: The smallest average of a slice will usually be found in shorter slices because:
# They include fewer numbers, so a single very low number has a larger impact on the average.
# Any longer slice can be broken down into smaller slices, and the average of a longer slice can't be smaller than
# the smallest average of its parts.

def solution(numbers):
    N = len(numbers)
    min_avg = float('inf')
    min_start_pos = 0

    for i in range(N - 1):
        # Check slices of length 2
        avg_2 = (numbers[i] + numbers[i + 1]) / 2.0
        if avg_2 < min_avg:
            min_avg = avg_2
            min_start_pos = i

        # Check slices of length 3, only if possible
        if i < N - 2:
            avg_3 = (numbers[i] + numbers[i + 1] + numbers[i + 2]) / 3.0
            if avg_3 < min_avg:
                min_avg = avg_3
                min_start_pos = i

    return min_start_pos


# Example usage
A = [4, 2, 2, 5, 1, 5, 8]
print(solution(A))  # Output: 1
