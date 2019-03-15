
from functools import singledispatch


@singledispatch
def fprint(data):
    print(f'({type(data).__name__}) {data}')


@fprint.register(list)
@fprint.register(set)
@fprint.register(tuple)
def _(data):
    formatted_header = f'{type(data).__name__} -> index : value'
    print(formatted_header)
    print('-' * len(formatted_header))
    for index, value in enumerate(data):
        print(f'{index} : ({type(value).__name__}) {value}')


@fprint.register(dict)
def _(data):
    formatted_header = f'{type(data).__name__} -> key : value'
    print(formatted_header)
    print('-' * len(formatted_header))
    for key, value in data.items():
        print(f'({type(key).__name__}) {key}: ({type(value).__name__}) {value}')
        

@fprint.register("chrome")
def _(data):
    print("Chrome Entered")


@fprint.register(bytes)
def _(data):
    print(data)

fprint("test String")
fprint("chrome")
fprint([1, 2, 3])
fprint({'a': 1, 'b': 2})
fprint(bytes(32))