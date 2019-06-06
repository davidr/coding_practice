import eulerlib

def compute(starting_number_limit: int = 1_000_000) -> int:
    largest_sequence = (-1, -1)
    for i in range(1, starting_number_limit):
        seq_len = len(eulerlib.collatz_sequence(i))
        if seq_len > largest_sequence[1]:
            largest_sequence = (i, seq_len)

    return largest_sequence[0]