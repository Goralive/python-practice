def get_odds_and_evens(numbers):
    num_evens = 0
    num_odds = 0

    for num in numbers:
        if num % 2 == 0:
            num_odds += 1
        else:
            num_evens += 1
