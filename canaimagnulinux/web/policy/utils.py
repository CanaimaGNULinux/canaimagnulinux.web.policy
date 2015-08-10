# -*- coding: utf-8 -*-

from plone.i18n.normalizer import idnormalizer


def _add_id(structure):
    """ Add a key for the id as the normalized title, if it does not exists. """
    for item in structure:
        item.setdefault('id', idnormalizer.normalize(item['title'], 'es'))
        if '_children' in item:
            item['_children'] = _add_id(item['_children'])
    return structure


def createCollage(context, title):
    """ Create and publish a Collage in the given context. """
    id = idnormalizer.normalize(title, 'es')
    if not hasattr(context, id):
        context.invokeFactory('Collage', id=id, title=title)
