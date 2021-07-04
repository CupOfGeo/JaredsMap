import googlemaps
from datetime import datetime

with open('secret.txt','r') as file:
    api_key = file.read()

gmaps = googlemaps.Client(key=api_key)

# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#
# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.distance_matrix("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
print(directions_result['rows'])
#for thing in directions_result:
#    print(thing)
#    print('-'*50)