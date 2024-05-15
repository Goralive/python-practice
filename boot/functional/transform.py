def doc_format_checker_and_converter(conversion_function, valid_formats):
    def inner_converter(filename, content):
        if filename.split(".")[-1] in valid_formats:
            print("HELLO!!!")
        else:
            ValueError("Invalid file format")


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
