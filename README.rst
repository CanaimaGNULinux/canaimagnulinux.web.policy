.. -*- coding: utf-8 -*-

.. contents:: Tabla de Contenidos

Introducción
============

Este producto ofrece varios perfiles de instalación para el sitio de Canaima GNU/Linux.

Características
===============
Este producto habilita las siguientes configuraciones:

- Instala los siguientes productos:

  - El paquete `Products.CMFPlacefulWorkflow`_ para uso en los formularios.

  - El producto `plone.app.caching`_ para cacheo y aceleración de contenido.

  - El producto `plone.app.dexterity`_ para gestión de tipos de contenidos ``Dexterity``.

  - El producto `plone.app.ldap`_ para autenticación con ``LDAP``.

  - El producto `collective.geo.settings`_ para georeferenciar contenidos.

  - El producto ``collective.geo.usersmap`` para georeferenciar miembros (usuarios) del portal.

  - El producto ``collective.googleanalytics`` para generar las estadísticas de Google Analytics.

  - El producto `quintagroup.analytics`_ para generar las estadísticas de la creación de contenidos.

  - El producto `collective.nitf`_ para los artículos de noticias.


Instalación
===========

Este proyecto debe ser instalado usando configuraciones buildout. Debe leer el archivo
``INSTALL.txt`` en la carpeta ``docs`` de este producto.


Insignias de calidad
--------------------

.. image:: https://d2weczhvl823v0.cloudfront.net/CanaimaGNULinux/canaimagnulinux.web.policy/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

.. image:: https://travis-ci.org/CanaimaGNULinux/canaimagnulinux.web.policy.svg?branch=master
   :target: https://travis-ci.org/CanaimaGNULinux/canaimagnulinux.web.policy

.. image:: https://coveralls.io/repos/CanaimaGNULinux/canaimagnulinux.web.policy/badge.png
   :target: https://coveralls.io/r/CanaimaGNULinux/canaimagnulinux.web.policy

Dependencias del sitio
----------------------

Dependencias usadas en el sitio de Canaima GNU/Linux.

.. list-table:: Dependencias extras
   :widths: 10 10 10 10
   :header-rows: 1

   * - Nombre de paquete
     - Versión
     - Pruebas
     - Pruebas de cobertura
   * - Products.Doormat
     - |Products.Doormat.v|
     - |Products.Doormat.t|
     - |Products.Doormat.c|
   * - Products.FacultyStaffDirectory
     - |Products.FacultyStaffDirectory.v|
     - |Products.FacultyStaffDirectory.t|
     - |Products.FacultyStaffDirectory.c|
   * - Products.PloneFormGen
     - |Products.PloneFormGen.v|
     - |Products.PloneFormGen.t|
     - |Products.PloneFormGen.c|
   * - Products.PloneServicesCenter
     - |Products.PloneServicesCenter.v|
     - |Products.PloneServicesCenter.t|
     - |Products.PloneServicesCenter.c|
   * - Products.PloneSoftwareCenter
     - |Products.PloneSoftwareCenter.v|
     - |Products.PloneSoftwareCenter.t|
     - |Products.PloneSoftwareCenter.c|
   * - plone.api
     - |plone.api.v|
     - |plone.api.t|
     - |plone.api.c|
   * - plone.app.ldap
     - |plone.app.ldap.v|
     - |plone.app.ldap.t|
     - |plone.app.ldap.c|
   * - canaimagnulinux.web.theme
     - |canaimagnulinux.web.theme.v|
     - |canaimagnulinux.web.theme.t|
     - |canaimagnulinux.web.theme.c|
   * - cioppino.twothumbs
     - |cioppino.twothumbs.v|
     - |cioppino.twothumbs.t|
     - |cioppino.twothumbs.c|
   * - collective.cover
     - |collective.cover.v|
     - |collective.cover.t|
     - |collective.cover.c|
   * - collective.disqus
     - |collective.disqus.v|
     - |collective.disqus.t|
     - |collective.disqus.c|
   * - collective.facebook.portlets
     - |collective.facebook.portlets.v|
     - |collective.facebook.portlets.t|
     - |collective.facebook.portlets.c|
   * - collective.geo.usersmap
     - |collective.geo.usersmap.v|
     - |collective.geo.usersmap.t|
     - |collective.geo.usersmap.c|
   * - collective.googleanalytics
     - |collective.googleanalytics.v|
     - |collective.googleanalytics.t|
     - |collective.googleanalytics.c|
   * - collective.googlenews
     - |collective.googlenews.v|
     - |collective.googlenews.t|
     - |collective.googlenews.c|
   * - collective.nitf
     - |collective.nitf.v|
     - |collective.nitf.t|
     - |collective.nitf.c|
   * - collective.opendata
     - |collective.opendata.v|
     - |collective.opendata.t|
     - |collective.opendata.c|
   * - collective.polls
     - |collective.polls.v|
     - |collective.polls.t|
     - |collective.polls.c|
   * - collective.twitter.portlets
     - |collective.twitter.portlets.v|
     - |collective.twitter.portlets.t|
     - |collective.twitter.portlets.c|
   * - collective.twitter.tweet
     - |collective.twitter.tweet.v|
     - |collective.twitter.tweet.t|
     - |collective.twitter.tweet.c|
   * - collective.upload
     - |collective.upload.v|
     - |collective.upload.t|
     - |collective.upload.c|
   * - sc.social.like
     - |sc.social.like.v|
     - |sc.social.like.t|
     - |sc.social.like.c|

