# -*- coding: utf-8 -*-

from Products.ATContentTypes.lib import constraintypes
# from Products.CMFDefault.exceptions import MetadataError
from Products.CMFQuickInstallerTool import interfaces as qi_interfaces
from Products.CMFPlone import interfaces as st_interfaces

from canaimagnulinux.web.policy.config import CREATORS
from canaimagnulinux.web.policy.config import DEFAULT_CONTENT
from canaimagnulinux.web.policy.config import DEFAULT_SUBJECTS
from canaimagnulinux.web.policy.config import DEPENDENCIES
from canaimagnulinux.web.policy.config import HIDDEN_PRODUCTS
from canaimagnulinux.web.policy.config import HIDDEN_PROFILES
from canaimagnulinux.web.policy.config import MAILHOST_CONFIGURATION
from canaimagnulinux.web.policy.config import PROFILE_ID as PROFILE_NAME
from canaimagnulinux.web.policy.config import PROJECTNAME
from canaimagnulinux.web.policy.config import SITE_STRUCTURE

from plone import api
from zope.interface import implements

import logging
logger = logging.getLogger(PROJECTNAME)


class HiddenProducts(object):
    """ Hidden Products in portal_quickinstaller """
    implements(qi_interfaces.INonInstallable)

    def getNonInstallableProducts(self):
        products = []
        products = [p for p in HIDDEN_PRODUCTS]
        return products


class HiddenProfiles(object):
    """ Hidden profiles from the home screen to create the site """
    implements(st_interfaces.INonInstallable)

    def getNonInstallableProfiles(self):
        return HIDDEN_PROFILES


def constrain_types(folder, allowed_types):
    """ Constrain addable types in folder. """

    folder.setConstrainTypesMode(constraintypes.ENABLED)
    folder.setImmediatelyAddableTypes(allowed_types)
    folder.setLocallyAllowedTypes(allowed_types)


def createContentType(type, folder, title, subject, state, exclude_from_nav):
    """ Create common Content Types. """

    obj = api.content.create(type=type, title=title, container=folder)
    obj.setTitle(title)
    obj.reindexObject('Title')

    if subject is not None:
        obj.setSubject(subject)
        obj.reindexObject('Subject')
        logger.info('The subjects is done!')

    if exclude_from_nav is not False:
        obj.setExcludeFromNav(True)
        logger.info('The element was excluded from navigation')

    if state is not None:
        api.content.transition(obj, state)
        logger.info('The workflow transition is done')
    else:
        pass

    logger.info('Created the {0} item'.format(obj))


def disable_mail_host(site):
    """ Disabling configured smtp host before reinstalling """

    smtphost = ''
    try:
        mailHost = api.portal.get_tool('MailHost')

        if mailHost is not None:
            smtphost = mailHost.smtp_host
            mailHost.smtp_host = ''
            logger.info('Disabling configured smtp host before reinstalling: {0}'.format(smtphost,))
    except AttributeError:
        smtphost = ''

    return smtphost


def install_dependencies(site):
    """ Install Products dependencies. """

    qi = api.portal.get_tool(name='portal_quickinstaller')
    for product in DEPENDENCIES:
        if not qi.isProductInstalled(product):
            qi.installProduct(product)
            logger.info('Installed {0}'.format(product))
        else:
            qi.reinstallProducts([product])
            logger.info('Reinstalled {0}'.format(product))


def exclude_from_navigation_default_content(site):
    """ Exclude from navigation "Members" section. """

    members = site['Members']
    members.setExcludeFromNav(True)
    # site['Members'].setExcludeFromNav(True)
    logger.info('Excluded from Nav {0} item'.format(site))


def remove_default_content(site):
    """ Remove the default Plone content. """

    for item in DEFAULT_CONTENT:
        if hasattr(site, item):
            try:
                api.content.delete(obj=site[item])
                logger.info('Deleted {0} item'.format(item))
            except AttributeError:
                logger.info('No {0} item detected. Hmm... strange. Continuing...'.format(item))


