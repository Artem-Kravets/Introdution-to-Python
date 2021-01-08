import time
import logging

logging.basicConfig(filename="my_log.log", level=logging.INFO)


def log_decorator(func):

    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        logging.info(
            f"Function Name - {func.__name__} with Args - {args} and Kwargs - {kwargs} run in {run_time}"
        )
        return result
    return wrapper_timer


@log_decorator
def wishes(*args, **kwargs):
    time.sleep(0.3)
    print(args, kwargs)


wishes(["Happy", "New"], year=2021, this_year="cow")

