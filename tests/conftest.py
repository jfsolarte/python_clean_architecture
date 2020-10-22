
import pytest


from python_clean_architecture.app import create_app
from python_clean_architecture.settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)