import requests

def get_status_code(site_url):
    r = requests.get(site_url, allow_redirects=False)
    return r.status_code