Pruebas
=======

Para ejecutar las pruebas del paquete debe ubicarse en el directorio de su proyecto 
Buildout, y ejecutar en una consola de comando el siguiente comando:

::

    $ ./bin/test -s canaimagnulinux.web.policy

Si necesita saber cual son las pruebas disponibles para este producto ejecute el 
siguiente comando:

::

    $ ./bin/test -s canaimagnulinux.web.policy --list-tests

Para correr una prueba en especifica coloque el parámetro ``-t`` y el nombre de 
la función correspondiente, a continuación un ejemplo con el siguiente comando:

::

    $ ./bin/test -s canaimagnulinux.web.policy -t test_portal_title

Para ver más opciones para ejecutar sus pruebas ejecute el siguiente comando:

::

    $ ./bin/test --help


Soporte
=======

¿Tienes una idea?, ¿Encontraste un error? Háganos saber mediante la `apertura de un ticket de soporte`_.


Autor(es) Original(es)
======================

* Leonardo J .Caballero G. aka macagua

Colaboraciones impresionantes
=============================

* Noe Nieto aka tzicatl

* Nombre Completo aka apodo

Par una lista actualizada de todo los colaboradores visite: https://github.com/canaimagnulinux/canaimagnulinux.web.policy/contributors

.. _Products.CMFPlacefulWorkflow: https://pypi.python.org/pypi/Products.CMFPlacefulWorkflow
.. _plone.app.ldap: https://pypi.python.org/pypi/plone.app.ldap
.. _plone.app.caching: https://pypi.python.org/pypi/plone.app.caching
.. _plone.app.dexterity: https://pypi.python.org/pypi/plone.app.dexterity
.. _plone.app.caching: https://pypi.python.org/pypi/plone.app.caching
.. _quintagroup.analytics: https://pypi.python.org/pypi/quintagroup.analytics
.. _collective.nitf: https://github.com/collective/collective.nitf
.. _collective.geo.settings: https://pypi.python.org/pypi/collective.geo.settings
.. _apertura de un ticket de soporte: https://github.com/CanaimaGNULinux/canaimagnulinux.web.policy/issues

.. |cioppino.twothumbs.v| image:: http://img.shields.io/pypi/v/cioppino.twothumbs.svg
   :target: https://pypi.python.org/pypi/cioppino.twothumbs
.. |cioppino.twothumbs.t| image:: https://secure.travis-ci.org/collective/cioppino.twothumbs.png
   :target: http://travis-ci.org/collective/cioppino.twothumbs
.. |cioppino.twothumbs.c| image:: https://coveralls.io/repos/collective/cioppino.twothumbs/badge.png?branch=master
   :target: https://coveralls.io/r/collective/cioppino.twothumbs

.. |Products.Doormat.v| image:: http://img.shields.io/pypi/v/Products.Doormat.svg
   :target: https://pypi.python.org/pypi/Products.Doormat
.. |Products.Doormat.t| image:: https://secure.travis-ci.org/collective/Products.Doormat.png
   :target: http://travis-ci.org/collective/Products.Doormat
.. |Products.Doormat.c| image:: https://coveralls.io/repos/collective/Products.Doormat/badge.png?branch=master
   :target: https://coveralls.io/r/collective/Products.Doormat

.. |Products.FacultyStaffDirectory.v| image:: http://img.shields.io/pypi/v/Products.FacultyStaffDirectory.svg
   :target: https://pypi.python.org/pypi/Products.FacultyStaffDirectory
.. |Products.FacultyStaffDirectory.t| image:: https://secure.travis-ci.org/collective/Products.FacultyStaffDirectory.png
   :target: http://travis-ci.org/collective/Products.FacultyStaffDirectory
.. |Products.FacultyStaffDirectory.c| image:: https://coveralls.io/repos/collective/Products.FacultyStaffDirectory/badge.png?branch=master
   :target: https://coveralls.io/r/collective/Products.FacultyStaffDirectory

.. |Products.PloneFormGen.v| image:: http://img.shields.io/pypi/v/Products.PloneFormGen.svg
   :target: https://pypi.python.org/pypi/Products.PloneFormGen
