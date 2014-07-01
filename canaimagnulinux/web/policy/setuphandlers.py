# -*- coding: utf-8 -*-

from zope.component import getUtility

from plone import api
from plone.registry.interfaces import IRegistry
from plone.i18n.normalizer import idnormalizer
from Products.ATContentTypes.lib import constraintypes
from Products.CMFPlacefulWorkflow.PlacefulWorkflowTool import WorkflowPolicyConfig_id

from collective.nitf.controlpanel import INITFSettings
from collective.googlenews.interfaces import GoogleNewsSettings
from collective.geo.settings.interfaces import IGeoSettings
from canaimagnulinux.web.policy.config import PROJECTNAME, DEPENDENCIES, MAILHOST_CONFIGURATION

import logging
logger = logging.getLogger(PROJECTNAME)

def constrain_types(folder, allowed_types):
    """Constrain addable types in folder.
    """

    folder.setConstrainTypesMode(constraintypes.ENABLED)
    folder.setImmediatelyAddableTypes(allowed_types)
    folder.setLocallyAllowedTypes(allowed_types)

def set_workflow_policy(obj):
    """
    Cambiar el workflow del objeto utilizando CMFPlacefulWorkflow.
    """

    obj.manage_addProduct['CMFPlacefulWorkflow'].manage_addWorkflowPolicyConfig()
    pc = getattr(obj, WorkflowPolicyConfig_id)
    pc.setPolicyIn(policy='one-state')
    logger.info('Workflow changed for element {0}'.format(obj.getId()))

def createFolder(context, title, allowed_types=['Topic'], exclude_from_nav=False):
    """
    Crea una carpeta en el contexto especificado por omisión,
    la carpeta contiene colecciones (Topic).
    """

    id = idnormalizer.normalize(title, 'es')
    if not hasattr(context, id):
        context.invokeFactory('Folder', id=id, title=title)
        folder = context[id]
        folder.setConstrainTypesMode(constraintypes.ENABLED)
        folder.setLocallyAllowedTypes(allowed_types)
        folder.setImmediatelyAddableTypes(allowed_types)
        #set_workflow_policy(folder)
        if exclude_from_nav:
            folder.setExcludeFromNav(True)
        folder.reindexObject()
    else:
        folder = context[id]
        folder.setLocallyAllowedTypes(allowed_types)
        folder.setImmediatelyAddableTypes(allowed_types)
        # reindexamos para que el catálogo se entere de los cambios
        folder.reindexObject()

def createLink(context, title, link):
    """
    Crea y publica un vínculo en el contexto dado.
    """

    id = idnormalizer.normalize(title, 'es')
    if not hasattr(context, id):
        context.invokeFactory('Link', id=id, title=title, remoteUrl=link)

def createPloneSoftwareCenter(context, title):
    """
    Crea un PloneSoftwareCenter en el contexto dado.
    """

    id = idnormalizer.normalize(title, 'es')
    if not hasattr(context, id):
        context.invokeFactory('PloneSoftwareCenter', id=id, title=title)

def createContentType(type, folder, title, state, exclude_from_nav):
    """
    Create common Content Types.
    """

    obj = api.content.create(type=type, title=title, container=folder)
    obj.setTitle(title)
    obj.reindexObject('Title')

    if exclude_from_nav != False:
        obj.setExcludeFromNav(True)
        logger.info("The element was excluded from navigation")

    if state != None:
        api.content.transition(obj, state)
        logger.info("The workflow transition is done")
    else:
        pass

    logger.info("Created the {0} item".format(obj))

def createCollection(folder, title, type, genre='Current', section=None):
    """ Crea una colección de Artículos de noticias publicados, que pertenecen
    al género y a la sección especificados; los ordena de forma descendente
    por fecha de publicación, y les asigna una vista por defecto.
    """

    workflowTool = api.portal.get_tool(name='portal_workflow')
    collection = api.content.create(type='Collection', title=title, container=folder)
    collection.setTitle(title)

    query = []
    # tipo de contenido
    query.append({'i': 'portal_type',
                  'o': 'plone.app.querystring.operation.selection.is',
                  'v': [type]})
    #              'v': ['collective.nitf.content']})

    # género
    #query.append({'i': 'genre',
    #              'o': 'plone.app.querystring.operation.selection.is',
    #              'v': [genre]})

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

