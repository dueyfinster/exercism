def classify(number):
    if number < 1:
        raise ValueError("Number must be greater than 1")

    factors = []
    for i in range(1, number):
        if number % i == 0:
            print("factor of " + str(number) + " is " + str(i))
            factors.append(i)

    total = sum(factors)

    if total == number:
        return "perfect"
    elif total > number:
        return "abundant"

    return "deficient"

