![alt cover](https://media.discordapp.net/attachments/823597727887261768/839194420447281172/New_Project_1.png)
# Huntfer

An automation tool to help you to find weak functions in your target source code for potential attacks.

## Features:

- Support multi languages with templates system, so you can add your own template.
- Scanning a single file or a whole directory.
- Changeable regex.

## Install:

```bash
# require Python3
git clone https://github.com/RyouYoo/Huntfer.git
```

## Guide:

```
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

### Template Example:
```json
{
    "extension": "php",
    "functions": {
        "exec": {
            "name": "Execute an external program",
            "exploits": ["Command Injection"]
        }
        .......
}
```
