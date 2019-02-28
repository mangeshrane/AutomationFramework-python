from core.decorators.stacktrace import StackTrace
import sys
from core.logger import log

k = ""

def Test(*args, tags=None, invocation_count=1):
    print("HERE -01 ")
    def entangle(func):
        def wrapper(*args, **kwargs):
            st = StackTrace()
            sys.settrace(st)
            try:
                for i in range(invocation_count):
                    func(*args, **kwargs)
            finally:
                sys.settrace(None)
        return wrapper
    return entangle