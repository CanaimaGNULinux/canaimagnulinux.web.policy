# -*- coding: utf-8 -*-

"""
Contains constants used by setuphandler.py
"""

# from canaimagnulinux.web.policy import CanaimaPolicyMF as _

PROJECTNAME = 'canaimagnulinux.web.policy'

PRODUCT_DEPENDENCIES = [
    'plone.api',
    'Products.CMFPlacefulWorkflow',
    'plone.app.ldap',
    'plone.app.caching',
    'cioppino.twothumbs',
    'plone.contentratings',
    'collective.geo.usersmap',
    'collective.googleanalytics',
    'collective.googlenews',
    'collective.disqus',
    'collective.facebook.portlets',
    'collective.twitter.portlets',
    'collective.twitter.tweet',
    'sc.social.like',
    'collective.nitf',
    'collective.upload',
    'collective.polls',
    'collective.cover',
    'Products.Doormat',
    'Products.PloneFormGen',
    # 'Products.PloneSoftwareCenter',
    'Products.PloneServicesCenter',
    'Products.ArchAddOn',
    'Products.FacultyStaffDirectory',
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
