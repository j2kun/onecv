'''
   This file contains basic templates for all the sections in a CV.
'''


educationItem = (
   "{when}",
   "{degree} in {subject}\n{institution}. {comments}"
)

publicationItem = (
   "{when}",
   "{title}. {authors}. {venue}."
)

preprintItem = (
   "",
   "{title}. {authors}."
)

talksItem = (
   "{when}",
   "{title}\n{venue}. {label}."
)

workExperienceItem = (
   "{when}",
   "{title}. {organization}.\n{comments}"
)

serviceItem = (
   "{when}",
   "{title}, {event}.\n{organization}."
)

teachingItem = (
   "{course}",
   "{type}, {institution}, {when}.\n{comments}"
)

awardsItem = (
   "{when}",
   "{title}.\n{comments}. Granted by {granter}.\nMonetary value of {monetary-value}.",
)

contractWorkItem = (
   "{when}",
   "{type}, {title}. {organization}.\n{comments}"
)

genericItem = (
   "{name}",
   "{title}\n{comments}"
)

genericDateItem = (
   "{when}",
   "{title}\n{comments}"
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
