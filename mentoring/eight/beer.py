from mentoring.eight import is_adult

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
    {"customer": {"name": "Lenand", "surname": "Palmer"}},
]


    # return customer_list["customer"]["age"] >= 18


is_adult(customers)
# adults = list(filter(is_adult, customers))
# print(f"We should have 3 adults: {adults}")
