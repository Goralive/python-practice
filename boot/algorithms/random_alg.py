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


def median_followers(nums):
    print(nums)
    if nums is None:
        return None
    if nums <= 0:
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
    for list in list_of_lists:
        for name in list:
            if target_name == name:
                count += 1
    return count


def remove_duplicates(nums):
    pass
