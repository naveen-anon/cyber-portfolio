
import requests

def domain_lookup(domain):

    url = f"https://api.hackertarget.com/whois/?q={domain}"

    r = requests.get(url)

    return {"whois": r.text}
