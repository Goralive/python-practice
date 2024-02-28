def remove_duplicates(lst):
    return set(lst)

def count_vowels(text):
    vowels = ['A', 'a', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    counter = 0
    unique_vowel = set()

    for letter in text:
        if letter in vowels:
            counter += 1
            unique_vowel.add(letter)
    return counter, unique_vowel

def find_missing_ids(first_ids, second_ids):
    return list(set(first_ids) - set(second_ids))

print(count_vowels("Building a job-ready portfolio of coding projects does not happen overnight."))