def create_site_structure(site, structure):
    """ Create and publish new site structure as defined in config.py."""

    for item in structure:
        id = item['id']
        title = item['title']
        description = item.get('description', u'')
        subject = item.get('subjects', u'')
        if id not in site:
            # creators are defined?
            if 'creators' not in item:
                item['creators'] = CREATORS
            obj = api.content.create(site, **item)
            # publish private content or make a workflow transition
            if item['type'] not in ['Image', 'File']:
                if '_transition' not in item and api.content.get_state(obj) == 'private':
                    api.content.transition(obj, 'publish')
                elif item.get('_transition', None):
                    api.content.transition(obj, item['_transition'])
            # constrain types in folder?
            if '_addable_types' in item:
                constrain_types(obj, item['_addable_types'])
            # the content has more content inside? create it
            if '_children' in item:
                create_site_structure(obj, item['_children'])
            # add an image to all news items
            if obj.portal_type == 'News Item':
                if 'image' in item:
                    obj.setImage(item['image'])
            # set the default view to object
            if '_layout' in item:
                obj.setLayout(item['_layout'])
            # XXX: workaround for https://github.com/plone/plone.api/issues/99
            obj.setTitle(title)
            obj.setDescription(description)
            obj.setSubject(subject)
            obj.reindexObject()
            logger.debug(u'{0} fue creado y publicado'.format(title))
        else:
            logger.debug(u'Sin crear elemento \'{0}\'; ya existente este contenido'.format(title))
    logger.info('All site structure created')


def set_site_default_page(site):
    """ Set front page as site default page. """
    site.setDefaultPage('portada')
    # site.manage_changeProperties(**{"default_page": 'portada'})
    logger.info(u'Set item as default page for Portal')


def set_default_subject_metadata(site):
    """ Set default subjects as Website metadata. """
    # mdtool = api.portal.get_tool(name='portal_metadata')

    # Set up a MetadataTool element policy for events
    # try:
    #     mdtool.addElementPolicy(
    #         element='Subject',
    #         # content_type='Event',
    #         content_type='<default>',
    #         is_required=0,
    #         supply_default=0,
    #         default_value='',
    #         enforce_vocabulary=0,
    #         allowed_vocabulary=DEFAULT_SUBJECTS,
    #         REQUEST=None)
    #     logger.info(u'Set all default subjects as Website metadata')
    # except MetadataError:
    #     logger.info(u'Without set all default subjects as Website metadata')

    pm = site.portal_metadata
    objdcmi = pm.DCMI
    if objdcmi is not None:
        objdcmi.updateElementPolicy('Subject', '<default>', 0, 0, "", 0, DEFAULT_SUBJECTS)
        logger.info('Updated default subjects as %s' % (DEFAULT_SUBJECTS,))


def set_support_section(site):
    """ Rename the "support" folder as "Servicios empresariales" section. """

    obj = site['support']
    api.content.rename(obj=obj, new_id='servicios-empresariales')
    title = u'Servicios empresariales'
    description = 'Existen diversas áreas de servicios que ofrecen los proveedores de servicios comerciales en Canaima.'
    obj.setTitle(title)
    obj.setDescription(description)
    obj.reindexObject('Title')
    obj.reindexObject('Description')
    logger.info('Renamed the {0} item'.format(obj))

    obj_source = site['servicios-empresariales']
    obj_target = site['soporte-y-aprendizaje']['mercado-de-servicios']
    api.content.move(source=obj_source, target=obj_target)
    logger.info('Moved from {0} to {1} item'.format(obj_source, obj_target))

    obj = site['soporte-y-aprendizaje']['mercado-de-servicios']['servicios-empresariales']['providers']
    api.content.rename(obj=obj, new_id='proveedores')
    title = u'Proveedores'
    obj.setTitle(title)
    obj.reindexObject('Title')
    logger.info('Renamed the {0} item'.format(obj))

    obj = site['soporte-y-aprendizaje']['mercado-de-servicios']['servicios-empresariales']['sites']
    api.content.delete(obj=obj)
    logger.info('Deleted the {0} item'.format(obj))

    obj = site['soporte-y-aprendizaje']['mercado-de-servicios']['servicios-empresariales']['case-studies']
    api.content.delete(obj=obj)
    logger.info('Deleted the {0} item'.format(obj))

    logger.info('All "Servicios empresariales" section is done!')


