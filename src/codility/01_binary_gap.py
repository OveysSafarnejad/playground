def solution(number: int):
    flag = False
    bin_gap = 0
    max_len = 0
    while number > 0:

        dev_res = number % 2
        number = number // 2
        if dev_res == 1 and not flag:
            flag = True
            continue
        if dev_res == 0 and flag:
            max_len += 1
            continue
        if dev_res == 1 and flag:
            bin_gap = max(bin_gap, max_len)
            max_len = 0
            continue

    return bin_gap


if __name__ == "__main__":
    binary_gap = solution(number=1041)
    print(binary_gap)
