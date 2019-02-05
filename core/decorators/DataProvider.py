from functools import wraps

def data(arg):
    def wrap(f):
        def parser(func, args):
            func(*args)
        def wrapper(*args, **kwargs):
            for i in arg:
                parser(f, i)
        return wrapper
    return wrap


@data([[1, 2],[3, 2],[3, 3]])
def test(k, l):
    print("Got parameter ", k, l)


test()
