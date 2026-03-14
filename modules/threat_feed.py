import requests

def get_threats():

    url = "https://otx.alienvault.com/api/v1/pulses/subscribed"

    try:
        r = requests.get(url)
        return r.json()
    except:
        return {"error":"unable to fetch threat feed"}
