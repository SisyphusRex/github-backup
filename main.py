#!/usr/bin/env python

# system imports
import sys
import json

# First Party Imports

# Third Party Imports
import requests


def run(*args):
    """Main Entry Point"""
    try:
        params = {"per_page": 100}
        response = requests.get(
            "https://api.github.com/users/sisyphusrex/repos", timeout=10, params=params
        )
    except requests.RequestException:
        sys.exit("bad request")

    file_path = "repo_list.json"

    converted_response = response.json()

    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(converted_response, json_file, indent=4)


if __name__ == "__main__":
    run(*sys.argv[1:])
else:
    raise ImportError("Run this file directly, don't import it.")
