#!/usr/bin/env python3

import sys, requests, warnings
warnings.filterwarnings("ignore")

apikey = sys.argv[1] if len(sys.argv)>1 else input("Feed me a google maps api key. -> ")

endpoints = {
	"static-map": ['', f"https://maps.googleapis.com/maps/api/staticmap?center=45%2C10&zoom=7&size=400x400&key={apikey}"],
	"street-view": ['', f"https://maps.googleapis.com/maps/api/streetview?size=400x400&location=46.5116899,-84.3401894&fov=90&heading=235&pitch=10&key={apikey}"],
	"embed (free)": ['', f"https://www.google.com/maps/embed/v1/place?q=Ottawa&key={apikey}"],
	"embed (paid)": ['', f"https://www.google.com/maps/embed/v1/search?q=restaurants+in+ottawa&key={apikey}"],
	"directions": ['error_message', f"https://maps.googleapis.com/maps/api/directions/json?origin=the+white+house&destination=the+pentagon&key={apikey}"],
	"geocode": ['error_message', f"https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key={apikey}"],
	"distance matrix": ['error_message', f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key={apikey}"],
	"place from text": ['error_message', f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={apikey}"],
	"timezone": ['error', "https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key={apikey}"],
	"autocomplete": ['error_message', f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Bingh&types=%28cities%29&key={apikey}"],
	"elevation": ['error_message', f"https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034&key={apikey}"],
	"roads": ['error', f"https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|60.170877,24.942796&key={apikey}"],
	"geolocate": ['error', f"https://www.googleapis.com/geolocation/v1/geolocate?key={apikey}", {'considerIp':'true'}]
}

for i in endpoints.keys():

	if len(endpoints[i]) == 3: 
		response = requests.post(endpoints[i][1], data=endpoints[i][2], verify=False)
		if response.text.find(endpoints[i][0]) < 0:
			print(f"{i} : {endpoints[i][1]}")
	else:
		response = requests.get(endpoints[i][1], verify=False)

		if not endpoints[i][0]:
			if response.status_code == 200:
				print(f"{i} : {endpoints[i][1]}")
		else:
			if response.text.find(endpoints[i][0]) < 0:
				print(f"{i} : {endpoints[i][1]}")
