import logging
from py_04 import get_logger


logger = get_logger(__name__)


def baz(el: str):
    logger.info("Start function baz")
    logger.debug(f"el={el}")


def foo():
    logger.error("Exception!")


if __name__ == "__main__":
    baz("test")
    foo()
