def debug(func):
    def wrapper(*args,**kwargs):
        args_value=",".join(str(arg) for arg in args)
        kwargs_value=",".join(f"{key} {value}" for key,value in kwargs.items() )

        result=func(*args,**kwargs)
        print(f"function {func.__name__} with args {args_value} and Kwargs {kwargs_value}")
        return result
    return wrapper








@debug
def greet(name="user",greeting="hello"):
    print(f"{greeting} {name}")

greet("chai",greeting="hanji")

@debug
def hello():
    print("hello")

hello()

