import re, argparse, json, sys

TEMPLATES_PATH =  json.load(open("./config.json", "r"))["TEMPLATES_PATH"]

parser = argparse.ArgumentParser()

parser.add_argument('-t', type=str, help="Template name to use, example: php, js...", required=True)
parser.add_argument('-r', type=str, help="Regex to use default: ", default="")

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

print(args)