import argparse
import asyncio

from .banner import banner, banner_help
from output import eyes_output
from .check_version import check_python_version


async def parser():
    parser = argparse.ArgumentParser(
        add_help=False  # IMPORTANTE: desactivamos el help automático
    )

    parser.add_argument(
        'email',
        nargs='?',
        type=str,
        default=None,
        help='search information on the target email with modules, services...'
    )

    parser.add_argument(
        '-m', '--modules',
        action='store_true',
        help='gives you all the email modules used by Eyes'
    )

    parser.add_argument(
        '-h', '--help',
        action='store_true',
        help='show this help message and exit'
    )

    args = parser.parse_args()

    # -------- HELP --------
    if args.help:
        print(banner_help)
        print("""
usage: python eyes.py [-h] [-m] [email]

positional arguments:
  email          search information on the target email with modules, services...

options:
  -h, --help     show this help message and exit
  -m, --modules  gives you all the email modules used by Eyes
""")
        exit()

    # -------- MODULES --------
    if args.modules:
        print(banner_help)
        print("""
[👀] Email modules :

 ├── Duolingo        # scrapable
 ├── GitHub          # scrapable (token optional)
 ├── Gravatar        # scrapable
 ├── Imgur
 ├── Mail.ru
 ├── Pastebin        # links dump
 ├── Protonmail      # scrapable
 ├── Bitmoji
 ├── Instagram
 ├── X (Twitter)
 ├── HudsonRock      # infostealer intelligence
 └── XposedOrNot     # breach exposure
""")
        exit()

    # -------- EMAIL SEARCH --------
    if args.email:
        check_python_version()
        print(banner)
        await eyes_output(args.email)
        exit()

    # -------- NO ARGUMENTS --------
    print(banner_help)
    print("Use -h to display help")
    exit()


def main():
    asyncio.run(parser())
