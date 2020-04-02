def combine(n, k):
    combinations = []
    generate(0, n, k, [], combinations)
    return combinations

def generate(num, n, k, current, combinations):
    if len(current) == k:
        combinations.append(current)
        return
    for i in range(num + 1, n + 1):
        generate(i, n, k, current + [i], combinations)
