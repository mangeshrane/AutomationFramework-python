import pytest
import unittest
from core.decorators.DataProvider import data

import ptest



    
@unittest.expectedFailure
def test_default_size(color):
    print(color)