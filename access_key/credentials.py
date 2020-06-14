import json
import os

package_dir = os.path.dirname(os.path.abspath(__file__))
access_key_path = os.path.join(package_dir, 'access.json')


def get_credentials(path: str = access_key_path) -> dict:
    with open(path, "r") as file:
        credentials = json.load(file)

    return credentials
