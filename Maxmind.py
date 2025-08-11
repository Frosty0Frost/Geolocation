import socket
from geolite2 import geolite2
import json

hostname = "google.com"
ip_address = socket.gethostbyname(hostname)
print("Id : {0}".format(ip_address))

reader = geolite2.reader()
response = reader.get(ip_address)

# Print full data (for debugging)
# print(json.dumps(response, indent=4))

# Safe access with .get() to avoid KeyErrors
continent_name = response.get('continent', {}).get('names', {}).get('en', 'Unknown')
country_name = response.get('country', {}).get('names', {}).get('en', 'Unknown')
latitude = response.get('location', {}).get('latitude', 'Unknown')
longitude = response.get('location', {}).get('longitude', 'Unknown')
timezone = response.get('location', {}).get('time_zone', 'Unknown')

print("Continent:", continent_name)
print("Country:", country_name)
print("Latitude:", latitude)
print("Longitude:", longitude)
print("Timezone:", timezone)

geolite2.close()
