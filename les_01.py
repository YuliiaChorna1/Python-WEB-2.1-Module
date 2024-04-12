import logging

def main():
    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")

    try:
        1 / 0
    except ZeroDivisionError as _:
        logging.exception("Oooops")

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.WARNING
    )

    main()