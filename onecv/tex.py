import re
from os.path import join
from pkg_resources import resource_string

from .templates.tex import templates as tmpl
from .utils import defaultSections, organizeItems

itemTEX = resource_string(__name__,
      join('templates','tex','item-template.tex')).decode("utf-8")
lineItemTEX = resource_string(__name__,
      join('templates','tex','line-item-template.tex')).decode("utf-8")
sectionTEX = resource_string(__name__,
      join('templates','tex','section-template.tex')).decode("utf-8")
cvTEX = resource_string(__name__,
      join('templates','tex','moderncv-template.tex')).decode("utf-8")

linkTEX = r'\href{{{url}}}{{\textcolor{{MidnightBlue}}{{\underline{{\textbf{{{text}}}}}}}}}'

def link(text, href):
   return linkTEX.format(url=href, text=text.replace('~', r'\textasciitilde{}'))

# makeItem: {string: string} string -> {string: string/int}
# produce a key-value pair of strings ready for sorting and insertion into
# the itemHTML template, along with the importance of the item.
def makeItem(item, sectionKey):
   def missingKeys(x):
      return any((k not in item) for k in re.findall('{+([^{}]+)}+', x))

   if 'comments' in item:
      item['comments'] = item['comments'].strip('.')

   lhs, rhs = tmpl.itemTemplates[sectionKey]
   if 'link' in item and 'title' in item:
      item['title'] = link(item['title'], item['link'])

   if '\n' in rhs:
      rhsLines = rhs.strip().split('\n')
      rhsLines = [(x if not missingKeys(x) else '{{}}') for x in rhsLines]
      finalRHS = '\n'.join(rhsLines)
   else:
      finalRHS = rhs

   imp = item['importance'] if 'importance' in item else 1
   return {'key': lhs.format_map(item), 'value': finalRHS.format_map(item),
         'importance': imp}


def makeSectionWithItems(items, sectionKey, importanceThreshold=999):
   print("Writing %s" % sectionKey)

   madeItems = [makeItem(item, sectionKey) for item in items]
   madeItems = organizeItems(madeItems, importanceThreshold)

   formattedItems = '\n'.join([itemTEX.format_map(item)
         for item in madeItems])

   return sectionTEX.format(key=sectionKey, items=formattedItems)


def makeKeyValueItem(key, value):
   if 'http' in value:
      return (key, link(value,value))
   else:
      return (key, value)


# section is a list of dicts with only one key-value pair
# no need to sort because things are already in order
def makeSectionWithKeyValues(section, sectionKey):
   print("Writing %s" % sectionKey)

   items = [makeKeyValueItem(*list(d.items())[0]) for d in section]
   formattedItems = '\n'.join([lineItemTEX.format(key=k, value=v)
      for (k,v) in items])

   return sectionTEX.format(key=sectionKey, items=formattedItems)


def makeTex(jsonObj, sections=defaultSections, importanceThreshold=999):
   personal = jsonObj['Personal']
   name = [x for x in personal if 'Name' in x][0]['Name']
   email = [x for x in personal if 'Email' in x][0]['Email']

   sections = ([makeSectionWithKeyValues(personal, 'Personal')] +
               [makeSectionWithItems(jsonObj[sec], sec, importanceThreshold)
                  for sec in sections if sec in jsonObj])

   return cvTEX.format(name=name, email=email,
      sections='\n'.join(sections))

