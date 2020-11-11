# https://www.youtube.com/watch?v=swU3c34d2NQ
# Programming Terms: Closures - How to Use Them and Why They Are Useful

import logging
logging.basicConfig(filename='example.log', level = logging.INFO)

def logger(func):

    def log_func(*args):
        logging.info(
        'running "{}" with arguments {}'.format(func.__name__, args)
        )
        print(func(*args))

    return log_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger = logger(add)
add_logger(3,4)
