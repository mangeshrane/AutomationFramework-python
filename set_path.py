import os

try:
    os.environ['PYTHONPATH']
except KeyError:
    os.environ['PYTHONPATH'] = ""


os.environ['PYTHONPATH'] += os.pathsep + os.path.abspath(os.path.dirname(__file__))

for root, dirs, files in os.walk('.', topdown=False):
    for name in dirs:
        os.environ['PYTHONPATH'] += os.pathsep + os.path.abspath(os.path.dirname(__file__)) + str(os.path.join(root, name)).lstrip('.')

print(os.getenv('PYTHONPATH'))