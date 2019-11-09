import config, googlemaps, requests

gmaps = googlemaps.Client(key=config.api_key)

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

location = (37.791531, -122.417573)
radius = 200
language = 'en-US'
type = 'restaurant'

place_ids = gmaps.places_nearby(location=location, radius=radius, language=language, type=type)

for result in place_ids['results']:
    print(result['name'])