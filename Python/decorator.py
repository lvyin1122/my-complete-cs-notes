# a simple decorator
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))
        return func(*args, **kwargs)

    return wrapper

@log
def test(p):
    print(test.__name__ + " param: " + p)
    
test("I'm a param")

# decorator with params

import functools

def log_with_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)

        return wrapper

    return decorator
    
@log_with_param("param")
def test_with_param(p):
    print(test_with_param.__name__)

