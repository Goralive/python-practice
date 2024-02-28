def calculate_total(items_purchased, grocery_list):
    item_prices = {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 1.21,
        "cheese": 3.50,
        "apples": 7.44,
        "bananas": 3.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 32.21,
        "cereal": 5.99,
    }

    # Don't touch above this line
    receipt = {}
    total = 0
    for item in items_purchased:
        if item in item_prices:
            total += item_prices[item]
            receipt[item] = item_prices[item]
        if item in grocery_list:
            grocery_list.remove(item)

    return grocery_list, receipt, total


calculate_total(
    ["milk", "eggs", "cheese", "apples", "bananas", "lettuce", "cereal"],
    [
        "milk",
        "oatmeal",
        "eggs",
        "cheese",
        "apples",
        "bananas",
        "carrots",
        "lettuce",
        "potatoes",
        "cereal",
        "chicken",
    ],
)
calculate_total(
    [
        "milk",
        "eggs",
        "bread",
        "cheese",
        "apples",
        "bananas",
        "carrots",
        "lettuce",
        "potatoes",
        "cereal",
    ],
    ["milk", "bread", "lettuce", "cereal"],
)
