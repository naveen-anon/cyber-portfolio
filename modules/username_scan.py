import subprocess

def scan_username(username):

    result = subprocess.getoutput(f"sherlock {username}")

    return {"result": result}
