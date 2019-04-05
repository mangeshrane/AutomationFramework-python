from setuptools import setup

setup(
    name='pytest-pyautomation',
    version='1.0',
    author='mrane',
    author_email='ranemangesh555@gmail.com',
    packages=['pyautomation',
              'pyautomation.api',
              'pyautomation.browsers',
              'pyautomation.configuration',
              'pyautomation.data_providers',
              'pyautomation.file_manager',
              'pyautomation.web',
              ],
    scripts=[],
    entry_points={'pyautomation': [
        'pytest-pyautomation=pyautomation.conftest',
    ]},
    url='',
    license='',
    description='',
    long_description=open('README.md').read(),
    install_requires=[
        "nose2>=0.4.7",
    ],
)