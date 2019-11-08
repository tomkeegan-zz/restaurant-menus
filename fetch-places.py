import config, googlemaps

class FetchPlaces():
    def setUp(self):
        self.key = config.api_key
        self.client =  googlemaps.Client(self.key)
        self.location = (37.791538, -122.417561)
        self.type = 'restaurant'
        self.language = 'en-US'
        self.region = 'US'
        self.radius = 1