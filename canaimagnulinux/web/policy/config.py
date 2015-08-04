# -*- coding: utf-8 -*-

"""
Contains constants used by setuphandler.py
"""

# from canaimagnulinux.web.policy import CanaimaPolicyMF as _

PROJECTNAME = 'canaimagnulinux.web.policy'

PRODUCT_DEPENDENCIES = [
    'Products.ArchAddOn',
    'Products.CMFPlacefulWorkflow',
    'Products.Doormat',
    'Products.FacultyStaffDirectory',
    'Products.PloneFormGen',
    'Products.PloneServicesCenter',
    # 'Products.PloneSoftwareCenter',
    'plone.api',
    'plone.contentratings',
    'plone.app.caching',
    'plone.app.ldap',
    'cioppino.twothumbs',
    'collective.cover',
    'collective.disqus',
    'collective.facebook.portlets',
    'collective.geo.usersmap',
    'collective.googleanalytics',
    'collective.googlenews',
    'collective.nitf',
    'collective.polls',
    'collective.twitter.portlets',
    'collective.twitter.tweet',
    'collective.upload',
    'sc.social.like',
]

PACKAGE_DEPENDENCIES = [
    'canaimagnulinux.web.theme',
]

DEPENDENCIES = PRODUCT_DEPENDENCIES + PACKAGE_DEPENDENCIES

MAILHOST_CONFIGURATION = {'configure': True,
                          'smtphost': 'localhost',
                          'smtpport': 25,
                          'fromemailname': 'Sitio Web Canaima GNU/Linux',
                          'fromemailaddress': 'soporte@canaima.softwarelibre.gob.ve'}
