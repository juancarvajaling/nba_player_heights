from sys import argv

from raw_data import HTTPGetter


def search_player_pairs(input_height: int) -> str:
    '''Returns a string of all pairs of players whose height in inches adds up
    to the integer input
    
    If no matches are found, the application will return "No matches found".'''

    data = HTTPGetter().get_data()
    if data is None:
        return 'An error accurred fetching NBA player information.'

    output = ''
    # Every player i in the list is compared with every player j, where j > i.
    # So, for a list with length n, i goes to n - 2.
    for idx_i, player_i in enumerate(data[:-1]):
        for player_j in data[idx_i+1:]:
            sum_heights = int(player_i['h_in']) + int(player_j['h_in'])
            if sum_heights == input_height:
                name_i = f'{player_i["first_name"]} {player_i["last_name"]}'
                name_j = f'{player_j["first_name"]} {player_j["last_name"]}'
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
