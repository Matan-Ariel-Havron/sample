import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def main():
    r = requests.get("https://coreyms.com")
    print(r.status_code)
    print("sdf")


if __name__ == "__main__":
    main()