def set_footer_site(site):
    """ Rename the doormat item as "Pie de pagina" section. """

    obj = site['doormat']
    api.content.rename(obj=obj, new_id='pie-de-pagina')
    title = u'Pie de pagina'
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Renamed the {0} item'.format(obj))

    # Column 1
    title = u'Columna 1'
    obj = site['pie-de-pagina']['column-1']
    api.content.rename(obj=obj, new_id='columna-1')
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Renamed the {0} item'.format(obj))

    obj = site['pie-de-pagina']['columna-1']['section-1']
    api.content.rename(obj=obj, new_id='canaima')
    title = u'Canaima'
    obj.setTitle(title)
    obj.reindexObject('Title')
    api.content.transition(obj, 'publish')
    logger.info('Renamed the {0} item'.format(obj))

    obj = site['pie-de-pagina']['columna-1']['canaima']['document-1']
    api.content.delete(obj=obj)
    logger.info('Deleted the {0} item'.format(obj))

    title = u'Conozca Canaima'
    obj_target = site['pie-de-pagina']['columna-1']['canaima']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Características'
    obj_target = site['pie-de-pagina']['columna-1']['canaima']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'¿Qué hay de nuevo?'
    obj_target = site['pie-de-pagina']['columna-1']['canaima']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Testimonios'
    obj_target = site['pie-de-pagina']['columna-1']['canaima']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Casos de éxito'
    obj_target = site['pie-de-pagina']['columna-1']['canaima']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 2
    title = u'Columna 2'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Soluciones'
    obj_target = site['pie-de-pagina']['columna-2']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Sector gobierno'
    obj_target = site['pie-de-pagina']['columna-2']['soluciones']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Sector comunal'
    obj_target = site['pie-de-pagina']['columna-2']['soluciones']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Geomática'
    obj_target = site['pie-de-pagina']['columna-2']['soluciones']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 3
    title = u'Columna 3'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Soporte y Aprendizaje'
    obj_target = site['pie-de-pagina']['columna-3']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Necesita ayuda'
    obj_target = site['pie-de-pagina']['columna-3']['soporte-y-aprendizaje']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Quiero aprender'
    obj_target = site['pie-de-pagina']['columna-3']['soporte-y-aprendizaje']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Consultoría'
    obj_target = site['pie-de-pagina']['columna-3']['soporte-y-aprendizaje']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Mercado de servicios'
    obj_target = site['pie-de-pagina']['columna-3']['soporte-y-aprendizaje']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 4
    title = u'Columna 4'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Descargas'
    obj_target = site['pie-de-pagina']['columna-4']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Obtener Canaima'
    obj_target = site['pie-de-pagina']['columna-4']['descargas']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Obtener códigos fuentes'
    obj_target = site['pie-de-pagina']['columna-4']['descargas']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Complementos del RNA'
    obj_target = site['pie-de-pagina']['columna-4']['descargas']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 5
    title = u'Columna 5'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Comunidad'
    obj_target = site['pie-de-pagina']['columna-5']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Unirte a Canaima'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Estar conectado'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Organización'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Equipos'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Forja'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Reuniones'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Grupo'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Opinión'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Galería de diseño'
    obj_target = site['pie-de-pagina']['columna-5']['comunidad']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 6
    title = u'Columna 6'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Novedades'
    obj_target = site['pie-de-pagina']['columna-6']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Blogs'
    obj_target = site['pie-de-pagina']['columna-6']['novedades']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Comunidad'
    obj_target = site['pie-de-pagina']['columna-6']['novedades']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Gobierno'
    obj_target = site['pie-de-pagina']['columna-6']['novedades']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Discusiones'
    obj_target = site['pie-de-pagina']['columna-6']['novedades']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    title = u'Actividades'
    obj_target = site['pie-de-pagina']['columna-6']['novedades']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    logger.info(u'Set the footer item for Portal')


