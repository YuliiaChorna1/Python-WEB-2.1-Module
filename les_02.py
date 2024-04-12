# MODERN logging approuch

import logging
import logging.config

logger = logging.getLogger("logging_test_app")

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        # "hello_wold": {
        #     "format": "%(asctime)s --- %(levelname)s: %(message)s"
        # },
        "simple": {
            "format": "%(asctime)s %(levelname)s: %(message)s"
        },
        "super simple": {
            "format": "%(message)s"
        }
    },
    "handlers":{
        # "hello_world": {
        #     "class": "logging.StreamHandler",
        #     "formatter": "simple",
        #     "stream": "ext://sys.stdout"
        # },
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler", # IMPORTANT to use!!
            "level": "DEBUG",
            "formatter": "super simple",
            "filename": "les_logs/my_app.log",
            "maxBytes": 10000,
            "backupCount": 2
        }
    },
    "loggers": {
        "root": {
            "level": "WARNING",
            "handlers": ["stdout", "file"]
        }
    }
}

def main():
    logger.debug("This is a debug message")
    logger.info("This is a info message")
    logger.warning("This is a warning message")
    logger.error("This is a error message")
    logger.critical("This is a critical message")

    try:
        1 / 0
    except ZeroDivisionError as _:
        logger.exception("Oooops")

if __name__ == '__main__':
    logging.config.dictConfig(logging_config)

    main()
