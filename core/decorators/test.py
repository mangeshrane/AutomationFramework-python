from core.decorators.stacktrace import StackTrace
from functools import wraps
import sys

def Test(**kw):
    def entangle(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            st = StackTrace(**kw)
            sys.settrace(st)
            try:
                return func(*args, **kwargs)
            finally:
                sys.settrace(None)
        return wrapper
    return entangle