'''
Welcome Adriano de Pinho Tavares from Using Python to Access Web Data

Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/opengeo.py. 
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, 
and retrieve the first plus_code from the JSON. An Open Location Code is a textual identifier that is another form of 
address based on the location of the address.

API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Open Street Map Data.

http://py4e-data.dr-chuck.net/opengeo?
This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, 
you get "No address..." response.
To call the API, you need to provide the address that you are requesting as the q= parameter that is properly URL encoded 
using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/opengeo.py

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" 
which will have a plus_code of "6FV8QPRJ+VQ".

$ python solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 1290 characters
Plus code 6FV8QPRJ+VQ
Turn In

Please run your program to find the plus_code for this location:

Elon University

Make sure to enter the name and case exactly as above and enter the plus_code and your Python code below. 
Hint: The first five characters of the plus_code are "87823 ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. 
Your program should work with the Google API - but the plus_code may not match for this assignment.
'''

import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters',  '')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    # print(json.dumps(js, indent=4))

    # lat = js['features'][0]['properties']['lat']
    # lon = js['features'][0]['properties']['lon']
    # print('lat', lat, 'lon', lon)
    # location = js['features'][0]['properties']['formatted']
    # print(location)
    
    #print number o characters

    plus_code = js['features'][0]['properties']['plus_code']
    print('Plus code ', plus_code)
    
# Enter location: Elon University
# Retrieving https://py4e-data.dr-chuck.net/opengeo?q=Elon+University
# Retrieved 1477 characters 
# Plus code  87823GW2+V4