.. |Products.PloneFormGen.t| image:: https://secure.travis-ci.org/collective/Products.PloneFormGen.png
   :target: http://travis-ci.org/collective/Products.PloneFormGen
.. |Products.PloneFormGen.c| image:: https://coveralls.io/repos/collective/Products.PloneFormGen/badge.png?branch=master
   :target: https://coveralls.io/r/collective/Products.PloneFormGen

.. |Products.PloneServicesCenter.v| image:: http://img.shields.io/pypi/v/Products.PloneServicesCenter.svg
   :target: https://pypi.python.org/pypi/Products.PloneServicesCenter
.. |Products.PloneServicesCenter.t| image:: https://secure.travis-ci.org/collective/Products.PloneServicesCenter.png
   :target: http://travis-ci.org/collective/Products.PloneServicesCenter
.. |Products.PloneServicesCenter.c| image:: https://coveralls.io/repos/collective/Products.PloneServicesCenter/badge.png?branch=master
   :target: https://coveralls.io/r/collective/Products.PloneServicesCenter

.. |Products.PloneSoftwareCenter.v| image:: http://img.shields.io/pypi/v/Products.PloneSoftwareCenter.svg
   :target: https://pypi.python.org/pypi/Products.PloneSoftwareCenter
.. |Products.PloneSoftwareCenter.t| image:: https://secure.travis-ci.org/collective/Products.PloneSoftwareCenter.png
   :target: http://travis-ci.org/collective/Products.PloneSoftwareCenter
.. |Products.PloneSoftwareCenter.c| image:: https://coveralls.io/repos/collective/Products.PloneSoftwareCenter/badge.png?branch=master
   :target: https://coveralls.io/r/collective/Products.PloneSoftwareCenter

.. |plone.api.v| image:: http://img.shields.io/pypi/v/plone.api.svg
   :target: https://pypi.python.org/pypi/plone.api
.. |plone.api.t| image:: https://secure.travis-ci.org/plone/plone.api.png
   :target: http://travis-ci.org/collective/plone.api
.. |plone.api.c| image:: https://coveralls.io/repos/plone/plone.api/badge.png?branch=master
   :target: https://coveralls.io/r/collective/plone.api

.. |plone.app.ldap.v| image:: http://img.shields.io/pypi/v/plone.app.ldap.svg
   :target: https://pypi.python.org/pypi/plone.app.ldap
.. |plone.app.ldap.t| image:: https://secure.travis-ci.org/plone/plone.app.ldap.png
   :target: http://travis-ci.org/collective/plone.app.ldap
.. |plone.app.ldap.c| image:: https://coveralls.io/repos/plone/plone.app.ldap/badge.png?branch=master
   :target: https://coveralls.io/r/collective/plone.app.ldap

.. |collective.polls.v| image:: http://img.shields.io/pypi/v/collective.polls.svg
   :target: https://pypi.python.org/pypi/collective.polls
.. |collective.polls.t| image:: https://secure.travis-ci.org/collective/collective.polls.png
   :target: http://travis-ci.org/collective/collective.polls
.. |collective.polls.c| image:: https://coveralls.io/repos/collective/collective.polls/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.polls

.. |canaimagnulinux.web.theme.v| image:: http://img.shields.io/pypi/v/canaimagnulinux.web.theme.svg
   :target: https://pypi.python.org/pypi/canaimagnulinux.web.theme
.. |canaimagnulinux.web.theme.t| image:: https://secure.travis-ci.org/CanaimaGNULinux/canaimagnulinux.web.theme.png
   :target: http://travis-ci.org/CanaimaGNULinux/canaimagnulinux.web.theme
.. |canaimagnulinux.web.theme.c| image:: https://coveralls.io/repos/CanaimaGNULinux/canaimagnulinux.web.theme/badge.png?branch=master
   :target: https://coveralls.io/r/CanaimaGNULinux/canaimagnulinux.web.theme

.. |collective.cover.v| image:: http://img.shields.io/pypi/v/collective.cover.svg
   :target: https://pypi.python.org/pypi/collective.cover
.. |collective.cover.t| image:: https://secure.travis-ci.org/collective/collective.cover.png
   :target: http://travis-ci.org/collective/collective.cover
.. |collective.cover.c| image:: https://coveralls.io/repos/collective/collective.cover/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.cover

.. |collective.disqus.v| image:: http://img.shields.io/pypi/v/collective.disqus.svg
   :target: https://pypi.python.org/pypi/collective.disqus
.. |collective.disqus.t| image:: https://secure.travis-ci.org/collective/collective.disqus.png
   :target: http://travis-ci.org/collective/collective.disqus
.. |collective.disqus.c| image:: https://coveralls.io/repos/collective/collective.disqus/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.disqus

