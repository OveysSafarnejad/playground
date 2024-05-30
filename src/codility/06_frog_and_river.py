def solution(leaves: list, river_width: int) -> int:
    if len(leaves) < river_width:
        return -1

    frog_path = {loc: False for loc in range(1, river_width + 1)}
    for time, loc in enumerate(leaves):
        if loc in frog_path:
            del frog_path[loc]

        if time + 1 >= river_width and len(frog_path.keys()) == 0:
            return time

    return -1


if __name__ == '__main__':
    res = solution(leaves=[1, 2, 3, 4, 5, 3, 4, 4], river_width=5)
    print(res)
