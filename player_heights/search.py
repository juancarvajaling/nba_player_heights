from sys import argv
from itertools import combinations

from raw_data import HTTPGetter


def search_player_pairs(input_height: int) -> str:
    '''Returns a string of all pairs of players whose height in inches adds up
    to the integer input
    
    If no matches are found, the application will return "No matches found".'''

    data = HTTPGetter().get_data()
    if data is None:
        return 'An error accurred fetching NBA player information.'

    output = ''
    # Loop for every pair of players
    for pair in combinations(data, 2):
        sum_heights = int(pair[0]['h_in']) + int(pair[1]['h_in'])
        if sum_heights == input_height:
            name_i = f'{pair[0]["first_name"]} {pair[0]["last_name"]}'
            name_j = f'{pair[1]["first_name"]} {pair[1]["last_name"]}'
            output += f'- {name_i:25}{name_j}\n'

    if not output:
        output = 'No matches found'

    return output


def main(input_argv: list) -> str:
    '''Handles the module running.'''

    if len(input_argv) < 2:
        return 'No argument was passed.'

    try:
        input_height = int(input_argv[1])
    except ValueError:
        return 'It was expected a number as input.'

    output = search_player_pairs(input_height)
    return output


if __name__ == '__main__':
    output = main(argv)
    print(output)
