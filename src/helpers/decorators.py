import time
import functools
import logging
from functools import wraps
from colorama import Fore, Style


def timer_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        minutes = int(elapsed // 60)
        seconds = elapsed % 60
        logging.info(
            f"{Fore.RED}{func.__name__}{Style.RESET_ALL} executed in "
            f"{Fore.RED}{minutes}M {seconds:.2f}S ({elapsed:.2f} seconds){Style.RESET_ALL}"
        )
        return result

    return wrapper
