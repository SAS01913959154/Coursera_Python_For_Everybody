import urllib.request, urllib.parse, urllib.error
import json
import ssl


# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

print('User count:', len(js))
#print(json.dumps(js, indent=4))
sum=0
count=0
for item in js['comments']:
    num=item['count']
    count=count+1
    sum=sum+int(num)
print("Count : ",count)
print("Sum : ",sum)
