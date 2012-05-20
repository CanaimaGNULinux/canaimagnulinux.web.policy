# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.lib import constraintypes

# TODO: estandarizar el uso de una de las dos opciones
from plone.i18n.normalizer import idnormalizer

from Products.CMFPlacefulWorkflow.PlacefulWorkflowTool import WorkflowPolicyConfig_id

from canaima.policy.utils import checkIfImport, performImportToPortal
from canaima.policy.config import *

from Products.GenericSetup.context import Logger,SetupEnviron
obj = SetupEnviron()
logger = obj.getLogger(PROJECTNAME)

#def importZEXPs(context):
#    '''   '''
#    if context.readDataFile("canaima.policy_various.txt") is None:
#        return
#    
#    portal = context.getSite()
#    if checkIfImport():
#        performImportToPortal(portal)


def set_workflow_policy(obj):
    """Cambiar el workflow del objeto utilizando CMFPlacefulWorkflow.
    """
    obj.manage_addProduct['CMFPlacefulWorkflow'].manage_addWorkflowPolicyConfig()
    pc = getattr(obj, WorkflowPolicyConfig_id)
    pc.setPolicyIn(policy='one-state')
    logger.info('Workflow changed for element %s' % obj.getId())


def createFolder(context, title, allowed_types=['Topic'], exclude_from_nav=False):
    """Crea una carpeta en el contexto especificado por omisión, 
    la carpeta contiene colecciones (Topic).
    """
    id = idnormalizer.normalize(title, 'es')
    if not hasattr(context, id):
        context.invokeFactory('Folder', id=id, title=title)
        folder = context[id]
        folder.setConstrainTypesMode(constraintypes.ENABLED)
        folder.setLocallyAllowedTypes(allowed_types)
        folder.setImmediatelyAddableTypes(allowed_types)
        set_workflow_policy(folder)
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
    """Crea y publica un vínculo en el contexto dado.
    """
    id = idnormalizer.normalize(title, 'es')
    if not hasattr(context, id):
        context.invokeFactory('Link', id=id, title=title, remoteUrl=link)


def createPloneSoftwareCenter(context, title):
    """Crea un PloneSoftwareCenter en el contexto dado.
    """
    id = idnormalizer.normalize(title, 'es')
    if not hasattr(context, id):
        context.invokeFactory('PloneSoftwareCenter', id=id, title=title)

def createCollage(context, title):
    """Crea un Collage en el contexto dado..
    """
    id = idnormalizer.normalize(title, 'es')
    if not hasattr(context, id):
        context.invokeFactory('Collage', id=id, title=title)

def disable_mail_host(portal):
    """
    """
    smtphost = ""
    try:
        mailHost = getattr(portal,'MailHost')
        
        if mailHost <> None:
            smtphost = mailHost.smtp_host
            mailHost.smtp_host = ""
            logger.info("Disabling configured smtp host before reinstalling : %s" % (smtphost,))
    except AttributeError:
        smtphost = ""
    
    return smtphost

def install_dependencies(portal):
    """Instala las dependencias del namespace Products.
    """
    
    qi = getToolByName(portal, 'portal_quickinstaller')
    for product in DEPENDENCIES:
        if not qi.isProductInstalled(product):
            qi.installProduct(product)
            logger.info('Installed %s' % product)
        else:
            qi.reinstallProducts([product])
            logger.info('Reinstalled %s' % product)


def remove_default_content(portal):
    """Borra el contenido creado en la instalación de Plone.
    """
    #removable = ['Members', 'news', 'events', 'front-page']
    removable = ['news', 'events', 'front-page']
    for item in removable:
        if hasattr(portal, item):
            try:
                portal.manage_delObjects([item])
                logger.info("Deleted %s item" % item)
            except AttributeError:
                logger.info("No %s item detected. Hmm... strange. Continuing..." % item)


def create_site_structure(portal):
    """Crea la estructura del sitio de Canaima GNU/Linux.
    """
    createFolder(portal, u'Novedades',
                 allowed_types=['Event', 'News'],
                 exclude_from_nav=False)

    immediatelyAddableTypes = ['Event', 'News']
    locallyAllowedTypes = ['Folder','Event', 'News']
    novedades = portal['novedades']
    novedades.setLocallyAllowedTypes(locallyAllowedTypes)
    novedades.setImmediatelyAddableTypes(immediatelyAddableTypes)
    
#    createPloneSoftwareCenter(u'Descargas',
#                 exclude_from_nav=False)
    
    createFolder(portal, u'Documentos', allowed_types=['File', 'Folder', 'Link', 'Image', 'Document'])
    portal['documentos'].setLayout('folder_listing')
    
    createLink(portal, u'Proyectos', 'http://proyectos.canaima.softwarelibre.gob.ve/')

    logger.info('Site structure created')


def configure_site_properties(portal):
    """Define el titulo del sitio creado.
    """
    properties = getToolByName(portal, 'portal_properties')
    memberdata = getToolByName(portal, 'portal_memberdata')
    
    if portal.title.lower() == "site" or portal.title.lower()== "plone site":
        portal.title = "Portal Canaima GNU/Linux"
        portal.description = "Portal de la meta distribución Canaima GNU/Linux"
        logger.info("Configured Site Title and Description.")
    else:
        logger.info("Site title has already been changed, so NOT changing site title or description.")
    
#    properties.
    properties.site_properties.enable_livesearch = False
    properties.site_properties.localTimeFormat = '%d %b %Y'
    properties.site_properties.default_language = 'es'
    memberdata.language = 'es'
    logger.info("Configured Site properties is done!")

def configure_mail_host(portal):
    """
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
                
            logger.info("Done with Mail Configuration")
    
    except AttributeError:
        pass

def enable_mail_host(portal, smtphost):
    """
    """
    try:
        mailHost = getattr(portal,'MailHost')
        
        if mailHost <> None and smtphost != "":
            mailHost.smtp_host = smtphost
            logger.info("Enabling configured smtp host after reinstallation: %s" % (smtphost,))
    except AttributeError:
        pass

def clear_and_rebuild_catalog(portal):
    """
    """
    pc = portal.portal_catalog
    pc.clearFindAndRebuild()


def setupVarious(context):
    ''' miscellaneous import steps for setup '''
    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.
    
    if context.readDataFile('canaima.policy_various.txt') is None:
        return
    
    # Add additional setup code here
    
    portal = context.getSite()
    old_smtphost = disable_mail_host(portal)#<-- Do this first so that reinstallation will not fire any notifications if any
    
    install_dependencies(portal)
    remove_default_content(portal)
    create_site_structure(portal)
    configure_site_properties(portal)
    configure_mail_host(portal)
    enable_mail_host(portal, old_smtphost) #<-- Do this last so that mail smtp host configured before reinstallation will be maintained.
    clear_and_rebuild_catalog(portal)
    
