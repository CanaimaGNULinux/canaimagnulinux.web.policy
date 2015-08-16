# -*- coding: utf-8 -*-

from Products.ATContentTypes.lib import constraintypes
from Products.CMFPlacefulWorkflow.PlacefulWorkflowTool import WorkflowPolicyConfig_id
from plone import api
from plone.i18n.normalizer import idnormalizer
import logging

logger = logging.getLogger('canaimagnulinux.web.policy')


def _add_id(structure):
    """ Add a key for the id as the normalized title, if it does not exists. """
    for item in structure:
        item.setdefault('id', idnormalizer.normalize(item['title'], 'es'))
        if '_children' in item:
            item['_children'] = _add_id(item['_children'])
    return structure


def set_workflow_policy(obj):
    """ Change the workflow object using CMFPlacefulWorkflow. """

    obj.manage_addProduct['CMFPlacefulWorkflow'].manage_addWorkflowPolicyConfig()
    pc = getattr(obj, WorkflowPolicyConfig_id)
    pc.setPolicyIn(policy='one-state')
    logger.info('Workflow changed for element {0}'.format(obj.getId()))


def createFolder(context, title, allowed_types=['Topic'], exclude_from_nav=False):
    """ Create a folder in the context specified by default,
        the folder contains collections (Topic).

        >>> createFolder(site, u'Documentos', allowed_types=['File', 'Folder', 'Link', 'Image', 'Document'])
    """

    id = idnormalizer.normalize(title, 'es')
    if not hasattr(context, id):
        context.invokeFactory('Folder', id=id, title=title)
        folder = context[id]
        folder.setConstrainTypesMode(constraintypes.ENABLED)
        folder.setLocallyAllowedTypes(allowed_types)
        folder.setImmediatelyAddableTypes(allowed_types)
        # set_workflow_policy(folder)
        if exclude_from_nav:
            folder.setExcludeFromNav(True)
        folder.reindexObject()
    else:
        folder = context[id]
        folder.setLocallyAllowedTypes(allowed_types)
        folder.setImmediatelyAddableTypes(allowed_types)
        # reindexamos para que el catálogo se entere de los cambios
        folder.reindexObject()


def createCollection(folder, title, type, subject, genre='Current', section=None):
    """ Create a collection of Articles items published, which belong
        gender and the specified section; sorts them in descending
        by date of publication, and assigns a default view.

        >>> createCollection(folder=obj_target, title=title, type=types, subject=subjects, genre='Current', section='Actividades')
    """

    # workflowTool = api.portal.get_tool(name='portal_workflow')
    collection = api.content.create(type='Collection', title=title, container=folder)
    collection.setTitle(title)

    query = []
    # tipo de contenido
    query.append({'i': 'portal_type',
                  'o': 'plone.app.querystring.operation.selection.is',
                  'v': [type]})

    # categoría
    if subject is not None:

        query.append({'i': 'Subject',
                      'o': 'plone.app.querystring.operation.selection.is',
                      'v': [subject]})

    if 'collective.nitf.content' in type:

        # género
        if genre is not None:

            query.append({'i': 'genre',
                          'o': 'plone.app.querystring.operation.selection.is',
                          'v': [genre]})

        # sección
        if section is not None:

            query.append({'i': 'section',
                          'o': 'plone.app.querystring.operation.selection.is',
                          'v': [section]})

    # estado
    query.append({'i': 'review_state',
                  'o': 'plone.app.querystring.operation.selection.is',
                  'v': ['published']})

    # orden
    sort_on = u'effective'

    # vista por defecto
    default_view = 'standard_view'

    collection.query = query
    collection.sort_on = sort_on
    collection.setLayout(default_view)

    # Publicamos
    api.content.transition(collection, 'publish')

    # reindexamos para que el catálogo se entere de los cambios
    collection.reindexObject()
    logger.info('Created the {0} Section'.format(collection))


def createLink(context, title, link):
    """ Create and publish a link in the given context.

        >>> createLink(site, u'Software libre', 'http://www.softwarelibre.gob.ve/')
    """

    id = idnormalizer.normalize(title, 'es')
    if not hasattr(context, id):
        context.invokeFactory('Link', id=id, title=title, remoteUrl=link)


def createPloneSoftwareCenter(context, title):
    """ Creates a PloneSoftwareCenter in the given context.

        >>> createPloneSoftwareCenter(u'Descargas', exclude_from_nav=False)
    """

    id = idnormalizer.normalize(title, 'es')
    if not hasattr(context, id):
        context.invokeFactory('PloneSoftwareCenter', id=id, title=title)


def createCollage(context, title):
    """ Create and publish a Collage in the given context. """
    id = idnormalizer.normalize(title, 'es')
    if not hasattr(context, id):
        context.invokeFactory('Collage', id=id, title=title)
