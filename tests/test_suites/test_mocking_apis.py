import requests_staticmock
import requests
from core.file_manager.file_manager import FileManager
import os


session = requests.Session()
with requests_staticmock.mock_session_with_fixtures(session, # requests session
                                                    os.path.join(FileManager.get_test_datadir(), "data.json"), # path
                                                    'http://test_context.com'): # Base URL to mock
    # will return a response object with the contents of tests/fixtures/test.json
    response = requests.session().request('get', 'http://test_context.com/test.json')
    print(response)
