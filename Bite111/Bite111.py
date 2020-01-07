import requests

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    url = IPINFO_URL.replace('{ip}', ip_address)
    r = requests.get(url).json()
    result = r.get('country')
    return result


ip = get_ip_country('185.161.200.10')
print(ip)