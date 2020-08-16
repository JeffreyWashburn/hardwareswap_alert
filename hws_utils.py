from json import load, dump
from datetime import datetime as dt
from os.path import isfile
from argparse import ArgumentParser

NOTIFY_IMG = "icons/hardwareswap.ico"
HWSWAP_NEW = "https://www.reddit.com/r/hardwareswap/new"

def save_discovered(discovered):
    with open("history.json", "w") as f:
        dump(discovered, f)

def load_discovered():
    with open("history.json", "r") as f:
        discovered = load(f)
    while len(discovered) < 3:
        discovered.append(None)
        save_discovered(discovered)
    return discovered

def create_history():
    if not isfile("history.json"):
        with open("history.json", "w") as f:
            dump([None, None, None], f)

def create_defaults():
    if not isfile("defaults.json"):
        with open("defaults.json", "w") as f:
            dump({
                "desc": "Monitor r/hardwareswap for certain posts",
                "patterns": ["usa"],
                "flair_filters": ["selling", "trading"]
            }, f)

def load_defaults():
    if isfile("defaults.json"):
        with open("defaults.json", "r") as f:
            return load(f)

def get_now():
    return dt.strftime(dt.now(), "%Y%m%d %H-%M-%S")

def get_args(defaults):
    # get command line arguments
    parser = ArgumentParser(defaults['desc'])
    parser.add_argument(
        "-p", "--patterns",
        nargs="*",
        default=defaults['patterns'],
        help="Patterns to match posts with",
    )
    parser.add_argument(
        "-f", "--flairs",
        nargs="*",
        default=defaults['flair_filters'],
        help="Flairs to filter posts with"
    )
    return parser.parse_args()

def validate_args(args, patterns_to_validate):
    for pattern in args.patterns:
        if pattern not in patterns_to_validate:
            print(f"Pattern {pattern} does not exist. Edit 'patterns' dict to create your own.")
            exit()