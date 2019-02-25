import urllib
import json

import requests

def getData(url):
    u = urllib.urlopen(url)
    data_str = u.read()

    try:
        data = json.loads(data_str)
    except Exception as e:
        print 'Error : %s' %(e)
        sys.exit(1)

    return data

