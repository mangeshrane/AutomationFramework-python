import os
import pathlib

project_root = pathlib.Path(os.getcwd()).parent.parent
print(project_root)