import requests
import json

# Define the Overpass API endpoint
OVERPASS_URL = 'http://overpass-api.de/api/interpreter'

# Define locations to fetch
locations = ['Waffle House', 'Home Depot', "Lowe's"]

# Function to fetch data from Overpass API

def fetch_locations(location):
    query = f'[out:json];node["amenity"="restaurant"]["name"~"{location}"](area);out body;';
    response = requests.get(OVERPASS_URL, params={'data': query})
    return response.json()

# Function to check status based on definitions

def check_status(count):
    if count > 10:
        return 1  # Green operational
    elif count > 0:
        return 2  # Yellow warning
    else:
        return 3  # Red critical

# Main function to get locations and check their status

def main():
    result = {}
    for location in locations:
        data = fetch_locations(location)
        count = len(data['elements'])
        status = check_status(count)
        result[location] = {'count': count, 'status': status}

    # Write the result to data.json
    with open('data.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)

if __name__ == '__main__':
    main()
