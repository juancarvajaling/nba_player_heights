# NBA Player Heights

This application takes a single integer input, compare it with NBA player heights information, and prints a list of all pairs of players whose height in inches adds up to the integer.

## Requirements

- requests

## Installation

Install with:
```bash
pip install -r /path/to/nba_player_heights/requirements.txt
```

## Usage

`search` module need to be called with a height in inches as argument, for example:

```bash
python /path/to/nba_player_heights/player_heigths/search.py 139
```

Then, the application will display the list of pairs as follow:

```bash
- Brevin Knight          Nate Robinson
- Nate Robinson          Mike Wilks
```

## Test

To run the tests, first install the requirements:
```bash
pip install -r /path/to/nba_player_heights/requirements_test.txt
```

Next:
```bash
pytest /path/to/nba_player_heights/tests.py
```