import re
from sys import stderr

defaultSections = [
   'Education',
   'Publications',
   'Preprints',
   'Talks',
   'Professional Programs',
   'Service',
   'Awards',
   'Teaching',
   'Posters',
   'Other'
]

def datelike(astring):
   return bool(re.search(r'\d{4}', astring))

def maxYear(aString):
   return max(int(x) for x in re.findall(r'\d{4}', str(aString)))

def minYear(aString):
   return min(int(x) for x in re.findall(r'\d{4}', str(aString)))

def report(missingKey, data):
   stderr.write("Note: missing key %r; skipping...\n" % missingKey)

# organizeItems: [{string: string}], string -> [{string, string}]
# make a list of items and sort them by (importance, date), if the keys are
# dates, otherwise sort just by importance
def organizeItems(items, threshold):
   def dateKey(d):
      return (int(d['importance']), -maxYear(d['key']), -minYear(d['key']))

   if all(datelike(d['key']) for d in items):
      items.sort(key=dateKey)
   else:
      items.sort(key=lambda d: int(d['importance']))

   return [x for x in items if x['importance'] <= threshold]