.. |collective.facebook.portlets.v| image:: http://img.shields.io/pypi/v/collective.facebook.portlets.svg
   :target: https://pypi.python.org/pypi/collective.facebook.portlets
.. |collective.facebook.portlets.t| image:: https://secure.travis-ci.org/collective/collective.facebook.portlets.png
   :target: http://travis-ci.org/collective/collective.facebook.portlets
.. |collective.facebook.portlets.c| image:: https://coveralls.io/repos/collective/collective.facebook.portlets/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.facebook.portlets

.. |collective.geo.usersmap.v| image:: http://img.shields.io/pypi/v/collective.geo.usersmap.svg
   :target: https://pypi.python.org/pypi/collective.geo.usersmap
.. |collective.geo.usersmap.t| image:: https://secure.travis-ci.org/collective/collective.geo.usersmap.png
   :target: http://travis-ci.org/collective/collective.geo.usersmap
.. |collective.geo.usersmap.c| image:: https://coveralls.io/repos/collective/collective.geo.usersmap/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.geo.usersmap

.. |collective.googleanalytics.v| image:: http://img.shields.io/pypi/v/collective.googleanalytics.svg
   :target: https://pypi.python.org/pypi/collective.googleanalytics
.. |collective.googleanalytics.t| image:: https://secure.travis-ci.org/collective/collective.googleanalytics.png
   :target: http://travis-ci.org/collective/collective.googleanalytics
.. |collective.googleanalytics.c| image:: https://coveralls.io/repos/collective/collective.googleanalytics/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.googleanalytics

.. |collective.googlenews.v| image:: http://img.shields.io/pypi/v/collective.googlenews.svg
   :target: https://pypi.python.org/pypi/collective.googlenews
.. |collective.googlenews.t| image:: https://secure.travis-ci.org/collective/collective.googlenews.png
   :target: http://travis-ci.org/collective/collective.googlenews
.. |collective.googlenews.c| image:: https://coveralls.io/repos/collective/collective.googlenews/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.googlenews

.. |collective.nitf.v| image:: http://img.shields.io/pypi/v/collective.nitf.svg
   :target: https://pypi.python.org/pypi/collective.nitf
.. |collective.nitf.t| image:: https://secure.travis-ci.org/collective/collective.nitf.png
   :target: http://travis-ci.org/collective/collective.nitf
.. |collective.nitf.c| image:: https://coveralls.io/repos/collective/collective.nitf/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.nitf

.. |collective.opendata.v| image:: http://img.shields.io/pypi/v/collective.opendata.svg
   :target: https://pypi.python.org/pypi/collective.opendata
.. |collective.opendata.t| image:: https://secure.travis-ci.org/plonegovbr/collective.opendata.png
   :target: http://travis-ci.org/collective/collective.opendata
.. |collective.opendata.c| image:: https://coveralls.io/repos/plonegovbr/collective.opendata/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.opendata

.. |collective.twitter.portlets.v| image:: http://img.shields.io/pypi/v/collective.twitter.portlets.svg
   :target: https://pypi.python.org/pypi/collective.twitter.portlets
.. |collective.twitter.portlets.t| image:: https://secure.travis-ci.org/collective/collective.twitter.portlets.png
   :target: http://travis-ci.org/collective/collective.twitter.portlets
.. |collective.twitter.portlets.c| image:: https://coveralls.io/repos/collective/collective.twitter.portlets/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.twitter.portlets

.. |collective.twitter.tweet.v| image:: http://img.shields.io/pypi/v/collective.twitter.tweet.svg
   :target: https://pypi.python.org/pypi/collective.twitter.tweet
.. |collective.twitter.tweet.t| image:: https://secure.travis-ci.org/collective/collective.twitter.tweet.png
   :target: http://travis-ci.org/collective/collective.twitter.tweet
.. |collective.twitter.tweet.c| image:: https://coveralls.io/repos/collective/collective.twitter.tweet/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.twitter.tweet

.. |collective.upload.v| image:: http://img.shields.io/pypi/v/collective.upload.svg
   :target: https://pypi.python.org/pypi/collective.upload
.. |collective.upload.t| image:: https://secure.travis-ci.org/collective/collective.upload.png
   :target: http://travis-ci.org/collective/collective.upload
.. |collective.upload.c| image:: https://coveralls.io/repos/collective/collective.upload/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.upload

.. |sc.social.like.v| image:: http://img.shields.io/pypi/v/sc.social.like.svg
   :target: https://pypi.python.org/pypi/sc.social.like
.. |sc.social.like.t| image:: https://secure.travis-ci.org/collective/sc.social.like.png
   :target: http://travis-ci.org/collective/sc.social.like
.. |sc.social.like.c| image:: https://coveralls.io/repos/collective/sc.social.like/badge.png?branch=master
   :target: https://coveralls.io/r/collective/sc.social.like
