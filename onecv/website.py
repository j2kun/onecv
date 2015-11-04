import re
from os.path import join
from pkg_resources import resource_string

from .templates.html import templates as tmpl
from .utils import defaultSections, organizeItems, report

itemHTML = resource_string(__name__,
      join('templates','html','item-template.html')).decode("utf-8")
sectionHTML = resource_string(__name__,
      join('templates','html','section-template.html')).decode("utf-8")
websiteHTML = resource_string(__name__,
      join('templates','html','website-template.html')).decode("utf-8")
websiteCSS = resource_string(__name__,
      join('templates','html','style.css')).decode("utf-8")
DEFAULT_TEMPLATE_KEY = 'genericItem'


def small(s):
   return '<span class="small-details">%s</span>' % s

def link(text, href):
   return '<a href="{href}">{text}</a>'.format(href=href, text=text)

def divwrap(value):
   return '<div>%s</div>' % value

# makeItem: {string: string} string -> {string: string/int}
# produce a key-value pair of strings ready for sorting and insertion into
# the itemHTML template, along with the importance of the item.
def makeItem(item, sectionKey):
   def missingKeys(x, debug=True):
      result = [k for k in re.findall('{(.*?)}', x) if k not in item]
      if debug and len(result) > 0:
         for k in result:
            report(k, item)

      return result

   if sectionKey not in tmpl.itemTemplates:
      lhs, rhs = tmpl.itemTemplates[DEFAULT_TEMPLATE_KEY]
   else:
      lhs, rhs = tmpl.itemTemplates[sectionKey]

   if 'link' in item and 'title' in item:
      item['title'] = link(item['title'], item['link'])

   if '\n' in rhs:
      rhsLines = rhs.strip().split('\n')
      rhsLines = [x for x in rhsLines if not missingKeys(x)]

      finalRHS = '\n'.join([divwrap(line) if i == 0 else divwrap(small(line))
        for i,line in enumerate(rhsLines)])
   else:
      finalRHS = divwrap(rhs)

   imp = item['importance'] if 'importance' in item else 1
   return {'key': lhs.format_map(item), 'value': finalRHS.format_map(item),
         'importance': imp}


def makeSectionWithItems(items, sectionKey, importanceThreshold=999):
   print("Writing %s" % sectionKey)

   madeItems = [makeItem(item, sectionKey) for item in items]
   madeItems = organizeItems(madeItems, importanceThreshold)

   formattedItems = '\n'.join([itemHTML.format_map(item)
         for item in madeItems])

   return sectionHTML.format(key=sectionKey, items=formattedItems)


def makeKeyValueItem(key, value):
   if 'http' in value:
      return (key, link(value,value))
   elif len(value) > 100:
      return (key, small(value))
   else:
      return (key, value)


# section is a list of dicts with only one key-value pair
# no need to sort because things are already in order
def makeSectionWithKeyValues(section, sectionKey):
   print("Writing %s" % sectionKey)

   items = [makeKeyValueItem(*list(d.items())[0]) for d in section]
   formattedItems = '\n'.join([itemHTML.format(key=k, value=v)
      for (k,v) in items])

   return sectionHTML.format(key=sectionKey, items=formattedItems)


defaultItemSections = [
   'Education',
   'Publications',
   'Preprints',
   'Talks',
   'Professional Programs',
   'Service',
   'Awards',
   'Teaching',
   'Other'
]

def makeWebsite(jsonObj, sections=defaultSections, importanceThreshold=999):
   personal = jsonObj['Personal']
   name = [x for x in personal if 'Name' in x][0]['Name']

   sections = ([makeSectionWithKeyValues(personal, 'Personal')] +
               [makeSectionWithItems(jsonObj[sec], sec, importanceThreshold)
                  for sec in sections if sec in jsonObj])

   return websiteHTML.format(name=name, style=websiteCSS,
      sections='\n'.join(sections))

