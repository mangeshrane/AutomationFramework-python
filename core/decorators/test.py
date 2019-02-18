from core.decorators.stacktrace import StackTrace
import sys

k = ""

def Test(*args, tag=None):
    def entangle(func):
        def wrapper(*args, **kwargs):
            st = StackTrace()
            sys.settrace(st)
            try:
                return func(*args, **kwargs)
            finally:
                sys.settrace(None)
        return wrapper
    return entangle