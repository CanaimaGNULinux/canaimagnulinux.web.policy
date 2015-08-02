# -*- coding: utf-8 -*-

"""
This is an integration "unit" test for Site Structure
"""

from canaimagnulinux.web.policy.testing import INTEGRATION_TESTING

from plone import api

import unittest


class SiteStructureTestCase(unittest.TestCase):
    """
    The class that tests the Plone Site Structure was created.
    """

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.member_folder = self.portal['Member']

    def test_default_content_is_removed(self):
        existing = self.portal.objectIds()
        self.assertTrue('events' not in existing)
        self.assertTrue('front-page' not in existing)
        self.assertTrue('news' not in existing)

    def test_root_folders(self):
        existing = self.portal.objectIds()
        self.assertIn('canaima', existing)
        self.assertIn('soluciones', existing)
        self.assertIn('soporte-y-aprendizaje', existing)
        self.assertIn('descargas', existing)
        self.assertIn('comunidad', existing)
        self.assertIn('novedades', existing)
        self.assertIn('portada', existing)
        self.assertEqual(self.portal.getDefaultPage(), 'portada')
        self.assertIn('Member', existing)
        self.assertEqual(self.member_folder.getExcludeFromNav(), True)
        self.assertIn('pie-de-pagina', existing)

    def test_folder_canaima(self):
        folder = self.portal['canaima']
        self.assertEqual(folder.getTitle(), 'Canaima')
        types = ('Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'CaseStudyFolder',)
        self.assertEqual(folder.getImmediatelyAddableTypes(), types)
        self.assertEqual(folder.getLocallyAllowedTypes(), types)
        self.assertEqual(api.content.get_state(folder), 'published')
        self.assertIn('conozca-canaima', folder)
        self.assertIn('caracteristicas', folder)
        self.assertIn('por-que-usar-canaima', folder)
        self.assertIn('por-que-software-libre', folder)
        self.assertIn('casos-de-exitos', folder)

    def test_folder_soluciones(self):
        folder = self.portal['soluciones']
        self.assertEqual(folder.getTitle(), 'Soluciones')
        types = ('Folder', 'Document', 'File', 'Image', 'Collection', 'collective.cover.content',)
        self.assertEqual(folder.getImmediatelyAddableTypes(), types)
        self.assertEqual(folder.getLocallyAllowedTypes(), types)
        self.assertEqual(api.content.get_state(folder), 'published')

    def test_folder_comunidad(self):
        folder = self.portal['comunidad']
        self.assertEqual(folder.getTitle(), 'Comunidad')
        types = ('Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'FSDFacultyStaffDirectory',)
        self.assertEqual(folder.getImmediatelyAddableTypes(), types)
        self.assertEqual(folder.getLocallyAllowedTypes(), types)
        self.assertEqual(api.content.get_state(folder), 'published')
        self.assertEqual(folder.getLayout(), '@@usersmap_view')

    # def test_portal_title(self):

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

        # self.assertEqual("Plone site", self.portal.getProperty('title'))

    # def test_able_to_add_document(self):
        # new_id = self.folder.invokeFactory('Document', 'my-page')
        # self.assertEqual('my-page', new_id)

    # Keep adding methods here, or break it into multiple classes or
    # multiple files as appropriate. Having tests in multiple files makes
    # it possible to run tests from just one package:
    #
    #   ./bin/test -s canaimagnulinux.web.policy -t test_integration_unit
