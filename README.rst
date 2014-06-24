.. -*- coding: utf-8 -*-

.. contents:: Tabla de Contenidos

Introducción
============

Este producto ofrece varios perfiles de instalación para el sitio de Canaima GNU/Linux.

Características
===============
Este producto habilita las siguientes configuraciones:

- Por definir.


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

.. _`apertura de un ticket de soporte`: https://github.com/CanaimaGNULinux/canaimagnulinux.web.policy/issues