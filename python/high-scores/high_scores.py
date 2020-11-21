def latest(scores):
    return scores[-1:][0]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
		length = len(scores) if len(scores) <= 3 else 3
		scores.sort(reverse = True)
		return scores[:length]
