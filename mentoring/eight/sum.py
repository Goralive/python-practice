from functools import reduce
from beer import is_adult

customers = [
    {
        "customer": {
            "name": "Boris",
            "surname": "Francheski",
            "age": 18,
            "beer_bottles": 85,
        }
    },
    {"customer": {"name": "Bob", "surname": "", "age": 17}},
    {"customer": {"name": "Audrey", "surname": "Horne", "age": 21, "beer_bottles": 20}},
    {"customer": {"name": "Laura", "surname": "Palmer", "age": 33, "beer_bottles": 78}},
    {"customer": {"name": "Lenand", "surname": "Palmer", "age": 13}},
]


# Print the report on how many bottles of beer was drank and Name Surname of the winner. Using reduce
def __get_winner():
    # Get adults
    return reduce(
        lambda x, y: x
        if x["customer"]["beer_bottles"] > y["customer"]["beer_bottles"]
        else y,
        filter(is_adult, customers),
    )


def __summarize_amount_of_bottles():
    adults = (filter(is_adult, customers),)
    sum_list = [value for key, value in adults if key == "beer_bottles"]
    return reduce(lambda x, y: x + y, sum_list)


def report():
    sold_bottles = __summarize_amount_of_bottles()

    winner = __get_winner()["customer"]
    print(
        f'Winner is {winner["name"]} {winner["surname"]} with {winner["beer_bottles"]}'
    )
    print(f"Overall was sold: {sold_bottles}")


report()
