# Github Backup
The purpose of this program is to make backing up all of a user's github repos an automated process instead of cloning each repo one by one.
This program is not automatic in the sense of cloning repos on its own on a schedule.
It is automatic in the sense that it queries github's API for a list of a user's repos and then iterates over that list, cloning each repo in turn.

This automation allows a user to avoid keeping track of all of his/her repos and cloning them individually.

I am hoping to create an executable to store on a thumbdrive and allow the user to run the executable from the command line and clone the repos to the thumb drive.

## Pseudocode
This code requires the user to have already authenticated his/her machine with Github.
In my experience, when the user tries to push to a repo they must authenticate.  Git stores the credentials for Github in Windows Credential Manager.

** Since we are only cloning public repos, we should not have to authenticate.  If we are cloning private repos, then the machine should be authenticated and credentials stored **

1. Save .exe in backup directory
2. From Command Lone, move to backup directory
3. ./backup.exe <username> <#ofrepos>
4. Iterate through list of repo urls and git clone <url> --mirror

## How-To Backup
1. Clone This Repo
2. cd github-backup
3. python -m pip install -r requirements.txt
4. . .venv/scripts/activate
5. pyinstaller -F backup.py
6. Copy .exe from dist folder
7. Paste .exe in your backup drive (usb, external, etc)
8. cd to the directory with backup.exe
9. ./backup <gh_username> <repo_limit>
    * <gh_username> is your github username
    * <repo_limit> a number above the amount of repos in your account for github's API
  
## How-To Clone from Backup
1. cd to directory where you want to clone repos
2. git clone path/to/source/folder


## Outside Resources
1. https://gist.github.com/plembo/a786ce2851cec61ac3a051fcaf3ccdab
   how to use git package to clone repo from within python
2. https://stackoverflow.com/questions/11113896/use-git-commands-within-python-code
   suggest python subprocess module
3. https://graphite.dev/guides/git-clone-bare-mirror
   what is mirror?  
4. https://stackoverflow.com/questions/15275338/when-doing-a-git-clone-mirror-where-are-the-actual-files
   how to clone from mirror
5. https://stackoverflow.com/questions/21045061/git-clone-from-another-directory
   how to clone from mirror locally
