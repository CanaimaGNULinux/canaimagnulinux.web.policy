# -*- coding: utf-8 -*-

""" This is an integration "unit" test for Site Structure """

from canaimagnulinux.web.policy.testing import INTEGRATION_TESTING

from plone import api

import unittest


class SiteStructureTestCase(unittest.TestCase):
    """ The class that tests the Plone Site Structure was created. """

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.member_folder = self.portal['Member']

    def test_default_content_is_removed(self):
        """ This method test that the default content is removed. """
        existing = self.portal.objectIds()
        self.assertTrue('events' not in existing)
        self.assertTrue('front-page' not in existing)
        self.assertTrue('news' not in existing)

    def test_root_folders(self):
        """ This method test if the root folders are existing. """
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

    def test_canaima_folder(self):
        """ This method test if the items children of canaima folder are existing. """
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

    def test_soluciones_folder(self):
        """ This method test if the items children of soluciones folder are existing. """
        folder = self.portal['soluciones']
        self.assertEqual(folder.getTitle(), 'Soluciones')
        types = ('Folder', 'Document', 'File', 'Image', 'Collection', 'collective.cover.content',)
        self.assertEqual(folder.getImmediatelyAddableTypes(), types)
        self.assertEqual(folder.getLocallyAllowedTypes(), types)
        self.assertEqual(api.content.get_state(folder), 'published')

    def test_comunidad_folder(self):
        """ This method test if the items children of comunidad folder are existing. """
        folder = self.portal['comunidad']
        self.assertEqual(folder.getTitle(), 'Comunidad')
        types = ('Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'FSDFacultyStaffDirectory',)
        self.assertEqual(folder.getImmediatelyAddableTypes(), types)
        self.assertEqual(folder.getLocallyAllowedTypes(), types)
        self.assertEqual(api.content.get_state(folder), 'published')
        self.assertEqual(folder.getLayout(), '@@usersmap_view')
