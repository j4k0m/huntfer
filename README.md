# Huntfer

An automation tool to help you to find weak functions in your target source code for potential attacks.

## Features:

- Support multi languages with templates system, so you can add your own template.
- Scanning a single file or a whole directory.
- You can use your own regex to find functions in the source code.

## Install:

```bash
# require Python3
git clone https://github.com/RyouYoo/Huntfer.git
```

## Guide:

```bash
__ __  __ __  ____   ______  _____  ___  ____
|  |  ||  |  ||    \ |      ||     |/  _]|    \
|  |  ||  |  ||  _  ||      ||   __/  [_ |  D  )
|  _  ||  |  ||  |  ||_|  |_||  |_|    _]|    /
|  |  ||  :  ||  |  |  |  |  |   _]   [_ |    \
|  |  ||     ||  |  |  |  |  |  | |     ||  .  \. BY: Jakom
|__|__| \__,_||__|__|  |__|  |__| |_____||__|\_|

usage: main.py [-h] -t T [-r R] [-dr DR] [-f F]

optional arguments:
  -h, --help  show this help message and exit
  -t T        Template name to use, example: php, js...
  -r R        Regex to use, default: ^\w.*[(.)].
  -dr DR      Directory to scan.
  -f F        Single file to scan.
```

## Simple Usage:

```bash
python3 main.py -t php -f test.php
```

## Contribute:

You contribute by adding your own template or functions.

## To do:

- [ ]  Add Threads Support
- [ ]  Html Report Export
- [ ]  Colors
