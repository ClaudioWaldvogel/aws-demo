import os

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Avoid insecure warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
