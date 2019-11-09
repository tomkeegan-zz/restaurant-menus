import config, googlemaps

print('Initializing Google Maps API client...\n')
gmaps = googlemaps.Client(key=config.api_key)

location = (37.791531, -122.417573)
radius = 200
language = 'en-US'
type = 'restaurant'

print('Fetching list of places...\n')
place_ids = gmaps.places_nearby(location=location, radius=radius, language=language, type=type)

fp = open('data/place-ids.txt', 'w')

print('Fetched place_id for following restaurants:\n')
for result in place_ids['results']:
    print(result['name'])