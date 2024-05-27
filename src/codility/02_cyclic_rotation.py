def solution(num_array: list, rotations: int):
    if not num_array:
        return num_array

    arr_len = len(num_array)
    rotations = rotations % arr_len
    temp = num_array[arr_len - rotations: arr_len + 1]
    num_array[rotations:] = num_array[0:arr_len - rotations]
    num_array[0:rotations] = temp
    return num_array

    # or
    # return num_array[-rotations:] + num_array[:-rotations]


if __name__ == "__main__":
    res = solution(None, 3)
    print(res)
