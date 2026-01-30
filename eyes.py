import sys
import platform
import os

sys.dont_write_bytecode = True

if platform.system() == "Windows":
    os.system("title Eyes")

import asyncio
from lib.cli import parser

asyncio.run(parser())
