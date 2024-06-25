import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-1s %(message)s",  # string patterns that defines the output format
    level=logging.INFO,  # this sets the lowest log level that should be logged
)


# %(asctime)s: This placeholder is replaced by the time when the log message is created, formatted as specified by the asctime format in the formatter.
#
# %(levelname)-8s: This placeholder is replaced by the log level name (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL) left-aligned in an 8-character wide field. The -8s specifies that the field should be at least 8 characters wide, and if the level name is shorter than 8 characters, it will be padded with spaces.
#
# %(message)s: This placeholder is replaced by the actual log message that you provide when logging.


def add(num_one, num_two):
    logging.debug("Number one %i adding to number two %i", num_one, num_two)
    logging.info("Number one %i adding to number two %i", num_one, num_two)
    logging.warning("Number one %i adding to number two %i", num_one, num_two)
    logging.error("Number one %i adding to number two %i", num_one, num_two)
    logging.critical("Number one %i adding to number two %i", num_one, num_two)
    return num_one + num_two


def divide(num_one, num_two):
    return num_one / num_two


add(5, 10)
