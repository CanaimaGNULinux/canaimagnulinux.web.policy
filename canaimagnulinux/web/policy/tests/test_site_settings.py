# -*- coding: utf-8 -*-

"""
This is an integration "unit" test for Site Settings
"""

import unittest

from Products.CMFCore.utils import getToolByName

from canaimagnulinux.web.policy.testing import INTEGRATION_TESTING

class SiteSettingsTestCase(unittest.TestCase):
    """
    The class that tests the Plone Site Settings.
    """
    
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.portal_memberdata = getToolByName(self.portal, 'portal_memberdata')
        self.portal_properties = getToolByName(self.portal, 'portal_properties')
        self.mailhost = getToolByName(self.portal, 'MailHost')
    
    def test_portal_title(self):
        """
        This method test that ensure the portal title is the same.
        """
        self.assertTrue("Portal Canaima GNU/Linux", self.portal.getProperty('title'))
        
    def test_portal_description(self):
        """
        This method test that ensure the portal description is the same.
        """
        self.assertTrue("Portal de la meta distribución Canaima GNU/Linux", 
                        self.portal.getProperty('description'))

    def test_portal_memberdata_language(self):
        """
        This method test that ensure the memberdata language is the same.
        """
        self.assertTrue(
                "es",
                self.portal_memberdata.getProperty('language')
        )

    def test_local_time_format(self):
        """
        This method test that ensure the local time format is the same.
        """
        self.assertEqual(self.portal_properties.site_properties.localTimeFormat, '%d %b %Y')

    def test_default_language(self):
        """
        This method test that ensure the default language is the same.
        """
        self.assertEqual(self.portal_properties.site_properties.default_language, 'es')

    def test_livesearch_is_disabled(self):
        """
        This method test that ensure the livesearch is disabled.
        """
        self.assertFalse(self.portal_properties.site_properties.enable_livesearch)

    def test_mailhost_smtp_host(self):
        """
        This method test that ensure the mail host is the same.
        """
        self.assertTrue(self.mailhost.smtp_host, 'localhost')
