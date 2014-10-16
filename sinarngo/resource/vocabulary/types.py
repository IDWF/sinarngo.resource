from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class Types(grok.GlobalUtility):
    grok.name('sinarngo.resource.types')
    grok.implements(IVocabularyFactory)

    _terms = [
        dict(   value = 'application',
            title = 'Application or Product'),
        dict(
            value = 'data',
            title = u'Data, Surveys'
            ),
        dict( 
            value = 'legislation',
            title = u'Legislation, Regulations',
        ),
        dict( 
            value = 'media',
            title = u'Interview, Panel, Presentation',
        ),
        dict(
            value = 'periodical',
            title = 'Newsletter, Journal',
        ),
        dict( value = 'policy',
          title = u'Policy, Strategy or Plan',
        ),
        dict(
             value = 'project',
             title = u'Project',
         ),
        dict(
             value = 'research',
             title = u'Research reports, working paper',
         ),
        dict(
            value = 'training',
            title = u'Training Material, Guides'
        ),
            ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
