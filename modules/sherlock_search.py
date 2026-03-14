import subprocess

def search_username(username):

    command = f"sherlock {username}"

    result = subprocess.getoutput(command)

    return result
