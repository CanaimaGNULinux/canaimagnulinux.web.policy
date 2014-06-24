# -*- coding: utf-8 -*-

"""
This is an integration "unit" test.
"""

import unittest

from Products.CMFCore.utils import getToolByName

from canaimagnulinux.web.policy.config import PROJECTNAME, DEPENDENCIES
from canaimagnulinux.web.policy.testing import INTEGRATION_TESTING

class InstallTestCase(unittest.TestCase):
    """
    The class that tests the installation of a particular product.
    """

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed(self):
        """
        This method test the default GenericSetup profile of this package.
        """
        qi = getattr(self.portal, 'portal_quickinstaller')
        self.assertTrue(qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_installed(self):
        """
        This method test that dependencies products are installed of this package.
        """
        for p in DEPENDENCIES:
            self.failUnless(self.qi.isProductInstalled(p),
                            '%s not installed' % p)

class UninstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))
