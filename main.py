#!/usr/bin/env python

# system imports
import sys
import json
import subprocess

# First Party Imports

# Third Party Imports
import requests


def run(*args):
    """Main Entry Point"""
    repos_url = f"https://api.github.com/users/{args[0]}/repos"
    repo_limit = args[1]

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

    for repo in converted_response:
        try:
            subprocess.run(
                ["git", "clone", repo["html_url"], repo["name"], "--mirror"], check=True
            )
        except subprocess.CalledProcessError as e:
            print("Error cloning repository: %s" % (e))


if __name__ == "__main__":
    run(*sys.argv[1:])
else:
    raise ImportError("Run this file directly, don't import it.")
