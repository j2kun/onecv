
jsonString = '''{
   "Personal":
      {
         "Name": "Jeremy Kun",
         "Advisor": "Lev Reyzin",
         "Website": "http://math.uic.edu/~jkun2"
      },
   "Education":
      [
         {
          "when": "2011 - Present",
          "institution": "University of Illinois at Chicago",
          "degree": "Ph.D",
          "subject": "Mathematics",
          "comments": "Expected 2016.",
          "importance": 1
         },
         {
          "when": "2007 - 2011",
          "institution": "California Polytechnic State University",
          "degree": "B.S.",
          "subject": "Mathematics, Minor in Computer Science",
          "comments": "Magna Cum Laude.",
          "importance": 1
         },
         {
          "when": "2011",
          "institution": "Budapest Semesters in Mathematics",
          "comments": "Graduated with honors.",
          "importance": 2
         }
      ]
}'''

import json

jsonObj = json.loads(jsonString)
sectionKey = "Personal"

from onecv import website
#print(h.makeSectionWithItems(jsonObj[sectionKey], sectionKey))
#print(h.makeSectionWithKeyValues(jsonObj[sectionKey], sectionKey))

websiteStr = website.makeWebsite(jsonObj)

with open('test.html', 'w') as outfile:
   outfile.write(websiteStr)
