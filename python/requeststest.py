import requests
import webbrowser
from PIL import Image
'''
params = {"q":"pizza"}
r = requests.get("https://www.google.com",params=params)
if r.status_code >= 200 and r.status_code <=299:
    webbrowser.open(r.url)
'''

req2 = requests.get("https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fgetwallpapers.com%2Fwallpaper%2Ffull%2F7%2F7%2Ff%2F37399.jpg&f=1&nofb=1")
print(req2.status_code)

image = Image.open(BytesIO(req2.content))
image.show()