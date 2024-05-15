import logging

logging.basicConfig(
    filename="logfile.log",  # name of the log file that is created
    filemode="w",  # file mode used when opening the log file
    format="%(asctime)s %(levelname)-8s %(message)s",  # string patterns that defines the output format
    level=logging.DEBUG,  # this sets the lowest log level that should be logged
)


def add(num_one, num_two):
    logging.error("Number one %i adding to number two %i", num_one, num_two)

    return num_one + num_two


def divide(num_one, num_two):
    return num_one / num_two


add(5, 10)
