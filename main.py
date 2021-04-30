import re, argparse, json

TEMPLATES_PATH =  json.load(open("./config.json", "r"))["TEMPLATES_PATH"]

parser = argparse.ArgumentParser()

