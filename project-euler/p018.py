# fmt: off
mini_triangle = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]


]


full_triangle = [
    [                            75],
    [                          95, 64],
    [                        17, 47, 82],
    [                      18, 35, 87, 10],
    [                    20,  4, 82, 47, 65],
    [                  19,  1, 23, 75,  3, 34],
    [                88,  2, 77, 73,  7, 63, 67],
    [              99, 65,  4, 28,  6, 16, 70, 92],
    [            41, 41, 26, 56, 83, 40, 80, 70, 33],
    [          41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [        53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [      70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [    91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [  63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]
# fmt: on


def compute(triangle=full_triangle) -> int:
    chain_computed_triangle = []

    for i in reversed(range(len(triangle) - 1)):
        row_max_chain = []
        for j, val in enumerate(triangle[i]):
            triangle[i][j] = val + max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]


def compute_incorrect(triangle=full_triangle) -> int:
    """ 
    Well, I thought this was the right way to do it at first glance, but obviously, it's dumb.

    This starts at the top and just continues the chain at the largest adjacent element of the
    next row down, which makes no sense.
    """

    idx, val = 0, triangle[0][0]
    running_value = val

    for row in range(1, len(triangle)):

        # look one to the left (if appropriate), same idx, and one to the right on this row from
        # where we found the highest value in the previous row
        cur_row_idx, cur_row_val = None, -1
        for i in range(idx - 1 if idx > 0 else 0, idx + 2):
            if triangle[row][i] > cur_row_val:
                cur_row_idx, cur_row_val = i, triangle[row][i]

        running_value += cur_row_val
        print(cur_row_val)
        idx, val = cur_row_idx, cur_row_val

    return running_value
