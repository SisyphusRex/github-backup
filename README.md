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

## Outside Resources
1. https://gist.github.com/plembo/a786ce2851cec61ac3a051fcaf3ccdab
