import config, googlemaps

print('Initializing Google Maps API client...\n')
gmaps = googlemaps.Client(key=config.api_key)

location = (37.791531, -122.417573)
radius = 200
language = 'en-US'
type = 'restaurant'

print('Fetching list of places...\n')
place_ids = gmaps.places_nearby(location=location, radius=radius, language=language, type=type)

print('Fetching websites for following restaurants:\n')
with open('data/websites.txt', 'w') as fp:
    for result in place_ids['results']:
        details = gmaps.place(result['place_id'])['result']
        website = details.get('website', None)
        if website != None:
            print(result['name'] + '\n' + website + '\n')
            fp.write(website + '\n')