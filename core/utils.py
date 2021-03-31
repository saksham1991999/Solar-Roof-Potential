import requests, urllib, json
from decouple import config


def get_roof(latitude, longitude):
    imagewidth = 400
    imageheight = 400
    scale = 2
    zoom = 20
    maps_static_key = "AIzaSyDLgZUkLB8DomzcmN1WceGvVD_qXw7x8XY"
    url = "https://maps.googleapis.com/maps/api/staticmap?"
    center = str(latitude) + "," + str(longitude)
    urlparams = urllib.parse.urlencode({'center': center,
                                        'zoom': str(zoom),
                                        'size': str(imagewidth) + 'x' + str(imageheight),
                                        'maptype': 'satellite',
                                        'sensor': 'false',
                                        'scale': str(scale),
                                        'key': maps_static_key})
    r = requests.get(url + urlparams)
    print(r.content)
    if not (r.status_code == 404 or r.status_code == 403):
        return r.content
    else:
        return 0



