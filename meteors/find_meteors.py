import math
import requests

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

def get_dist(meteor):
    return meteor.get('distance', math.inf)

# if __name__ == '__main__':
# The code can tell if its a script or imported as a module
# if it is called as a module, this wont run
if __name__ == '__main__':
    my_loc = (33.5757706, -117.6493759)
# a Third comment
    meteor_resp = requests.get('https://data.nasa.gov/resource/y77d-th95.json')
    meteor_data = meteor_resp.json()
# a second set of test comments
    for meteor in meteor_data:
        if not ('reclat' in meteor and 'reclong' in meteor): continue
        meteor['distance'] = calc_dist(float(meteor['reclat']),
                                       float(meteor['reclong']),
                                       my_loc[0],
                                       my_loc[1])

    meteor_data.sort(key=get_dist)
# some notes here
    print(meteor_data[0:10])
