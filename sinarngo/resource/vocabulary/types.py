from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

from sinarngo.resource import MessageFactory as _

class Types(grok.GlobalUtility):
    grok.name('sinarngo.resource.types')
    grok.implements(IVocabularyFactory)

    _terms = [
        dict(
            value = 'activity',
            title = _(u'Activity or Event Report')
            ),
        dict(
            value = 'application',
            title = _(u'Application or Product')
            ),
        dict(
            value = 'books',
            title = _(u'Books')
            ),
        dict(
            value = 'promotional',
            title = _(u'Brochure, Promotional Materials')
            ),
        dict(
            value = 'data',
            title = _(u'Data, Surveys, Fact Sheets')
            ),
        dict( 
            value = 'legislation',
            title = _(u'Legislation, Regulations')
            ),
        dict( 
            value = 'media',
            title = _(u'Interview, Panel, Presentation')
            ),
        dict(
            value = 'periodical',
            title = _(u'Newsletter, Journal')
            ),
        dict( 
            value = 'policy',
            title = _(u'Policy, Strategy or Plan')
            ),
        dict(
             value = 'project',
             title = _(u'Project')
            ),
        dict(
             value = 'research',
             title = _(u'Research reports, working paper')
            ),
        dict(
            value = 'training',
            title = _(u'Training Material, Guides, Organizing/Educational Materials')
            ),
            ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
