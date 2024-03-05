def number_sum(n):
    sum = 0
    for i in range(1, n + 1):
        print(i)
        sum += i
    print(sum)


def find_min(nums):
    min = float("inf")
    for num in nums:
        if min > num:
            min = num
    return min


def remove_nonints(nums):
    ints = []
    for num in nums:
        if type(num) == int:
            ints.append(num)
    return ints


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


def area_sum(rectangles):
    rectangles_sum = 0
    for rectangle in rectangles:
        height = rectangle["height"]
        width = rectangle["width"]
        print(f"{rectangle['height']} + {rectangle['width']}")
        rectangles_sum += height * width
    print(f"Sum is -> {rectangles_sum}")
    return rectangles_sum


def fizzbuzz(start, end):
    for i in range(start, end):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)


def divide_list(nums, divisor):
    divided_nums = []
    for num in nums:
        divided_nums.append(num / divisor)
    return divided_nums


divide_list([6, 8, 10], 2)
# [3.0, 4.0, 5.0]


def join_strings(strings):
    phrase = ""
    size = len(strings)
    for i in range(size):
        phrase += strings[i]
        if i != size - 1:
            phrase += ","
    return phrase


join_strings(["hello", "my", "friend"])
# 'hello,my,friend'
