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

  - El producto `pas.plugins.velruse`_ para autenticación con redes sociales.

  - El producto `collective.geo.settings`_ para georeferenciar contenidos.

  - El producto ``collective.geo.usersmap`` para georeferenciar miembros (usuarios) del portal.

  - El producto ``collective.googleanalytics`` para generar las estadísticas de Google Analytics.

  - El producto `quintagroup.analytics`_ para generar las estadísticas de la creación de contenidos.

  - El producto `collective.nitf`_ para los artículos de noticias.


Instalación
===========

Debe leer el archivo ``INSTALL.txt`` en la carpeta ``docs`` de este producto.


Pruebas
=======

Para ejecutar las pruebas del paquete debe ubicarse en el directorio de su proyecto 
Buildout, y ejecutar en una consola de comando el siguiente comando:

.. code-block:: console

    $ ./bin/test -s canaimagnulinux.web.policy

Si necesita saber cual son las pruebas disponibles para este producto ejecute el 
siguiente comando:

.. code-block:: console

    $ ./bin/test -s canaimagnulinux.web.policy --list-tests

Para correr una prueba en especifica coloque el parámetro ``-t`` y el nombre de 
la función correspondiente, a continuación un ejemplo con el siguiente comando:

.. code-block:: console

    $ ./bin/test -s canaimagnulinux.web.policy -t test_portal_title

Para ver más opciones para ejecutar sus pruebas ejecute el siguiente comando:

.. code-block:: console

    $ ./bin/test --help


Sobre la calidad
================

.. image:: https://d2weczhvl823v0.cloudfront.net/CanaimaGNULinux/canaimagnulinux.web.policy/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

.. image:: https://travis-ci.org/CanaimaGNULinux/canaimagnulinux.web.policy.svg?branch=master
   :target: https://travis-ci.org/CanaimaGNULinux/canaimagnulinux.web.policy

.. image:: https://coveralls.io/repos/CanaimaGNULinux/canaimagnulinux.web.policy/badge.png
   :target: https://coveralls.io/r/CanaimaGNULinux/canaimagnulinux.web.policy

¿Tienes una idea?, ¿Encontraste un error? Háganos saber mediante la `apertura de un ticket de soporte`_.


Autor(es) Original(es)
======================

* Leonardo J .Caballero G. aka macagua

Colaboraciones impresionantes
=============================

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
.. _pas.plugins.velruse: https://pypi.python.org/pypi/pas.plugins.velruse
.. _apertura de un ticket de soporte: https://github.com/CanaimaGNULinux/canaimagnulinux.web.policy/issues
