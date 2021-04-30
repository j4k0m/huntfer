import re, argparse, json, sys

print("""\n __ __  __ __  ____   ______  _____  ___  ____  
|  |  ||  |  ||    \ |      ||     |/  _]|    \ 
|  |  ||  |  ||  _  ||      ||   __/  [_ |  D  )
|  _  ||  |  ||  |  ||_|  |_||  |_|    _]|    / 
|  |  ||  :  ||  |  |  |  |  |   _]   [_ |    \ 
|  |  ||     ||  |  |  |  |  |  | |     ||  .  \. BY: Jakom
|__|__| \__,_||__|__|  |__|  |__| |_____||__|\_|\n""")



TEMPLATES_PATH =  json.load(open("./config.json", "r"))["TEMPLATES_PATH"]

parser = argparse.ArgumentParser()

parser.add_argument('-t', type=str, help="Template name to use, example: php, js...", required=True)
parser.add_argument('-r', type=str, help="Regex to use default: ", default="")

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])


if __name__ == "__main__":
    print(args)