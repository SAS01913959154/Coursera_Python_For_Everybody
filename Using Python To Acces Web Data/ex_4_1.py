# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
nums = soup('span')
count=0
sum=0
y=list()
for num in nums:
    strnum=str(num)
    y=re.findall('([0-9]+)',strnum)
    for i in y:
        count=count+1
        sum=sum+int(i)
print("count:",count)
print("sum:",sum)
