import time
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_execution(func):
    """
    Log the start and completion of a function's execution.

    This decorator logs the beginning and end of a function's execution,
    providing insight into function call timing and completion for debugging
    and monitoring purposes.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: A wrapper function that logs execution details.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Execution has begun: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Execution has been completed: {func.__name__}")
        return result

    return wrapper


def measure_time(func):
    """
    Measure and log the execution time of a function.

    This decorator calculates and logs the time taken for a function's
    execution, making it a helpful tool for performance measurement and
    optimization.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: A wrapper function that logs execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Execution time {func.__name__}: {end_time - start_time:.4f} s")
        return result

    return wrapper
