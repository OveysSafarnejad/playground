def solution(sequence: str, left: list, right: list) -> list:
    seq_len = len(sequence)
    prefix_a = [0] * (seq_len + 1)
    prefix_c = [0] * (seq_len + 1)
    prefix_g = [0] * (seq_len + 1)
    prefix_t = [0] * (seq_len + 1)

    for index in range(seq_len):
        prefix_a[index + 1] = prefix_a[index] + (1 if sequence[index] == 'A' else 0)
        prefix_c[index + 1] = prefix_c[index] + (1 if sequence[index] == 'C' else 0)
        prefix_g[index + 1] = prefix_g[index] + (1 if sequence[index] == 'G' else 0)
        prefix_t[index + 1] = prefix_t[index] + (1 if sequence[index] == 'T' else 0)

    results = [0] * len(left)
    for index in range(len(left)):
        start = left[index]
        end = right[index] + 1

        # Check for 'a' in range:
        if prefix_a[end] - prefix_a[start] > 0:
            results[index] = 1
            continue
        # Check for 'c' in range:
        if prefix_c[end] - prefix_c[start] > 0:
            results[index] = 2
            continue
        # Check for 'g' in range:
        if prefix_g[end] - prefix_g[start] > 0:
            results[index] = 3
            continue
        # Check for 't' in range:
        if prefix_t[end] - prefix_t[start] > 0:
            results[index] = 4
            continue

    return results


if __name__ == '__main__':
    print(solution(sequence='CAGCCTA', left=[2, 5, 0], right=[4, 5, 6]))