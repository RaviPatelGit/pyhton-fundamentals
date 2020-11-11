# https://www.youtube.com/watch?v=FsAPt_9Bf3U
# Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions
from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran {} wirh args {}, and keyword args:{}'.format(orig_func.__name__, args,  kwargs))
        print(args)
        print(kwargs)
        return orig_func(*args, **kwargs)

    return wrapper



def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def my_wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} took {} sec to run.'.format(orig_func.__name__, t2))
        return result

    return my_wrapper

# @my_timer

@my_logger
@my_timer
def display_info(name, age):
    import time
    time.sleep(0.5)
    print('name:{} ,  age:{} '.format(name,age))

# my_disp = my_timer(display_info)

# my_disp('Raj', 28)
display_info('Ravi Patel', 26)
