import requests
import os
import urllib.request

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
}

for i in range(3900,5463):
    try:
        url = f"https://www.midiworld.com/download/{i}"
        r = requests.get(url, headers=headers)
        filename = os.path.join('downloaded', r.headers["Content-disposition"].split("=", -1)[-1])
        print(f"{i} --> {filename} ")
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(url, filename)
    except:
      print(f"Error in : {i}")
      break