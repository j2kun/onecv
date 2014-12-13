import json
from onecv import tex

with open('cv.json', 'r') as cvfile:
   jsonObj = json.load(cvfile)

with open('cv.tex', 'w') as outfile:
   outfile.write(tex.makeTex(jsonObj, importanceThreshold=3))
