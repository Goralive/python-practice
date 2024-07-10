import math


def find_minimum(nums):
    if len(nums) == 0:
        return None
    minimum = float("inf")
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum


def sum(nums):
    sum_all = 0
    for num in nums:
        sum_all += num
    return sum_all


def average_followers(nums):
    followers = len(nums)
    sum_all = 0
    if followers <= 0:
        return None
    for num in nums:
        sum_all += num

    return sum_all / followers


def median_followers(nums):
    print(nums)
    if nums is None:
        return None
    if len(nums) <= 0:
        return None
    sorted = nums.sort()
    middle = len(nums) / 2
    if middle % 2 != 0:
        middle -= middle - 0.5
    return sorted[middle]


def get_follower_prediction(follower_count: int, influencer_type: str, num_months: int):
    multiple = 2
    if influencer_type == "fitness":
        multiple = 4
    if influencer_type == "cosmetic":
        multiple = 3
    return follower_count * (multiple**num_months)


def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers, 2)


def num_possible_orders(num_posts):
    fact = 1
    for i in range(num_posts):
        fact *= i
    return fact


def decayed_followers(intl_followers, fraction_lost_daily, days):
    retention_rate = 1 - fraction_lost_daily
    return int(intl_followers * (retention_rate**days))


def log_scale(data, base):
    result = []
    for num in data:
        log = math.log(num, base)
        result.append(log)
    return result


# O(N)
def find_max(nums):
    max_value = -float("inf")
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value


# O(N**2)
def does_name_exist(first_names, last_names, full_name):
    for name in first_names:
        for surname in last_names:
            if f"{name} {surname}" == full_name:
                return True
    return False


# O(NM)
def get_avg_brand_followers(all_handles, brand_name):
    brand_counter = 0
    influencers_counter = 0
    for handles_list in all_handles:
        influencers_counter += 1
        for item in handles_list:
            if brand_name in item:
                brand_counter += 1

    return brand_counter / influencers_counter


all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"],
]
brand_name = "cosmo"

print(get_avg_brand_followers(all_handles, brand_name))


# 0(1)
def find_last_name(names_dict, first_name):
    try:
        return names_dict[first_name]
    except KeyError:
        return None


# log(n)
def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


def count_names(list_of_lists, target_name):
    count = 0
    for items_list in list_of_lists:
        for name in items_list:
            if target_name == name:
                count += 1
    return count


def remove_duplicates(nums):
    unique_list = []
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line


def vanity(influencer):
    return influencer.num_bio_links * 5 + influencer.num_selfies


def vanity_sort(influencers):
    sorted(influencers, key=vanity)


def bubble_sort(nums):
    swapping = True
    end = len(nums)

    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return nums


def merge_sort(nums):
    arr_length = len(nums)
    if arr_length < 2:
        return nums
    middle = arr_length // 2
    first_half = nums[:middle]
    second_half = nums[middle:]

    left_side = merge_sort(first_half)
    right_side = merge_sort(second_half)
    return merge(left_side, right_side)


def merge(first, second):
    finished_list = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            finished_list.append(first[i])
            i += 1
        else:
            finished_list.append(second[j])
            j += 1
    while i < len(first):
        finished_list.append(first[i])
        i += 1
    while j < len(second):
        finished_list.append(second[j])
        j += 1
    return finished_list


def insertion_sort(nums):
    if len(nums) < 1:
        return nums
    for i in range(len(nums)):
        j = i
        while 0 < j and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums


def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i


def selection_sort(nums):
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums


def fib(n):
    if n <= 1:
        return n
    current = 0
    parent = 1
    grandparent = 0
    for _ in range(0, n - 1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current


def power_set(input_set):
    if not input_set:
        return [[]]
    power_list = []
    first = input_set[0]
    remaining = input_set[1:]
    remaining_subsets = power_set(remaining)
    for elem in remaining_subsets:
        power_list.append([first] + elem)
        power_list.append(elem)
    return power_list


def exponential_growth(n, factor, days):
    growth = [n]
    for i in range(days):
        growth.append(growth[-1] * factor)
    return growth


def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1

    while time_left >= time_in_country:
        time_left -= time_in_country
        time_in_country *= factor
        count += 1
    return count


def regenerate(current_health, max_health, enemy_distance):
    while current_health != max_health:
        if enemy_distance <= 3:
            break
        print(f"Enemy distance is {enemy_distance}")
        current_health += 1
        enemy_distance -= 2
    return current_health
