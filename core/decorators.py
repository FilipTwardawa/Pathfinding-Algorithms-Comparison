import time
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_execution(func):
    """A decorator that logs the execution of a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Execution has begun: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Execution has been completed: {func.__name__}")
        return result

    return wrapper


def measure_time(func):
    """A decorator that measures the execution time of a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Execution time {func.__name__}: {end_time - start_time:.4f} s")
        return result

    return wrapper
