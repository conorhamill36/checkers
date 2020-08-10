#Decorators to be used with checkers.py
import functools
import time
import os, sys

#Decorator that simply prints the name of the function before and after executing
def func_name(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\n>>Function being called is {}()\n".format(func.__name__))
        value = func(*args, **kwargs)
        print("\n>>Function that was called was {}()\n".format(func.__name__))
        return value
    return wrapper


#Decorator to pause at the end of a function
def dramatic_pause(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        sleep_dur = 0
        print("Pausing for {} seconds...".format(sleep_dur))
        time.sleep(sleep_dur)
        return value
    return wrapper


#Decorator to suppress printing of a function
def mute_printing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sys.stdout = open(os.devnull, 'w') #Disables printing by changing stdout
        value = func(*args, **kwargs)
        sys.stdout = sys.__stdout__ #Re-enables painting by pointing back to the system's stdout
        return value
    return wrapper
