# -*- coding: utf-8 -*-

"""
This is an integration "unit" test for Site Structure
"""

import unittest

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from Products.CMFCore.utils import getToolByName

from canaimagnulinux.web.policy.testing import INTEGRATION_TESTING

class SiteStructureTestCase(unittest.TestCase):
    """
    The class that tests the Plone Site Structure was created.
    """

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']
        self.folder.invokeFactory('Document', 'd1',)
        self.d1 = self.folder['d1']

#    def test_portal_title(self):
        
        # This is a simple test. The method needs to start with the name
        # 'test'. 

        # Look at the Python unittest documentation to learn more about hte
        # kinds of assertion methods which are available.

        # PloneTestCase has some methods and attributes to help with Plone.
        # Look at the PloneTestCase documentation, but briefly:
        # 
        #   - self.portal is the portal root
        #   - self.folder is the current user's folder
        #   - self.logout() "logs out" so that the user is Anonymous
        #   - self.setRoles(['Manager', 'Member']) adjusts the roles of the current user
        
#        self.assertEqual("Plone site", self.portal.getProperty('title'))

    def test_able_to_add_document(self):
        new_id = self.folder.invokeFactory('Document', 'my-page')
        self.assertEqual('my-page', new_id)
        
    # Keep adding methods here, or break it into multiple classes or
    # multiple files as appropriate. Having tests in multiple files makes
    # it possible to run tests from just one package:
    #
    #   ./bin/test -s canaimagnulinux.web.policy -t test_integration_unit
