#!/usr/bin/env python

# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 


# system imports
import sys
import json
import subprocess
from datetime import date

# First Party Imports

# Third Party Imports
import requests


def run(*args):
    """Main Entry Point"""
    if len(args) != 2:
        print(
            "Program takes two arguments.\nUsage:\n./backup <username> <#ofreposlimit>"
        )
        sys.exit()

    repos_url = f"https://api.github.com/users/{args[0]}/repos"
    repo_limit = int(args[1])

    try:
        params = {"per_page": repo_limit}
        response = requests.get(repos_url, timeout=10, params=params)
    except requests.RequestException:
        sys.exit("Bad Request.")

    file_path = f"{date.today()}.json"

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
