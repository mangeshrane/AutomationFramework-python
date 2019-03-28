import os
import pytest

"""Configuration for pytest runner."""
pytest_plugins = 'core.reporter.pytest_plugin'

def pytest_addoption(parser):
    parser.addoption("--config", action="store")
    parser.addoption("--browser", action="store")
                   
@pytest.fixture(scope='session', autouse=True)
def config(request):
    config_file = request.config.option.config
    if config_file and os.path.isfile(config_file):
        os.environ['AUTO_CONFIG'] = config_file
        print("-- overriding default configuration with : " + config_file)
    else:
        print("Config file doesn't exist")

@pytest.fixture(scope="session", autouse=True)
def set_browser(request):
    browser = request.config.option.browser
    if browser:
        os.environ["CORE.DRIVER"] = browser
        print("-- overriding default driver configuration with : " + browser)
