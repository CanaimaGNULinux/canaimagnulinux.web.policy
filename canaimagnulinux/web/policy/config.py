# -*- coding: utf-8 -*-

"""
Contains constants used by setuphandler.py
"""

from canaimagnulinux.web.policy import CanaimaPolicyMF as _

PROJECTNAME = 'canaimagnulinux.web.policy'

PRODUCT_DEPENDENCIES = [
    'Products.CMFPlacefulWorkflow',
#    'iservices.rssdocument',
#    'Products.Collage',
#    'collective.collage.portlets',
#    'collective.collage.rssdocument',
#    'collective.twitterportlet',
#    'Products.ExternalStorage',
#    'collective.psc.externalstorage',
#    'Products.ArchAddOn',
#    'Products.AddRemoveWidget',
#    'Products.DataGridField',
#    'Products.PloneHelpCenter',
#    'Products.contentmigration',
#    'Products.SimpleAttachment',
#    'plone.folder',
#    'Products.PloneKeywordManager',
#    'Products.Poi',
#    'Products.PloneSoftwareCenter',
    ]

PACKAGE_DEPENDENCIES = [
    'canaima.aponwaotheme',
    ]

DEPENDENCIES = PRODUCT_DEPENDENCIES + PACKAGE_DEPENDENCIES


MAILHOST_CONFIGURATION = {'configure':True,
                         'smtphost':'localhost',
                         'smtpport':25,
                         'fromemailname':'Sitio Web Canaima GNU/Linux',
                         'fromemailaddress':'soporte@canaima.softwarelibre.gob.ve'
                        }
