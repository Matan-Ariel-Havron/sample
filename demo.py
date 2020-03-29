import math
import sys
from os import rename

import requests


def main():
    r = requests.get("https://coreyms.com")
    print(r.status_code)


if __name__ == "__main__":
    main()
