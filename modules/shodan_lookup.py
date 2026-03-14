
import shodan
from config import SHODAN_API

def shodan_host(ip):

    api = shodan.Shodan(LSkyFO1W4JBevcT5yZoOJXMiCgOZIjqx)

    try:

        host = api.host(ip)

        return host

    except:

        return {"error":"host not found"}
