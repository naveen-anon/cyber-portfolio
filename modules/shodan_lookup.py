import shodan
from config import SHODAN_API

def shodan_search(ip):

    api = shodan.Shodan(SHODAN_API)

    try:

        host = api.host(ip)

        return host

    except Exception as e:

        return {"error": str(e)}
