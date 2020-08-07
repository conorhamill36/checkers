#Decorators to be used with checkers.py
import time

#Decorator that simply prints the name of the function before and after executing
def func_name(func):
    def wrapper(*args, **kwargs):
        print("\n>>Function being called is {}()\n".format(func.__name__))
        value = func(*args, **kwargs)
        print("\n>>Function that was called was {}()\n".format(func.__name__))
        return value
    return wrapper


#Decorator to pause at the end of a function
def dramatic_pause(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        time.sleep(3)
        return value
    return wrapper


#Decorator to suppress printing of a function
def mute_printing(func):
    def wrapper(*args, **kwargs):
        sys.stdout = open(os.devnull, 'w') #Disables printing by changing stdout
        value = func(*args, **kwargs)
        sys.stdout = sys.__stdout__ #Re-enables painting by pointing back to the system's stdout
        return value
    return wrapper