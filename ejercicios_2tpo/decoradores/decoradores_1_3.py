import time

def wait_on(func):
    def wrapper(*args, **kwargs):
        time.sleep(3)
        result = func(*args,**kwargs)
        return result
    return wrapper

@wait_on
def sum(a,b):
    return a+b

print(sum(5,5))