def configure_site_properties(site):
    """ Set the Site Title, Description and Properties """

    properties = api.portal.get_tool(name='portal_properties')
    memberdata = api.portal.get_tool(name='portal_memberdata')

    # Site Title and Description.
    if site.title is None or site.title is not None:
        site.title = 'Portal Canaima GNU/Linux'
        site.description = 'Portal de la meta distribución Canaima GNU/Linux'
        logger.info('Configured Site Title and Description!')
    else:
        logger.info('Site title has already been changed, so NOT changing site title or description.')

    # Site properties.
    properties.site_properties.enable_livesearch = False
    properties.site_properties.localTimeFormat = '%d %b %Y'
    properties.site_properties.default_language = 'es'
    logger.info('Configured the Site properties!')

    # Member data properties.
    memberdata.language = 'es'
    logger.info('Configured member data properties!')


def configure_mail_host(site):
    """ Configuration for MailHost tool """

    try:
        mailHost = api.portal.get_tool('MailHost')

        if MAILHOST_CONFIGURATION['configure']:
            logger.info('Starting Mail Configuration changes')
            if mailHost.smtp_host == '':
                mailHost.smtp_host = MAILHOST_CONFIGURATION['smtphost']
                logger.info(mailHost.smtp_host)
            if mailHost.smtp_port is None:
                mailHost.smtp_port = MAILHOST_CONFIGURATION['smtpport']
                logger.info(mailHost.smtp_port)
            if site.email_from_name == '':
                site.email_from_name = MAILHOST_CONFIGURATION['fromemailname']
                logger.info(site.email_from_name)
            if site.email_from_address == '':
                site.email_from_address = MAILHOST_CONFIGURATION['fromemailaddress']
                logger.info(site.email_from_address)
            logger.info('Mail Configuration is Done!')

    except AttributeError:
        pass


def enable_mail_host(site, smtphost):
    """ Enabling SMTP configuration host """

    try:
        mailHost = api.portal.get_tool('MailHost')

        if mailHost is not None and smtphost != '':
            mailHost.smtp_host = smtphost
            logger.info('Enabling configured smtp host after reinstallation: {0}'.format(smtphost,))
    except AttributeError:
        pass


def setup_nitf_settings():
    """ Custom settings for collective.nitf """

    api.portal.set_registry_record(
        'collective.nitf.controlpanel.INITFSettings.available_genres',
        [u'Actuality', u'Anniversary', u'Current', u'Exclusive', u'From the Scene', u'Interview', u'Opinion', u'Profile']
    )
    api.portal.set_registry_record(
        'collective.nitf.controlpanel.INITFSettings.available_sections',
        set([u'Canaima', u'Novedades', u'Comunidad', u'Soporte y Aprendizaje', u'Soluciones', u'Descargas'])
    )
    api.portal.set_registry_record(
        'collective.nitf.controlpanel.INITFSettings.default_genre',
        u'Current'
    )
    api.portal.set_registry_record(
        'collective.nitf.controlpanel.INITFSettings.default_section',
        u'Novedades'
    )
    logger.info('Configured collective.nitf content type')


def setup_nitf_google_news():
    """ Setup collective.nitf content type in Google News """

    api.portal.set_registry_record(
        'collective.googlenews.interfaces.GoogleNewsSettings.portal_types',
        ['collective.nitf.content']
    )
    logger.info('Configured collective.nitf with collective.googlenews')


