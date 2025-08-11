import socket
import requests
from geolite2 import geolite2


public_ip = requests.get("https://api.ipify.org").text
print("Your Public IP:", public_ip)

reader = geolite2.reader()

def get_geo_info(ip):
    response = reader.get(ip)
    if not response:
        print("No data for IP:", ip)
        return
    
    continent = response.get('continent', {}).get('names', {}).get('en', 'Unknown')
    country = response.get('country', {}).get('names', {}).get('en', 'Unknown')
    city = response.get('city', {}).get('names', {}).get('en', 'Unknown')
    latitude = response.get('location', {}).get('latitude', 'Unknown')
    longitude = response.get('location', {}).get('longitude', 'Unknown')
    timezone = response.get('location', {}).get('time_zone', 'Unknown')

    print("\nIP Address:", ip)
    print("Continent:", continent)
    print("Country:", country)
    print("City:", city)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Timezone:", timezone)

# Get your location
get_geo_info(public_ip)


geolite2.close()


