import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.application import Application

fixture = None
config = None

@pytest.fixture
def app(request):
    global fixture
    global config
    browser = pytest.config.getoption('--browser')
    if config is None:
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), pytest.config.getoption('--config'))
        with open(config_file_path) as config_file:
            config = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, url=config['url'])
    fixture.session.ensure_login(config['username'], config['password'])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def finalize():
        fixture.session.logout()
        fixture.complete()
    request.addfinalizer(finalize)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', action='store')
    parser.addoption('--config', default='config.json', action='store')


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            test_data = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids = [str(x) for x in test_data])
        elif fixture.startswith("json_"):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids = [str(x) for x in test_data])


def load_from_module(module):
    return importlib.import_module('data.%s' % module).testdata


def load_from_json(json):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/%s.json' % json)) as json_f:
        return jsonpickle.decode(json_f.read())
