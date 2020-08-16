# Imports
import hws_utils
import hws_praw
import hws_patterns
from traceback import format_exc
from sys import exit
from multiprocessing import Process
from private.creds import my_credentials as mycreds

def handle_input(thread):
    while True:
        command = input("").lower().strip()
        if command == "stop":
            confirm = input("[*][STOP]: Exit? [y/n]: ").lower().strip()
            if confirm == "y":
                thread.terminate()
                exit()
            elif confirm == "n":
                continue
            else:
                continue
        else:
            print(f"[*][ERROR]: Command '{command}' does not exist.")

def start_msg(patterns, flair_filters):
    
    print(f"[{hws_utils.get_now()}][START]: Checking posts for patterns:")
    for pattern in patterns:
        print(pattern)
    print("And filtering by flairs:")
    for flair in flair_filters:
        print(flair)

if __name__ == "__main__":
    # create necessary files if they don't already exist
    hws_utils.create_history()
    hws_utils.create_defaults()

    # bring in default arguments
    defaults = hws_utils.load_defaults()

    # get args
    args = hws_utils.get_args(hws_utils.load_defaults())

    # validate arguments
    hws_utils.validate_args(args, hws_patterns.patterns)

    # localize args for readability
    patterns_list = [hws_patterns.patterns[pattern_string] 
        for pattern_string in args.patterns]
    flair_filters = args.flairs

    # run main thread with our arguments and handle input
    try:
        print(start_msg(args.patterns, args.flairs))
        main = Process(
            target=hws_praw.monitor,
            args=[patterns_list, flair_filters]
        )
        main.start()
        handle_input(main)
    except SystemExit:
        exit()
    except:
        var = format_exc()
        with open(f"err/{hws_utils.get_now()} traceback.err", "w") as f:
            f.write(var)