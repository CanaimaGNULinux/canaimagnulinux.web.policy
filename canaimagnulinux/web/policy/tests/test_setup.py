# -*- coding: utf-8 -*-

"""This is an integration "unit" test. It uses PloneTestCase, but does not
use doctest syntax.

You will find lots of examples of this type of test in CMFPlone/tests, for 
example.
"""

from unittest import TestSuite, makeSuite

from Products.CMFCore.utils import getToolByName

from canaimagnulinux.web.policy.config import PROJECTNAME, DEPENDENCIES
from canaimagnulinux.web.policy.tests.base import CanaimaPolicyTestCase

class TestSetup(CanaimaPolicyTestCase):
    """The name of the class should be meaningful. This may be a class that
    tests the installation of a particular product.
    """
    
    def afterSetUp(self):
        """This method is called before each single test. It can be used to
        set up common state. Setup that is specific to a particular test 
        should be done in that test method.
        """
        self.qi = getToolByName(self.portal, 'portal_quickinstaller')

    def beforeTearDown(self):
        """This method is called after each single test. It can be used for
        cleanup, if you need it. Note that the test framework will roll back
        the Zope transaction at the end of each test, so tests are generally
        independent of one another. However, if you are modifying external
        resources (say a database) or globals (such as registering a new
        adapter in the Component Architecture during a test), you may want to
        tear things down here.
        """

    def test_installed(self):
        """
        This method test the default GenericSetup profile of this package.
        """
        self.addProfile('%s:default'% (PROJECTNAME))

    def test_dependencies_installed(self):
        """
        This method test that dependencies products are installed of this package.
        """
        for p in DEPENDENCIES:
            self.failUnless(self.qi.isProductInstalled(p),
                            '%s not installed' % p)

def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    suite = TestSuite()
    suite.addTest(makeSuite(TestSetup))
    return suite
