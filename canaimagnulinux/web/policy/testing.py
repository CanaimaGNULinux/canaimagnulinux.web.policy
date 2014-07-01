# -*- coding: utf-8 -*-

"""
This layer is the Test class base.

Check out all tests on this package:

./bin/test -s canaimagnulinux.web.policy --list-tests
"""

from plone.testing.z2 import ZSERVER_FIXTURE, installProduct, uninstallProduct

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.testing import Layer
from zope.configuration import xmlconfig

class Fixture(Layer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):

        # Load ZCML
        import canaimagnulinux.web.policy
        self.loadZCML(package=canaimagnulinux.web.policy)
        xmlconfig.file(
            'configure.zcml',
            canaimagnulinux.web.policy,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        installProduct(app, 'canaimagnulinux.web.policy')

    def tearDownZope(self, app):
        # Uninstall products installed above
        uninstallProduct(app, 'canaimagnulinux.web.policy')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, 'canaimagnulinux.web.policy:default')

FIXTURE = Fixture()

"""
We use this base for all the tests in this package. If necessary,
we can put common utility or setup code in here. This applies to unit 
test cases.
"""
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="canaimagnulinux.web.policy:Integration"
)

"""
We use this for functional integration tests. Again, we can put basic 
common utility or setup code in here.
"""
ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(FIXTURE, ZSERVER_FIXTURE),
    name="canaimagnulinux.web.policy:Acceptance"
)
