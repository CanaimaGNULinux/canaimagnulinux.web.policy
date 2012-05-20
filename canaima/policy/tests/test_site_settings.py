# -*- coding: utf-8 -*-

"""This is an integration "unit" test. It uses PloneTestCase, but does not
use doctest syntax.

You will find lots of examples of this type of test in CMFPlone/tests, for 
example.
"""

from unittest import TestSuite, makeSuite

from Products.CMFCore.utils import getToolByName

from canaima.policy.tests.base import CanaimaPolicyTestCase

class TestSetup(CanaimaPolicyTestCase):
    """The name of the class should be meaningful. This may be a class that
    tests the installation of a particular product.
    """
    
    def afterSetUp(self):
        """This method is called before each single test. It can be used to
        set up common state. Setup that is specific to a particular test 
        should be done in that test method.
        """
        self.portal_memberdata = getToolByName(self.portal, 'portal_memberdata')
        self.portal_properties = getToolByName(self.portal, 'portal_properties')
        self.mailhost = getToolByName(self.portal, 'MailHost')
        
    def beforeTearDown(self):
        """This method is called after each single test. It can be used for
        cleanup, if you need it. Note that the test framework will roll back
        the Zope transaction at the end of each test, so tests are generally
        independent of one another. However, if you are modifying external
        resources (say a database) or globals (such as registering a new
        adapter in the Component Architecture during a test), you may want to
        tear things down here.
        """
    
    def test_portal_title(self):
        """
        This method test that ensure the portal title is the same.
        """
        self.failUnless("Portal Canaima GNU/Linux", self.portal.getProperty('title'))
        
    def test_portal_description(self):
        """
        This method test that ensure the portal description is the same.
        """
        self.failUnless("Portal de la meta distribución Canaima GNU/Linux", 
                        self.portal.getProperty('description'))

    def test_portal_memberdata_language(self):
        """
        This method test that ensure the memberdata language is the same.
        """
        self.failUnless(
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
        self.failUnless(self.mailhost.smtp_host, 'localhost')

def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    suite = TestSuite()
    suite.addTest(makeSuite(TestSetup))
    return suite
