'''This module is used to get NBA player heights.'''

from typing import Union

import requests


class HTTPGetter:
    '''Represents an object to get NBA player heights information.'''

    def __fetch_data(self) -> dict:
        '''Fetch NBA player heights information.'''

        raw_data = {}
        try:
            response = requests.get(
                'https://mach-eight.uc.r.appspot.com/', timeout=5
            )
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return raw_data
        
        raw_data = response.json()
        return raw_data

    def get_data(self) -> Union[list, None]:
        '''Return only the player list information from the fetched response.'''

        raw_data = self.__fetch_data()
        return raw_data.get('values')
