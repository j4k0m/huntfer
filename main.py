#!/usr/bin/pythno3
import re, argparse, json, sys

print("""\n __ __  __ __  ____   ______  _____  ___  ____  
|  |  ||  |  ||    \ |      ||     |/  _]|    \ 
|  |  ||  |  ||  _  ||      ||   __/  [_ |  D  )
|  _  ||  |  ||  |  ||_|  |_||  |_|    _]|    / 
|  |  ||  :  ||  |  |  |  |  |   _]   [_ |    \ 
|  |  ||     ||  |  |  |  |  |  | |     ||  .  \. BY: Jakom
|__|__| \__,_||__|__|  |__|  |__| |_____||__|\_|\n""")


CONFIG = json.load(open("./config.json", "r"))

TEMPLATES_PATH =  CONFIG["TEMPLATES_PATH"]
DEFAULT_REGEX = CONFIG["DEFAULT_REGEX"]

parser = argparse.ArgumentParser()

parser.add_argument('-t', type=str, help="Template name to use, example: php, js...", required=True)
parser.add_argument('-r', type=str, help=f"Regex to use, default: {DEFAULT_REGEX}", default=f"{DEFAULT_REGEX}")

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])


if __name__ == "__main__":
    try:
        TEMPLATE = json.load(open(f"{TEMPLATES_PATH}/{args.t}.json", "r"))
    except FileNotFoundError as e:
        print(e)
    else:
        print(TEMPLATE)