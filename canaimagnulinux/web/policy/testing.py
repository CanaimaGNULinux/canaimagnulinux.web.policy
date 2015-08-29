# -*- coding: utf-8 -*-

from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2


class Fixture(PloneSandboxLayer):

    """
    This layer is the Test class base.

    Check out all tests on this package:

    ./bin/test -s canaimagnulinux.web.policy --list-tests
    """

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """
            http://iswwwup.com/t/4f0cd268f62d/plone-unit-tests-do-not-load-dependency-package-profile.html
            https://github.com/collective/collective.rcse/blob/master/collective/rcse/testing.py
        """
        # Load ZCML

        import Products.Doormat
        self.loadZCML(package=Products.Doormat)

        import Products.FacultyStaffDirectory
        self.loadZCML(package=Products.FacultyStaffDirectory)

        import Products.PloneFormGen
        self.loadZCML(package=Products.PloneFormGen)

        import Products.PloneServicesCenter
        self.loadZCML(package=Products.PloneServicesCenter)

        import Products.PloneSoftwareCenter
        self.loadZCML(package=Products.PloneSoftwareCenter)

        import Products.membrane
        self.loadZCML(package=Products.membrane)

        import Products.Relations
        self.loadZCML(package=Products.Relations)

        import plone.app.ldap
        self.loadZCML(package=plone.app.ldap)

        import canaimagnulinux.userdata
        self.loadZCML(package=canaimagnulinux.userdata)

        import canaimagnulinux.web.policy
        self.loadZCML(package=canaimagnulinux.web.policy)

        import canaimagnulinux.web.theme
        self.loadZCML(package=canaimagnulinux.web.theme)

        import collective.cover
        self.loadZCML(package=collective.cover)

        import collective.geo.usersmap
        self.loadZCML(package=collective.geo.usersmap)

        import collective.googleanalytics
        self.loadZCML(package=collective.googleanalytics)

        import collective.googlenews
        self.loadZCML(package=collective.googlenews)

        import collective.disqus
        self.loadZCML(package=collective.disqus)

        import collective.facebook.portlets
        self.loadZCML(package=collective.facebook.portlets)

        import collective.nitf
        self.loadZCML(package=collective.nitf)

        import collective.opendata
        self.loadZCML(package=collective.opendata)

        import collective.polls
        self.loadZCML(package=collective.polls)

        import collective.twitter.portlets
        self.loadZCML(package=collective.twitter.portlets)

        import collective.twitter.tweet
        self.loadZCML(package=collective.twitter.tweet)

        import collective.upload
        self.loadZCML(package=collective.upload)

        import sc.social.like
        self.loadZCML(package=sc.social.like)

        # import Products.my
        # self.loadZCML(package=Products.my)
        # z2.installProduct(app, 'Products.my')  # initialize

        # Install products that use an old-style initialize() function
        z2.installProduct(app, 'Products.CMFPlacefulWorkflow')
        z2.installProduct(app, 'Products.Doormat')
        z2.installProduct(app, 'Products.PloneFormGen')
        z2.installProduct(app, 'Products.PloneServicesCenter')
        z2.installProduct(app, 'Products.PloneSoftwareCenter')
        z2.installProduct(app, 'Products.PythonField')
        z2.installProduct(app, 'Products.Relations')
        z2.installProduct(app, 'Products.membrane')
        z2.installProduct(app, 'Products.TALESField')
        z2.installProduct(app, 'Products.TemplateFields')
        z2.installProduct(app, 'canaimagnulinux.web.policy')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup

        # set the default workflow
        workflow_tool = portal['portal_workflow']
        workflow_tool.setDefaultChain('simple_publication_workflow')
        # XXX: plone-content profiles installs also portlets
        #      it should be better just to add the portlets instead
        #      of adding all content and then deleting it
        self.applyProfile(portal, 'Products.CMFPlone:plone-content')
        # install the policy package
        self.applyProfile(portal, 'canaimagnulinux.web.policy:default')

    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'Products.CMFPlacefulWorkflow')
        z2.uninstallProduct(app, 'Products.Doormat')
        z2.uninstallProduct(app, 'Products.PloneFormGen')
        z2.uninstallProduct(app, 'Products.PloneServicesCenter')
        z2.uninstallProduct(app, 'Products.PloneSoftwareCenter')
        z2.uninstallProduct(app, 'Products.PythonField')
        z2.uninstallProduct(app, 'Products.Relations')
        z2.uninstallProduct(app, 'Products.membrane')
        z2.uninstallProduct(app, 'Products.TALESField')
        z2.uninstallProduct(app, 'Products.TemplateFields')
        z2.uninstallProduct(app, 'canaimagnulinux.web.policy')

FIXTURE = Fixture()

"""
We use this base for all the tests in this package. If necessary,
we can put common utility or setup code in here. This applies to unit
test cases.
"""
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='canaimagnulinux.web.policy:Integration'
)

"""
We use this for functional integration tests. Again, we can put basic
common utility or setup code in here.
"""
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='canaimagnulinux.web.policy:Functional'
)

"""
We use this for functional integration tests with robot framework. Again,
we can put basic common utility or setup code in here.
"""
ROBOT_TESTING = FunctionalTesting(
    bases=(FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name='canaimagnulinux.web.policy:Robot',
)
