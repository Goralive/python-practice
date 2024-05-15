import functools


def get_median_font_size(font_sizes):
    length = len(font_sizes)
    if length < 1:
        return None
    sorted_fonts = sorted(font_sizes)
    if length % 2 == 0:
        middle = length // 2
        one = sorted_fonts[middle - 1]
        two = sorted_fonts[middle]
        return (one + two) / 2
    else:
        return sorted_fonts[length // 2]


def remove_invalid_lines(document):
    document_array = document.split("\n")
    change_lines = list(filter(elem, document_array))
    print(change_lines)


def elem(word):
    return word.startswith("-")


def accumulate(doc, sentence):
    return ".".join(doc, sentence)


def accumulate_first_sentences(sentences, n):
    if n < 1:
        return ""
    result = functools.reduce(accumulate, sentences)
    print(f"Result is -> {result}")
    return result
