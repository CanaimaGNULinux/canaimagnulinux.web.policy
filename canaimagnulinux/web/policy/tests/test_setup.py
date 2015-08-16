# -*- coding: utf-8 -*-

""" This is an integration "unit" test. """

from canaimagnulinux.web.policy.config import DEPENDENCIES as ZOPE2_STYLE_PRODUCTS
from canaimagnulinux.web.policy.config import PROFILE_ID
from canaimagnulinux.web.policy.config import PROJECTNAME
from canaimagnulinux.web.policy.testing import INTEGRATION_TESTING

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.registry.interfaces import IRegistry

from zope.component import getUtility

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
        self.registry = getUtility(IRegistry)


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


class DependenciesSettingsTestCase(BaseTestCase):
    """ Ensure package dependencies are properly configured. """

    def test_collective_upload_settings(self):
        from collective.upload.interfaces import IUploadSettings
        settings = self.registry.forInterface(IUploadSettings)
        expected = 'gif, jpeg, jpg, png, pdf, txt, ods, odt, odp, html, csv, zip, tgz, bz2'
        self.assertEqual(settings.upload_extensions, expected)
        self.assertEqual(settings.max_file_size, 10485760)
        self.assertEqual(settings.resize_max_width, 3872)
        self.assertEqual(settings.resize_max_height, 3872)

    def test_nitf_settings(self):
        from collective.nitf.controlpanel import INITFSettings
        settings = self.registry.forInterface(INITFSettings)
        self.assertEqual(settings.available_genres, [u'Actuality', u'Anniversary', u'Current', u'Exclusive', u'From the Scene', u'Interview', u'Opinion', u'Profile'])
        self.assertEqual(settings.available_sections, set([u'Canaima', u'Novedades', u'Comunidad', u'Soporte y Aprendizaje', u'Soluciones', u'Descargas']))
        self.assertEqual(settings.default_genre, u'Current')
        self.assertEqual(settings.default_section, u'Novedades')

    def test_nitf_google_news(self):
        from collective.googlenews.interfaces import GoogleNewsSettings
        settings = self.registry.forInterface(GoogleNewsSettings)
        self.assertEqual(settings.portal_types, ['collective.nitf.content'])

    def test_geo_settings(self):
        from collective.geo.settings.interfaces import IGeoSettings
        import decimal
        settings = self.registry.forInterface(IGeoSettings)
        self.assertEqual(settings.default_layers, [u'osm'])
        self.assertEqual(settings.zoom, decimal.Decimal(6))
        self.assertEqual(settings.longitude, decimal.Decimal(6.423750000000001))
        self.assertEqual(settings.latitude, decimal.Decimal(-66.58973000000024))

    def test_geo_usersmap_settings(self):
        from collective.geo.usersmap.interfaces import IUsersMapPreferences
        settings = self.registry.forInterface(IUsersMapPreferences)
        self.assertEqual(settings.title, u'Mapa de usuarios del portal')
        self.assertEqual(settings.description, u'Este mapa muestra las ubicaciones de los usuarios del portal.')
        self.assertEqual(settings.user_properties, [u'description', u'email'])

    def test_disqus_settings(self):
        from collective.disqus.interfaces import IDisqusSettings
        settings = self.registry.forInterface(IDisqusSettings)
        self.assertEqual(settings.activated, True)
        self.assertEqual(settings.developer_mode, False)
        self.assertEqual(settings.forum_short_name, 'canaimagnulinux')
        self.assertEqual(settings.access_token, '15796f758e24404bb965521fe85f9aa8')
        self.assertEqual(settings.app_public_key, 'iroSK4ud2I2sLMYAqMNI56tqI1fjbCm3XQ8T5HhZGTSQfAnj9m7yBNr9GqcycA8M')
        self.assertEqual(settings.app_secret_key, 'q3xfSJDNYvi5uwMq9Y6Whyu3xy6luxKN9PFsruE2X2qMz98xuX23GK7sS5KnIAtb')


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
