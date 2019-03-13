'''
Created on Feb 12, 2019

@author: mrane
'''

def expect_exception(exception):
    """Marks test to expect the specified exception. Call assertRaises internally"""
    def wrapper(fn):
        def wraps(self, *args, **kwargs):
            self.assertRaises(exception, fn, self, *args, **kwargs)
        return wraps
    return wrapper