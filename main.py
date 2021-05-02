#!/usr/bin/pythno3
import re, argparse, json, sys, os

def scan_file(_file):
    try:
        FILE_CONTENT = open(_file, "r").readlines()
    except FileNotFoundError as e:
        print(e)
    else:
        for i in range(len(FILE_CONTENT)):
            line = FILE_CONTENT[i]
            RESULT = re.search(args.r, line)
            if RESULT:
                FUN = RESULT[0].split("(")[0]
                if FUN in list(TEMPLATE["functions"].keys()):
                    print(f"{_file} -> Found [{FUN}] in line: {str(i + 1)}, Name: {TEMPLATE['functions'][FUN]['name']}, Potential attacks: {' '.join(i for i in TEMPLATE['functions'][FUN]['exploits'])}")

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
parser.add_argument('-r', type=str, help=f"Regex to use, default: {DEFAULT_REGEX}.", default=f"{DEFAULT_REGEX}")
parser.add_argument('-dr', type=str, help=f"Directory to scan.")
parser.add_argument('-f', type=str, help=f"Single file to scan.")

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])


if __name__ == "__main__":
    try:
        TEMPLATE = json.load(open(f"{TEMPLATES_PATH}/{args.t}.json", "r"))
    except FileNotFoundError as e:
        print(e)
    else:
        if args.dr:
            for root, dirs, files in os.walk(args.dr, topdown=False):
                for name in files:
                    if name.split(".")[-1] == TEMPLATE["extension"]:
                        scan_file(os.path.join(root, name))
        elif args.f:
            scan_file(args.f)