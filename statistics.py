from math import sqrt

# Replace with better, maybe not self-implemented versions when I get internet

def average(numbers):
    # maybe rewrite this to not materialize the array
    numbers = list(numbers)
    return float(sum(numbers)) / (len(numbers) or 1)


def median(numbers):
    # maybe rewrite this to not materialize the array
    if not numbers: return 0
    numbers = list(numbers)
    if len(numbers) % 2:
        return sorted(numbers)[len(numbers) / 2]

    srted = sorted(numbers)
    return average([srted[len(numbers) / 2 - 1], srted[len(numbers) / 2]])


def stdev(numbers):
    numbers = list(numbers)
    avg = average(numbers)
    return sqrt(average([(x - avg) * (x - avg) for x in numbers]))

