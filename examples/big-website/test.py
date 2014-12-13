import json
from onecv import website

with open('cv.json', 'r') as cvfile:
   jsonObj = json.load(cvfile)

with open('cv.html', 'w') as outfile:
   outfile.write(website.makeWebsite(jsonObj, importanceThreshold=3))
