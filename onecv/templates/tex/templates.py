'''
   This file contains basic templates for all the sections in a CV.
'''

educationItem = (
   "{when}",
   '''{{{institution}}}
      {{}}
      {{{degree} in {subject}.}}
      {{{comments}}}
      {{}}'''
)

publicationItem = (
   "{when}",
   '''{{{title}}}
      {{{authors}}}
      {{{venue}}}
      {{}}
      {{}}'''
)

preprintItem = (
   "",
   '''{{{title}}}
      {{}}
      {{{authors}}}
      {{}}
      {{{comments}}}'''
)

talksItem = (
   "{when}",
   '''{{{title}}}
      {{{venue}}}
      {{{label}}}
      {{}}
      {{{comments}}}'''
)

workExperienceItem = (
   "{when}",
   '''{{{title}}}
      {{{organization}}}
      {{}}
      {{}}
      {{{comments}}}'''
)

serviceItem = (
   "{when}",
   '''{{{title}}}
      {{{event}}}
      {{{organization}}}
      {{}}
      {{{comments}}}'''
)

teachingItem = (
   "{course}",
   '''{{{type}}}
      {{{institution}}}
      {{{when}}}
      {{}}
      {{{comments}}}'''
)

awardsItem = (
   "{when}",
   '''{{{title}}}
      {{{comments}}}
      {{Granted by {granter}}}
      {{}}
      {{Monetary value of {monetary-value}}}'''
)

contractWorkItem = (
   "{when}",
   '''{{{type}}}
      {{{title}}}
      {{{organization}}}
      {{}}
      {{{comments}}}'''
)

genericItem = (
   "{name}",
   '''{{{title}}}
      {{}}
      {{{comments}}}
      {{}}
      {{}}'''
)

genericDateItem = (
   "{when}",
   '''{{{title}}}
      {{}}
      {{{comments}}}
      {{}}
      {{}}'''
)

itemTemplates = {
   "Education": educationItem,
   "Publications": publicationItem,
   "Preprints": preprintItem,
   "Talks": talksItem,
   "Professional Programs": workExperienceItem,
   "Work Experience": workExperienceItem,
   "Contract Work": contractWorkItem,
   "Service": serviceItem,
   "Teaching": teachingItem,
   "Awards": awardsItem,
   "Programming": genericItem,
   "Posters": genericDateItem,
   "Other": genericItem
}