def setup_geo_settings():
    """ Custom settings for collective.geo """

    import decimal
    api.portal.set_registry_record(
        'collective.geo.settings.interfaces.IGeoSettings.default_layers',
        [u'osm']
    )
    api.portal.set_registry_record(
        'collective.geo.settings.interfaces.IGeoSettings.zoom',
        decimal.Decimal(6)
    )
    api.portal.set_registry_record(
        'collective.geo.settings.interfaces.IGeoSettings.longitude',
        decimal.Decimal(6.423750000000001)
    )
    api.portal.set_registry_record(
        'collective.geo.settings.interfaces.IGeoSettings.latitude',
        decimal.Decimal(-66.58973000000024)
    )
    logger.info('Configured collective.geo')


def setup_geo_usersmap_settings():
    """ Custom settings for collective.geo.usersmap """

    api.portal.set_registry_record(
        'collective.geo.usersmap.interfaces.IUsersMapPreferences.title',
        u'Mapa de usuarios del portal'
    )
    api.portal.set_registry_record(
        'collective.geo.usersmap.interfaces.IUsersMapPreferences.description',
        u'Este mapa muestra las ubicaciones de los usuarios del portal.'
    )
    api.portal.set_registry_record(
        'collective.geo.usersmap.interfaces.IUsersMapPreferences.user_properties',
        [u'description', u'email']
    )
    logger.info('Configured collective.geo.usersmap')


def setup_disqus_settings():
    """ Custom settings for collective.disqus """

    api.portal.set_registry_record(
        'collective.disqus.interfaces.IDisqusSettings.activated',
        True
    )
    api.portal.set_registry_record(
        'collective.disqus.interfaces.IDisqusSettings.developer_mode',
        False
    )
    api.portal.set_registry_record(
        'collective.disqus.interfaces.IDisqusSettings.forum_short_name',
        'canaimagnulinux'
    )
    api.portal.set_registry_record(
        'collective.disqus.interfaces.IDisqusSettings.access_token',
        u'15796f758e24404bb965521fe85f9aa8'
    )
    api.portal.set_registry_record(
        'collective.disqus.interfaces.IDisqusSettings.app_public_key',
        u'iroSK4ud2I2sLMYAqMNI56tqI1fjbCm3XQ8T5HhZGTSQfAnj9m7yBNr9GqcycA8M'
    )
    api.portal.set_registry_record(
        'collective.disqus.interfaces.IDisqusSettings.app_secret_key',
        u'q3xfSJDNYvi5uwMq9Y6Whyu3xy6luxKN9PFsruE2X2qMz98xuX23GK7sS5KnIAtb'
    )
    logger.info('Configured collective.disqus')


def import_registry_settings():
    """ Import registry settings; we need to do this before other stuff here,
    like using a cover layout defined there.

    XXX: I don't know if there is other way to do this on ZCML or XML.
    """
    PROFILE_ID = 'profile-{0}'.format(PROFILE_NAME)
    setup = api.portal.get_tool('portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'plone.app.registry')
    logger.info('Imported registry settings from GenericSetup profile.')


def clear_and_rebuild_catalog(site):
    """ Clear and rebuild catalog """

    catalog = api.portal.get_tool(name='portal_catalog')
    catalog.clearFindAndRebuild()
    logger.info('Clear and rebuild catalog is done!')


def setupVarious(context):
    """ Miscellaneous import steps for setup """
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
    exclude_from_navigation_default_content(portal)
    remove_default_content(portal)
    create_site_structure(portal, SITE_STRUCTURE)
    set_site_default_page(portal)
    # set_default_subject_metadata(portal)
    set_support_section(portal)
    set_footer_site(portal)
    configure_site_properties(portal)
    configure_mail_host(portal)
    # Do this last so that mail smtp host configured before reinstallation will be maintained.
    enable_mail_host(portal, old_smtphost)
    setup_nitf_settings()
    setup_nitf_google_news()
    setup_geo_settings()
    setup_geo_usersmap_settings()
    setup_disqus_settings()
    import_registry_settings()
    clear_and_rebuild_catalog(portal)
