def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Two strands must be equal len")
    return sum(x != y for x,y in zip(strand_a, strand_b))
