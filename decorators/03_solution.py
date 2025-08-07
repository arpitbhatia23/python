import time

def cache(func):
    cache_value={}
    print(f"cache value {cache_value}")
    def wrapper(*args,**kwargs):
        if args in cache_value:
            return cache_value[args]
        result=func(*args,**kwargs)
        cache_value[args]=result
        return result
    return wrapper





@cache
def long_function(a,b):
    time.sleep(4)
    return a + b

print(long_function(1, 2))
print(long_function(3, 2))
print(long_function(3, 2))
print(long_function(1, 2))
print(long_function(1, 2))



