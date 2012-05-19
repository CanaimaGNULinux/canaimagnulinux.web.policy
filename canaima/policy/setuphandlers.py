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


def install_dependencies(portal):
    """Instala las dependencias del namespace Products.
    """
    
    qi = getToolByName(portal, 'portal_quickinstaller')
    for product in PRODUCT_DEPENDENCIES:
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


def configure_site_title(portal):
    """Define el titulo del sitio creado.
    """
    if portal.title.lower() == "site" or portal.title.lower()== "plone site":
        portal.title = "Portal Canaima GNU/Linux"
        portal.description = "Portal de la meta distribución Canaima GNU/Linux"
        logger.info("Configured Site Title and Description.")
    else:
        logger.info("Site title has already been changed, so NOT changing site title or description.")


#def importZEXPs(context):
#    '''   '''
#    if context.readDataFile("canaima.policy_various.txt") is None:
#        return
#    
#    portal = context.getSite()
#    if checkIfImport():
#        performImportToPortal(portal)


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
    
    install_dependencies(portal)
    remove_default_content(portal)
    create_site_structure(portal)
    configure_site_title(portal)
    
