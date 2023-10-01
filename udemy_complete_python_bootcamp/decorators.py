#DECORATORS IN PYTHON 3

def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func



@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")
    return 1


func_needs_decorator()