def disable_mail_host(site):
    """
    """

    smtphost = ""
    try:
        mailHost = api.portal.get_tool('MailHost')
        
        if mailHost != None:
            smtphost = mailHost.smtp_host
            mailHost.smtp_host = ""
            logger.info("Disabling configured smtp host before reinstalling: {0}".format(smtphost,))
    except AttributeError:
        smtphost = ""
    
    return smtphost

def install_dependencies(site):
    """
    Install Products dependencies.
    """

    qi = api.portal.get_tool(name='portal_quickinstaller')
    for product in DEPENDENCIES:
        if not qi.isProductInstalled(product):
            qi.installProduct(product)
            logger.info('Installed {0}'.format(product))
        else:
            qi.reinstallProducts([product])
            logger.info('Reinstalled {0}'.format(product))

def remove_default_content(site):
    """
    Remove the default Plone content.
    """

    removable = ['news', 'events', 'front-page']
    for item in removable:
        if hasattr(site, item):
            try:
                api.content.delete(obj=site[item])
                logger.info('Deleted {0} item'.format(item))
            except AttributeError:
                logger.info("No {0} item detected. Hmm... strange. Continuing...".format(item))

def create_site_structure(site):
    """
    Create the Canaima GNU/Linux Web site structure.
    """

    # Exclude from navigation "Members" section
    members = site['Members']
    members.setExcludeFromNav(True)
    #site['Members'].setExcludeFromNav(True)
    logger.info("Excluded from Nav {0} item".format(site))

    # Rename "Servicios empresariales" section
    obj = site['support']
    api.content.rename(obj=obj, new_id='servicios-empresariales')
    title = u'Servicios empresariales'
    obj.setTitle(title)
    obj.reindexObject('Title')
    logger.info("Renamed the {0} item".format(obj))

    # Rename "Pie de pagina" section
    obj = site['doormat']
    api.content.rename(obj=obj, new_id='pie-de-pagina')
    title = u'Pie de pagina'
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info("Renamed the {0} item".format(obj))

    # Column 1
    title = u'Columna 1'
    obj = site['pie-de-pagina']['column-1']
    api.content.rename(obj=obj, new_id='columna-1')
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info("Renamed the {0} item".format(obj))

    obj = site['pie-de-pagina']['columna-1']['section-1']
    api.content.rename(obj=obj, new_id='canaima')
    title = u'Canaima'
    obj.setTitle(title)
    obj.reindexObject('Title')
    api.content.transition(obj, 'publish')
    logger.info("Renamed the {0} item".format(obj))

    obj = site['pie-de-pagina']['columna-1']['canaima']['document-1']
    api.content.delete(obj=obj)
    logger.info("Deleted the {0} item".format(obj))

    title = u'Conozca Canaima'
    obj_target = site['pie-de-pagina']['columna-1']['canaima']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Características'
    obj_target = site['pie-de-pagina']['columna-1']['canaima']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'¿Qué hay de nuevo?'
    obj_target = site['pie-de-pagina']['columna-1']['canaima']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Testimonios'
    obj_target = site['pie-de-pagina']['columna-1']['canaima']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Casos de éxito'
    obj_target = site['pie-de-pagina']['columna-1']['canaima']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    # Column 2
    title = u'Columna 2'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Soluciones'
    obj_target = site['pie-de-pagina']['columna-2']
    createContentType('DoormatSection', obj_target, title, 'publish', False)

    title = u'Sector gobierno'
    obj_target = site['pie-de-pagina']['columna-2']['soluciones']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Sector comunal'
    obj_target = site['pie-de-pagina']['columna-2']['soluciones']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Geomática'
    obj_target = site['pie-de-pagina']['columna-2']['soluciones']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    # Column 3
    title = u'Columna 3'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Soporte y Aprendizaje'
    obj_target = site['pie-de-pagina']['columna-3']
    createContentType('DoormatSection', obj_target, title, 'publish', False)

    title = u'Necesita ayuda'
    obj_target = site['pie-de-pagina']['columna-3']['soporte-y-aprendizaje']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Quiero aprender'
    obj_target = site['pie-de-pagina']['columna-3']['soporte-y-aprendizaje']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Consultoría'
    obj_target = site['pie-de-pagina']['columna-3']['soporte-y-aprendizaje']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Mercado de servicios'
    obj_target = site['pie-de-pagina']['columna-3']['soporte-y-aprendizaje']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    # Column 4
    title = u'Columna 4'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Descargas'
    obj_target = site['pie-de-pagina']['columna-4']
    createContentType('DoormatSection', obj_target, title, 'publish', False)

    title = u'Obtener Canaima'
    obj_target = site['pie-de-pagina']['columna-4']['descargas']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Obtener códigos fuentes'
    obj_target = site['pie-de-pagina']['columna-4']['descargas']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Complementos del RNA'
    obj_target = site['pie-de-pagina']['columna-4']['descargas']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    # Column 5
    title = u'Columna 5'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Comunidad'
    obj_target = site['pie-de-pagina']['columna-5']
    createContentType('DoormatSection', obj_target, title, 'publish', False)

    title = u'Unirte a Canaima'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Estar conectado'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Organización'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Equipos'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Forja'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Reuniones'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Grupo'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Opinión'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Galería de diseño'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    # Column 6
    title = u'Columna 6'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Novedades'
    obj_target = site['pie-de-pagina']['columna-6']
    createContentType('DoormatSection', obj_target, title, 'publish', False)

    title = u'Blogs'
    obj_target = site['pie-de-pagina']['columna-6']['novedades']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Comunidad'
    obj_target = site['pie-de-pagina']['columna-6']['novedades']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Gobierno'
    obj_target = site['pie-de-pagina']['columna-6']['novedades']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Discusiones'
    obj_target = site['pie-de-pagina']['columna-6']['novedades']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    title = u'Actividades'
    obj_target = site['pie-de-pagina']['columna-6']['novedades']
    createContentType('DoormatReference', obj_target, title, 'publish', False)

    # Create "Portada" item
    title = u'Portada'
    obj = api.content.create(type='collective.cover.content', title=title, container=site)
    obj.setTitle(title)
    obj.reindexObject('Title')
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))
    site.manage_changeProperties(**{"default_page" : 'portada'})
    logger.info("Set {0} item as default page for Portal".format(obj))

    # Create "Canaima" section
    title = u'Canaima'
    obj = api.content.create(type='Folder', title=title, container=site)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'CaseStudyFolder']
    constrain_types(obj, obj_constrain_types)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Conozca Canaima'
    obj_target = site['canaima']
    createContentType('Document', obj_target, title, None, False)

    title = u'Características'
    obj_target = site['canaima']
    createContentType('Document', obj_target, title, None, False)

    title = u'¿Por qué usar Canaima?'
    obj_target = site['canaima']
    createContentType('Document', obj_target, title, None, False)

    title = u'¿Por qué Software libre?'
    obj_target = site['canaima']
    createContentType('Document', obj_target, title, None, False)

    title = u'Casos de éxitos'
    obj_target = site['canaima']
    createContentType('CaseStudyFolder', obj_target, title, None, False)

    # Create "Soluciones" section
    title = u'Soluciones'
    obj = api.content.create(type='Folder', title=title, container=site)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'Collection', 'collective.cover.content']
    constrain_types(obj, obj_constrain_types)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Sector gobierno'
    obj_target = site['soluciones']
    types = ['Document']
    createCollection(folder=obj_target, title=title, type=types, genre=None, section='Soluciones')

    title = u'Sector comunas'
    obj_target = site['soluciones']
    types = ['Document']
    createCollection(folder=obj_target, title=title, type=types, genre=None, section='Soluciones')

    title = u'Geomática'
    obj_target = site['soluciones']
    types = ['Document']
    createCollection(folder=obj_target, title=title, type=types, genre=None, section='Soluciones')

    title = u'Canaima Popular'
    obj_target = site['soluciones']
    createContentType('Document', obj_target, title, None, True)

    title = u'Canaima Educativo'
    obj_target = site['soluciones']
    createContentType('Document', obj_target, title, None, True)

    title = u'Canaima Colibri'
    obj_target = site['soluciones']
    createContentType('Document', obj_target, title, None, True)

    title = u'Canaima Comunal'
    obj_target = site['soluciones']
    createContentType('Document', obj_target, title, None, True)

    title = u'Canaima Caribay'
    obj_target = site['soluciones']
    createContentType('Document', obj_target, title, None, True)

    title = u'GeoCanaima'
    obj_target = site['soluciones']
    createContentType('Document', obj_target, title, None, True)

    # Create "Soporte y Aprendizaje" section
    title = u'Soporte y Aprendizaje'
    obj = api.content.create(type='Folder', title=title, container=site)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'ProviderFolder']
    constrain_types(obj, obj_constrain_types)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Necesito ayuda'
    obj_target = site['soporte-y-aprendizaje']
    obj = api.content.create(type='Folder', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'collective.cover.content']
    constrain_types(obj, obj_constrain_types)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Yo quiero aprender'
    obj_target = site['soporte-y-aprendizaje']
    obj = api.content.create(type='Folder', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'FSDDepartment']
    constrain_types(obj, obj_constrain_types)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Consultoría'
    obj_target = site['soporte-y-aprendizaje']
    obj = api.content.create(type='Folder', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'FSDDepartment']
    constrain_types(obj, obj_constrain_types)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Mercado de servicios'
    obj_target = site['soporte-y-aprendizaje']
    obj = api.content.create(type='Folder', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    #obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'ProviderFolder', 'FSDDepartment']
    #constrain_types(obj, obj_constrain_types)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    obj_source = site['servicios-empresariales']
    obj_target = site['soporte-y-aprendizaje']['mercado-de-servicios']
    api.content.move(source=obj_source, target=obj_target)
    logger.info("Moved from {0} to {1} item".format(obj_source, obj_target))

    obj = site['soporte-y-aprendizaje']['mercado-de-servicios']['servicios-empresariales']['providers']
    api.content.rename(obj=obj, new_id='proveedores')
    title = u'Proveedores'
    obj.setTitle(title)
    obj.reindexObject('Title')
    logger.info("Renamed the {0} item".format(obj))

    obj = site['soporte-y-aprendizaje']['mercado-de-servicios']['servicios-empresariales']['sites']
    api.content.delete(obj=obj)

    obj = site['soporte-y-aprendizaje']['mercado-de-servicios']['servicios-empresariales']['case-studies']
    api.content.delete(obj=obj)

    # Create "Descargas" section
    title = u'Descargas'
    obj = api.content.create(type='Folder', title=title, container=site)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'collective.cover.content']
    constrain_types(obj, obj_constrain_types)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Obtener Canaima'
    obj_target = site['descargas']
    obj = api.content.create(type='Folder', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'ProviderFolder', 'FSDDepartment']
    constrain_types(obj, obj_constrain_types)
    api.content.transition(obj, 'publish')
    logger.info("Created the {0} item".format(obj))

    title = u'Verifique la descarga de la imagen ISO'
    obj_target = site['descargas']
    createContentType('Document', obj_target, title, 'publish', False)

    title = u'Obtener códigos fuentes'
    obj_target = site['descargas']
    createContentType('Document', obj_target, title, 'publish', False)

    title = u'Complementos del RNA'
    obj_target = site['descargas']
    createContentType('collective.cover.content', obj_target, title, 'publish', False)

    # Create "Comunidad" section
    title = u'Comunidad'
    obj = api.content.create(type='Folder', title=title, container=site)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'FSDFacultyStaffDirectory']
    constrain_types(obj, obj_constrain_types)
    api.content.transition(obj, 'publish')
    site['comunidad'].setLayout('@@usersmap_view')
    logger.info("Created the {0} item".format(obj))

    title = u'Unirse a Canaima'
    obj_target = site['comunidad']
    createContentType('Document', obj_target, title, 'publish', False)

    title = u'Estar conectado'
    obj_target = site['comunidad']
    createContentType('Document', obj_target, title, 'publish', False)

    title = u'Organización'
    obj_target = site['comunidad']
    obj = api.content.create(type='Folder', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    api.content.transition(obj, 'publish')
    #obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'News', 'collective.cover.content']
    #constrain_types(obj, obj_constrain_types)
    logger.info("Created the {0} item".format(obj))

    title = u'Equipos'
    obj_target = site['comunidad']
    obj = api.content.create(type='Folder', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    api.content.transition(obj, 'publish')
    #obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'News', 'collective.cover.content']
    #constrain_types(obj, obj_constrain_types)
    logger.info("Created the {0} item".format(obj))

    title = u'Forja'
    obj_target = site['comunidad']
    obj = api.content.create(type='Folder', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    api.content.transition(obj, 'publish')
    obj_constrain_types = ['Document', 'File', 'Image', 'News', 'collective.cover.content']
    #constrain_types(obj, obj_constrain_types)
    logger.info("Created the {0} item".format(obj))

    title = u'Reuniones'
    obj_target = site['comunidad']
    obj = api.content.create(type='Folder', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    api.content.transition(obj, 'publish')
    #obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'News', 'collective.cover.content']
    #constrain_types(obj, obj_constrain_types)
    logger.info("Created the {0} item".format(obj))

    title = u'Grupos'
    obj_target = site['comunidad']
    #obj = api.content.create(type='FSDFacultyStaffDirectory', title=title, container=obj_target)
    obj = api.content.create(type='Folder', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    api.content.transition(obj, 'publish')
    #obj_constrain_types = ['Folder', 'Document', 'File', 'Image', 'News', 'collective.cover.content']
    #constrain_types(obj, obj_constrain_types)
    logger.info("Created the {0} item".format(obj))

    # Create "Novedades" section
    createFolder(site, u'Novedades',
                 allowed_types=['Event', 'News', 'Link', 'Collection'],
                 exclude_from_nav=False)

    immediatelyAddableTypes = ['Event', 'News']
    locallyAllowedTypes = ['Folder', 'Event', 'News', 'Link', 'Collection', 'collective.nitf.content']
    novedades = site['novedades']
    novedades.setLocallyAllowedTypes(locallyAllowedTypes)
    novedades.setImmediatelyAddableTypes(immediatelyAddableTypes)
    logger.info("Created the {0} item".format(novedades))
    
    title = u'Blogs'
    obj_target = site['novedades']
    createContentType('Link', obj_target, title, None, False)

    title = u'Comunidad'
    obj_target = site['novedades']
    types = ['collective.nitf.content']
    createCollection(folder=obj_target, title=title, type=types, genre='Current', section='Comunidad')

    title = u'Gobierno'
    obj_target = site['novedades']
    types = ['collective.nitf.content']
    createCollection(folder=obj_target, title=title, type=types, genre='Current', section='Gobierno')

    title = u'Discusiones'
    obj_target = site['novedades']
    types = ['collective.nitf.content']
    createCollection(folder=obj_target, title=title, type=types, genre='Current', section='Discusiones')

    title = u'Actividades'
    obj_target = site['novedades']
    types = ['collective.nitf.content']
    createCollection(folder=obj_target, title=title, type=types, genre='Current', section='Actividades')

#    createPloneSoftwareCenter(u'Descargas', exclude_from_nav=False)
#    createFolder(site, u'Documentos', allowed_types=['File', 'Folder', 'Link', 'Image', 'Document'])
#    site['documentos'].setLayout('folder_listing')
    
    createLink(site, u'Proyectos', 'http://proyectos.canaima.softwarelibre.gob.ve/')
    obj = site['proyectos']
    obj.setExcludeFromNav(True)
    logger.info('All site structure created')

def configure_site_properties(site):
    """
    Set the Site Title, Description and Properties
    """

    properties = api.portal.get_tool(name='portal_properties')
    memberdata = api.portal.get_tool(name='portal_memberdata')
    
    # Site Title and Description.
    if site.title == None or site.title != None:
        site.title = "Portal Canaima GNU/Linux"
        site.description = "Portal de la meta distribución Canaima GNU/Linux"
        logger.info("Configured Site Title and Description!")
    else:
        logger.info("Site title has already been changed, so NOT changing site title or description.")
    
    # Site properties.
    properties.site_properties.enable_livesearch = False
    properties.site_properties.localTimeFormat = '%d %b %Y'
    properties.site_properties.default_language = 'es'
    logger.info("Configured the Site properties!")

    # Member data properties.
    memberdata.language = 'es'
    logger.info("Configured member data properties!")

def configure_mail_host(site):
    """
    Configuration for MailHost tool
    """

    try:
        mailHost = api.portal.get_tool('MailHost')
        
        if MAILHOST_CONFIGURATION["configure"]:
            logger.info("Starting Mail Configuration changes")
            if mailHost.smtp_host == '':
                mailHost.smtp_host = MAILHOST_CONFIGURATION["smtphost"]
                logger.info(mailHost.smtp_host)
            if mailHost.smtp_port == None:
                mailHost.smtp_port = MAILHOST_CONFIGURATION["smtpport"]
                logger.info(mailHost.smtp_port)
            if site.email_from_name == '':
                site.email_from_name = MAILHOST_CONFIGURATION["fromemailname"]
                logger.info(site.email_from_name)
            if site.email_from_address == '':
                site.email_from_address = MAILHOST_CONFIGURATION["fromemailaddress"]
                logger.info(site.email_from_address)
            logger.info("Mail Configuration is Done!")

    except AttributeError:
        pass

def enable_mail_host(site, smtphost):
    """
    Enabling SMTP configuration host
    """

    try:
        mailHost = api.portal.get_tool('MailHost')
        
        if mailHost != None and smtphost != "":
            mailHost.smtp_host = smtphost
            logger.info("Enabling configured smtp host after reinstallation: {0}".format(smtphost,))
    except AttributeError:
        pass

def setup_nitf_settings():
    """
    Custom settings for collective.nitf
    """

    settings = getUtility(IRegistry).forInterface(INITFSettings, False)
    settings.available_genres = [u'Actuality', u'Anniversary', u'Current', u'Exclusive', u'From the Scene', u'Interview', u'Opinion', u'Profile']
    settings.available_sections = set([u'Canaima', u'Novedades', u'Comunidad', u'Soporte y Aprendizaje', u'Soluciones', u'Descargas'])
    settings.default_genre = u'Current'
    settings.default_section = u'Novedades'
    logger.info('Configured collective.nitf content type')

def setup_nitf_google_news():
    """
    Setup collective.nitf content type in Google News
    """

    settings = getUtility(IRegistry).forInterface(GoogleNewsSettings, False)
    settings.portal_types = ["collective.nitf.content"]
    logger.info('Configured collective.nitf with collective.googlenews')

def setup_geo_settings():
    """
    Custom settings for collective.geo.usersmap
    """

    import decimal
    settings = getUtility(IRegistry).forInterface(IGeoSettings, False)
    settings.default_layers = [u'osm']
    settings.zoom = decimal.Decimal(6)
    settings.longitude = decimal.Decimal(6.423750000000001)
    settings.latitude = decimal.Decimal(-66.58973000000024)
    logger.info('Configured collective.geo.usersmap')

def clear_and_rebuild_catalog(site):
    """
    Clear and rebuild catalog
    """

    catalog = api.portal.get_tool(name='portal_catalog')
    catalog.clearFindAndRebuild()
    logger.info("Clear and rebuild catalog is done!")

def setupVarious(context):
    """ miscellaneous import steps for setup """
    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.
    
    if context.readDataFile('canaimagnulinux.web.policy_various.txt') is None:
        return
    
    # Add additional setup code here
    portal = api.portal.get()

    # Do this first so that reinstallation will not fire any notifications if any
    old_smtphost = disable_mail_host(portal)
    install_dependencies(portal)
    remove_default_content(portal)
    create_site_structure(portal)
    configure_site_properties(portal)
    configure_mail_host(portal)
    # Do this last so that mail smtp host configured before reinstallation will be maintained.
    enable_mail_host(portal, old_smtphost)
    setup_nitf_settings()
    setup_nitf_google_news()
    setup_geo_settings()
    clear_and_rebuild_catalog(portal)
