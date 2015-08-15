# -*- coding: utf-8 -*-

""" Contains constants used by setuphandler.py """

PROJECTNAME = 'canaimagnulinux.web.policy'
PROFILE_ID = '{0}:default'.format(PROJECTNAME)

# content created at Plone's installation
DEFAULT_CONTENT = ('front-page', 'news', 'events')

DEPENDENCIES = [
    'ArchAddOn',
    'CMFPlacefulWorkflow',
    'Doormat',
    'FacultyStaffDirectory',
    'PloneFormGen',
    'PloneServicesCenter',
    'PloneSoftwareCenter',
]

MAILHOST_CONFIGURATION = {
    'configure': True,
    'smtphost': 'localhost',
    'smtpport': 25,
    'fromemailname': 'Sitio Web Canaima GNU/Linux',
    'fromemailaddress': 'soporte@canaima.softwarelibre.gob.ve'
}
