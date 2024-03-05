def filter_messages(messages):
    dang = "dang"
    filtered = []
    words_counter = []
    for i in range(len(messages)):
        temp = messages[i].split()
        print(f"iterator {i} message {temp}")
        deleted = 0
        for j in range(len(temp)):
            if temp[j] == dang:
                deleted += 1
                temp.remove(j)
                words_counter.append(deleted)
            else:
                words_counter.append(deleted)

        filtered.append(" ".join(temp))
    return filtered, words_counter


filter_messages(
    [
        "well dang it",
        "dang the whole dang thing",
        "kill that knight, dang it",
        "get him!",
        "donkey kong",
        "oh come on, get them",
        "run away from the dang baddies",
    ]
)
