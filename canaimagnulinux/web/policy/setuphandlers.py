# -*- coding: utf-8 -*-

from plone import api
# TODO: estandarizar el uso de una de las dos opciones
from plone.i18n.normalizer import idnormalizer
from Products.ATContentTypes.lib import constraintypes
from Products.CMFPlacefulWorkflow.PlacefulWorkflowTool import WorkflowPolicyConfig_id
from canaimagnulinux.web.policy.config import PROJECTNAME, DEPENDENCIES, MAILHOST_CONFIGURATION

import logging
logger = logging.getLogger(PROJECTNAME)

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

def disable_mail_host(portal):
    """
    """
    smtphost = ""
    try:
        mailHost = getattr(portal,'MailHost')
        
        if mailHost <> None:
            smtphost = mailHost.smtp_host
            mailHost.smtp_host = ""
            logger.info("Disabling configured smtp host before reinstalling: {0}".format(smtphost,))
    except AttributeError:
        smtphost = ""
    
    return smtphost

def install_dependencies(portal):
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

def remove_default_content(portal):
    """
    Remove the default Plone content.
    """
    #removable = ['Members', 'news', 'events', 'front-page']
    removable = ['news', 'events', 'front-page']
    for item in removable:
        if hasattr(portal, item):
            try:
                api.content.delete(obj=portal[item])
                logger.info('Deleted {0} item'.format(item))
            except AttributeError:
                logger.info("No {0} item detected. Hmm... strange. Continuing...".format(item))

def create_site_structure(portal):
    """
    Create the Canaima GNU/Linux Web site structure.
    """
    createFolder(portal, u'Novedades',
                 allowed_types=['Event', 'News'],
                 exclude_from_nav=False)

    immediatelyAddableTypes = ['Event', 'News']
    locallyAllowedTypes = ['Folder','Event', 'News']

    novedades = portal['novedades']
    novedades.setLocallyAllowedTypes(locallyAllowedTypes)
    novedades.setImmediatelyAddableTypes(immediatelyAddableTypes)
    logger.info("Created the {0} item".format(novedades))

#    novedades2 = api.content.create(
#        type='Folder',
#        title='Novedades 2',
#        container=portal)
#    logger.info("Created %s item with plone.api" % novedades2)
#    novedades2 = portal['novedades-2']
#    novedades2.setLocallyAllowedTypes(locallyAllowedTypes)
#    novedades2.setImmediatelyAddableTypes(immediatelyAddableTypes)
#    logger.info("Allowed Types by %s item" % novedades2)
    
#    createPloneSoftwareCenter(u'Descargas',
#                 exclude_from_nav=False)
    
    createFolder(portal, u'Documentos', allowed_types=['File', 'Folder', 'Link', 'Image', 'Document'])
    portal['documentos'].setLayout('folder_listing')
    
    createLink(portal, u'Proyectos', 'http://proyectos.canaima.softwarelibre.gob.ve/')
#    obj = api.content.create(
#        type='Link',
#        title='Github',
#        container=portal)
#    assert obj.id == 'github'
#    logger.info('Link created with plone.api')
    logger.info('Site structure created')

def configure_site_properties(portal):
    """
    Set the Site Title, Description and Properties
    """
    properties = api.portal.get_tool(name='portal_properties')
    memberdata = api.portal.get_tool(name='portal_memberdata')
    
    # Site Title and Description.
    if portal.title == None or portal.title != None:
        portal.title = "Portal Canaima GNU/Linux"
        portal.description = "Portal de la meta distribución Canaima GNU/Linux"
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

def configure_mail_host(portal):
    """
    Configuration for MailHost tool
    """
    try:
        mailHost = getattr(portal,'MailHost')
        
        if MAILHOST_CONFIGURATION["configure"]:
            logger.info("Starting Mail Configuration changes")
            if mailHost.smtp_host == '':
                mailHost.smtp_host = MAILHOST_CONFIGURATION["smtphost"]
                logger.info(mailHost.smtp_host)
            if mailHost.smtp_port == None:
                mailHost.smtp_port = MAILHOST_CONFIGURATION["smtpport"]
                logger.info(mailHost.smtp_port)
            if portal.email_from_name == '':
                portal.email_from_name = MAILHOST_CONFIGURATION["fromemailname"]
                logger.info(portal.email_from_name)
            if portal.email_from_address == '':
                portal.email_from_address = MAILHOST_CONFIGURATION["fromemailaddress"]
                logger.info(portal.email_from_address)
            logger.info("Mail Configuration is Done!")

    except AttributeError:
        pass

def enable_mail_host(portal, smtphost):
    """
    Enabling SMTP configuration host
    """
    try:
        mailHost = getattr(portal,'MailHost')
        
        if mailHost <> None and smtphost != "":
            mailHost.smtp_host = smtphost
            logger.info("Enabling configured smtp host after reinstallation: {0}".format(smtphost,))
    except AttributeError:
        pass

def clear_and_rebuild_catalog(portal):
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
    clear_and_rebuild_catalog(portal)
