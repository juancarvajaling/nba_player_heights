import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'player_heights')))

import requests
import pytest
import requests_mock

from search import main, search_player_pairs


@pytest.fixture(scope='class')
def url():
    return 'https://mach-eight.uc.r.appspot.com/'


@pytest.fixture(scope='class')
def sample_data():
    data = {'values': [
        {
            'first_name': 'Alex',
            'h_in': '77',
            'h_meters': '1.96',
            'last_name': 'Acker'
        },
        {
            'first_name': 'Morris',
            'h_in': '74',
            'h_meters': '1.88',
            'last_name': 'Almond'
        },
        {
            'first_name': 'LaMarcus',
            'h_in': '77',
            'h_meters': '1.96',
            'last_name': 'Aldridge'
        },
        {
            'first_name': 'Louis',
            'h_in': '81',
            'h_meters': '2.06',
            'last_name': 'Amundson'
        },
        {
            'first_name': 'Jose',
            'h_in': '77',
            'h_meters': '1.96',
            'last_name': 'Barea'
        }
    ]}
    return data


@pytest.fixture(scope='class')
def expected_result():
    result = (
        f'- {"Alex Acker":<25}LaMarcus Aldridge\n'
        f'- {"Alex Acker":<25}Jose Barea\n'
        f'- {"LaMarcus Aldridge":<25}Jose Barea\n'
    )
    return result


class TestPlayerHeights:

    def test_no_argument(self):
        assert main(['']) == 'No argument was passed.'

    def test_no_integer_input(self):
        assert main(['', 'a']) == 'It was expected a number as input.'

    def test_matches_found(self, requests_mock, url, sample_data, expected_result):
        requests_mock.get(url, json=sample_data)
        assert search_player_pairs(154) == expected_result

    def test_no_matches_found(self, requests_mock, url, sample_data):
        requests_mock.get(url, json=sample_data)
        assert search_player_pairs(300) == 'No matches found'

    def test_timeout_error(self, requests_mock, url):
        requests_mock.get(url, exc=requests.exceptions.ConnectTimeout)
        assert search_player_pairs(170) == 'An error accurred fetching NBA player information.'

    def test_http_400_error(self, requests_mock, url):
        requests_mock.get(url, status_code=400)
        assert search_player_pairs(170) == 'An error accurred fetching NBA player information.'

    def test_http_500_error(self, requests_mock, url):
        requests_mock.get(url, status_code=500)
        assert search_player_pairs(170) == 'An error accurred fetching NBA player information.'

    def test_connection_error(self, requests_mock, url):
        requests_mock.get(url, exc=requests.exceptions.ConnectionError)
        assert search_player_pairs(170) == 'An error accurred fetching NBA player information.'

