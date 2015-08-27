# -*- coding: utf-8 -*-

""" This is an integration "unit" test. """

from canaimagnulinux.web.policy.config import DEPENDENCIES as ZOPE2_STYLE_PRODUCTS
from canaimagnulinux.web.policy.config import PROFILE_ID
from canaimagnulinux.web.policy.config import PROJECTNAME
from canaimagnulinux.web.policy.testing import FUNCTIONAL_TESTING
from canaimagnulinux.web.policy.testing import INTEGRATION_TESTING

from plone import api
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.testing.z2 import Browser

import unittest

DEPENDENCIES = [
    'ArchAddOn',
    'canaimagnulinux.web.theme',
    'cioppino.twothumbs',
    'collective.cover',
    'collective.disqus',
    'collective.facebook.portlets',
    'collective.geo.usersmap',
    'collective.googleanalytics',
    'collective.googlenews',
    'collective.nitf',
    'collective.opendata',
    'collective.polls',
    'collective.twitter.portlets',
    'collective.twitter.tweet',
    'collective.upload',
    'Doormat',
    'FacultyStaffDirectory',
    'PloneFormGen',
    'PloneServicesCenter',
    'PloneSoftwareCenter',
    'plone.api',
    'plone.contentratings',
    'plone.app.caching',
    'plone.app.ldap',
    'sc.social.like',
] + ZOPE2_STYLE_PRODUCTS


class BaseTestCase(unittest.TestCase):
    """ Base test case to be used by other tests. """

    layer = INTEGRATION_TESTING

    profile = PROFILE_ID

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.wt = self.portal['portal_workflow']
        self.st = self.portal['portal_setup']


class InstallTestCase(BaseTestCase):
    """ Ensure product is properly installed. """

    def test_installed(self):
        """ This method test the default GenericSetup profile of this package. """
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_installed(self):
        """ This method test that dependencies products are installed of this package. """
        # for p in DEPENDENCIES:
        #     self.assertTrue(
        #         self.qi.isProductInstalled(p), u'{0} not installed'.format(p))
        expected = set(DEPENDENCIES)
        installed = self.qi.listInstalledProducts(showHidden=True)
        installed = set([product['id'] for product in installed])
        result = sorted(expected - installed)

        self.assertTrue(
            result,
            'These dependencies are not installed: ' + ', '.join(result)
        )

    def test_version(self):
        """ This method test that last version for profile of this package. """
        self.assertEqual(
            self.st.getLastVersionForProfile(PROFILE_ID), (u'1000',))


class DependenciesSettingsTestCase(BaseTestCase):
    """ Ensure package dependencies are properly configured. """

    def test_collective_upload_settings(self):
        expected = 'gif, jpeg, jpg, png, pdf, txt, ods, odt, odp, html, csv, zip, tgz, bz2'
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.upload.interfaces.IUploadSettings.upload_extensions'),
            expected
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.upload.interfaces.IUploadSettings.max_file_size'),
            10485760
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.upload.interfaces.IUploadSettings.resize_max_width'),
            3872
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.upload.interfaces.IUploadSettings.resize_max_height'),
            3872
        )

    def test_nitf_settings(self):
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.nitf.controlpanel.INITFSettings.available_genres'),
            [u'Actuality', u'Anniversary', u'Current', u'Exclusive', u'From the Scene', u'Interview', u'Opinion', u'Profile']
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.nitf.controlpanel.INITFSettings.available_sections'),
            set([u'Canaima', u'Novedades', u'Comunidad', u'Soporte y Aprendizaje', u'Soluciones', u'Descargas'])
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.nitf.controlpanel.INITFSettings.default_genre'),
            u'Current'
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.nitf.controlpanel.INITFSettings.default_section'),
            u'Novedades'
        )

    def test_nitf_google_news(self):
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.googlenews.interfaces.GoogleNewsSettings.portal_types'),
            ['collective.nitf.content']
        )

    def test_google_analytics_tool(self):
        """  Test that the portal_analytics tool is created. """
        analytics_tool = api.portal.get_tool('portal_analytics')
        self.assertNotEqual(analytics_tool, None)

    def test_geo_settings(self):
        import decimal
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.geo.settings.interfaces.IGeoSettings.default_layers'),
            [u'osm']
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.geo.settings.interfaces.IGeoSettings.zoom'),
            decimal.Decimal(6)
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.geo.settings.interfaces.IGeoSettings.longitude'),
            decimal.Decimal(6.423750000000001)
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.geo.settings.interfaces.IGeoSettings.latitude'),
            decimal.Decimal(-66.58973000000024)
        )

    def test_geo_usersmap_settings(self):
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.geo.usersmap.interfaces.IUsersMapPreferences.title'),
            u'Mapa de usuarios del portal'
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.geo.usersmap.interfaces.IUsersMapPreferences.description'),
            u'Este mapa muestra las ubicaciones de los usuarios del portal.'
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.geo.usersmap.interfaces.IUsersMapPreferences.user_properties'),
            [u'description', u'email']
        )

    def test_disqus_settings(self):
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.disqus.interfaces.IDisqusSettings.activated'),
            True
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.disqus.interfaces.IDisqusSettings.developer_mode'),
            False
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.disqus.interfaces.IDisqusSettings.forum_short_name'),
            'canaimagnulinux'
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.disqus.interfaces.IDisqusSettings.access_token'),
            '15796f758e24404bb965521fe85f9aa8'
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.disqus.interfaces.IDisqusSettings.app_public_key'),
            'iroSK4ud2I2sLMYAqMNI56tqI1fjbCm3XQ8T5HhZGTSQfAnj9m7yBNr9GqcycA8M'
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.disqus.interfaces.IDisqusSettings.app_secret_key'),
            'q3xfSJDNYvi5uwMq9Y6Whyu3xy6luxKN9PFsruE2X2qMz98xuX23GK7sS5KnIAtb'
        )


class NonInstallableTestCase(unittest.TestCase):
    """Ensure non installable packages are available."""

    layer = FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_opendata_available(self):
        portal_url = self.portal.absolute_url()
        browser = Browser(self.layer['app'])

        opendata_url = '{0}/{1}'.format(portal_url, '/open-data')
        browser.open(opendata_url)
        # self.assertIn('Open Data', browser.contents)

        apidata_url = '{0}/{1}'.format(portal_url, '/apidata/cms/site_info')
        browser.open(apidata_url)
        self.assertIn('Portal Canaima GNU/Linux', browser.contents)


class UninstallTestCase(BaseTestCase):
    """ Ensure product is properly uninstalled. """

    def setUp(self):
        BaseTestCase.setUp(self)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        """ This method test the uninstall GenericSetup profile of this package. """
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_uninstalled(self):
        """ This method test that dependencies products are uninstalled. """
        pass
