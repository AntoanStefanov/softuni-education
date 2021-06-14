def generate_seq(n):
    seq = [0, 1]

    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def find_number(num, seq):
    if num in seq:
        return f"The number - {num} is at index {seq.index(num)}"
    return f"The number {num} is not in the sequence"