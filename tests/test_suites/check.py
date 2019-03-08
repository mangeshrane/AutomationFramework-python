import traceback
import sys
from contextlib import contextmanager


@contextmanager
def simpleManager(n):
    yield 
    