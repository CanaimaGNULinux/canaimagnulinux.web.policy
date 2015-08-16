# -*- coding: utf-8 -*-

""" Contains constants used by setuphandler.py """

from canaimagnulinux.web.policy.utils import _add_id

PROJECTNAME = 'canaimagnulinux.web.policy'
PROFILE_ID = '{0}:default'.format(PROJECTNAME)

# content created at Plone's installation
DEFAULT_CONTENT = ('front-page', 'news', 'events')

CREATORS = (u'Proyecto Canaima', )

DEPENDENCIES = [
    'ArchAddOn',
    'CMFPlacefulWorkflow',
    'Doormat',
    'FacultyStaffDirectory',
    'PloneFormGen',
    'PloneServicesCenter',
    'PloneSoftwareCenter',
]

MAILHOST_CONFIGURATION = {
    'configure': True,
    'smtphost': 'localhost',
    'smtpport': 25,
    'fromemailname': 'Sitio Web Canaima GNU/Linux',
    'fromemailaddress': 'soporte@canaima.softwarelibre.gob.ve'
}

# new site structure; this dictionary defines the objects that are going to be
# created on the root of the site; it also includes information about folder
# constraints and objects to be created inside them
SITE_STRUCTURE = [
    dict(
        type='collective.cover.content',
        title=u'Portada',
        description=u'Objeto que componen la página principal del sitio. (Atención: Este objeto no debe suprimirse)',
        text=u'',
        # template_layout='Portada inicio',
        excludeFromNav=True,
    ),
    dict(
        type='Folder',
        title=u'Términos y convenios',
        description=u'Términos y convenios del uso del sitio Web',
        _addable_types=['Folder', 'Document', 'File', 'Image', 'Link'],
        _children=[
            dict(
                type='Document',
                id='condiciones-generales-miembros',
                title=u'Condiciones generales de los miembros',
                description=u'Información general sobre las condiciones y términos generales del uso del portal Canaima GNU/Linux.',
                text=u'',
            ),
        ],
        excludeFromNav=True,
    ),
    dict(
        type='Folder',
        title=u'Canaima',
        description=u'Sección que contiene la información básica relativa al proyecto Canaima.',
        _addable_types=['Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'CaseStudyFolder'],
        _children=[
            dict(
                type='Document',
                title=u'Conozca Canaima',
                description=u'Información general sobre los elementos del proyecto Canaima GNU/Linux.',
            ),
            dict(
                type='Document',
                title=u'Características',
                description=u'Conozca las características de Canaima GNU/Linux.',
            ),
            dict(
                type='Document',
                title=u'¿Por qué usar Canaima?',
                description=u'Entienda por qué usar Canaima GNU/Linux.',
            ),
            dict(
                type='Document',
                title=u'¿Por qué Software libre?',
                description=u'Entienda la importancia del Software libre en Canaima GNU/Linux.',
            ),
            # dict(
            #     type='CaseStudyFolder',
            #     title=u'Casos de éxitos',
            #     description=u'Conjunto de Casos de éxitos en la adopción de Canaima GNU/Linux.',
            # ),
            dict(
                type='Folder',
                title=u'Casos de éxitos',
                description=u'Conjunto de Casos de éxitos en la adopción de Canaima GNU/Linux.',
                _addable_types=['Folder', 'Collection', 'Document', 'CaseStudyFolder'],
                _children=[
                    dict(
                        type='Collection',
                        title=u'Ministerios',
                        description=u'Casos de éxitos en la adopción de Canaima GNU/Linux a nivel de los Ministerios.',
                        sort_reversed=True,
                        sort_on=u'effective',
                        limit=1000,
                        query=[
                            dict(
                                i='portal_type',
                                o='plone.app.querystring.operation.selection.is',
                                v='Document',
                            ),
                            dict(
                                i='path',
                                o='plone.app.querystring.operation.string.relativePath',
                                v='../',
                            ),
                            dict(
                                i='review_state',
                                o='plone.app.querystring.operation.selection.is',
                                v=['published'],
                            ),
                        ],
                    ),
                    dict(
                        type='Document',
                        title=u'Canaima GNU/Linux en CNTI',
                        description='',
                        text=u'',
                    ),
                    dict(
                        type='Document',
                        title=u'Canaima GNU/Linux en Cenditel',
                        description='',
                        text=u'',
                    ),
                    dict(
                        type='Document',
                        title=u'Canaima GNU/Linux en Ministerio del Poder Popular para la Educación (MPPE)',
                        description='',
                        text=u'',
                    ),
                    dict(
                        type='Document',
                        title=u'Proyecto Canaima Educativo',
                        description='',
                        text=u'',
                    ),
                ],
            ),
        ],
    ),
    dict(
        type='Folder',
        title=u'Soluciones',
        description=u'Explore las posibilidades de Canaima GNU/Linux.',
        _addable_types=['Folder', 'Document', 'File', 'Image', 'Collection', 'collective.cover.content'],
        _children=[
            dict(
                type='Collection',
                title=u'Sector gobierno',
                description=u'Soluciones de Canaima GNU/Linux disponibles en el Sector gobierno.',
                sort_reversed=True,
                sort_on=u'effective',
                limit=1000,
                query=[
                    dict(
                        i='portal_type',
                        o='plone.app.querystring.operation.selection.is',
                        v='Document',
                    ),
                    dict(
                        i='path',
                        o='plone.app.querystring.operation.string.relativePath',
                        v='../',
                    ),
                    dict(
                        i='review_state',
                        o='plone.app.querystring.operation.selection.is',
                        v=['published'],
                    ),
                    dict(
                        i='genre',
                        o='plone.app.querystring.operation.selection.is',
                        v=None,
                    ),
                    dict(
                        i='section',
                        o='plone.app.querystring.operation.selection.is',
                        v='Soluciones',
                    ),
                ],
                subjects=(u'Soluciones', u'Sector gobierno', u'Distribución')
            ),
            dict(
                type='Collection',
                title=u'Sector comunas',
                description=u'Soluciones de Canaima GNU/Linux disponibles en el Sector comunas.',
                sort_reversed=True,
                sort_on=u'effective',
                limit=1000,
                query=[
                    dict(
                        i='portal_type',
                        o='plone.app.querystring.operation.selection.is',
                        v='Document',
                    ),
                    dict(
                        i='path',
                        o='plone.app.querystring.operation.string.relativePath',
                        v='../',
                    ),
                    dict(
                        i='review_state',
                        o='plone.app.querystring.operation.selection.is',
                        v=['published'],
                    ),
                    dict(
                        i='genre',
                        o='plone.app.querystring.operation.selection.is',
                        v=None,
                    ),
                    dict(
                        i='section',
                        o='plone.app.querystring.operation.selection.is',
                        v='Soluciones',
                    ),
                ],
                subjects=(u'Soluciones', u'Sector comunas', u'Distribución')
            ),
            dict(
                type='Collection',
                title=u'Geomática',
                description=u'Soluciones de Canaima GNU/Linux disponibles en el Geomática.',
                sort_reversed=True,
                sort_on=u'effective',
                limit=1000,
                query=[
                    dict(
                        i='portal_type',
                        o='plone.app.querystring.operation.selection.is',
                        v='Document',
                    ),
                    dict(
                        i='path',
                        o='plone.app.querystring.operation.string.relativePath',
                        v='../',
                    ),
                    dict(
                        i='review_state',
                        o='plone.app.querystring.operation.selection.is',
                        v=['published'],
                    ),
                    dict(
                        i='genre',
                        o='plone.app.querystring.operation.selection.is',
                        v=None,
                    ),
                    dict(
                        i='section',
                        o='plone.app.querystring.operation.selection.is',
                        v='Soluciones',
                    ),
                ],
                subjects=(u'Soluciones', u'Geomática', u'Distribución')
            ),
            dict(
                type='Document',
                title=u'Canaima Popular',
                description='',
                text=u'',
                subjects=(u'Soluciones', u'Sector gobierno', u'Distribución', u'Canaima Popular'),
                excludeFromNav=True,
            ),
            dict(
                type='Document',
                title=u'Canaima Educativo',
                description='',
                text=u'',
                subjects=(u'Soluciones', u'Sector gobierno', u'Distribución', u'Canaima Educativo'),
                excludeFromNav=True,
            ),
            dict(
                type='Document',
                title=u'Canaima Colibri',
                description='',
                text=u'',
                subjects=(u'Soluciones', u'Sector comunas', u'Distribución', u'Canaima Colibri'),
                excludeFromNav=True,
            ),
            dict(
                type='Document',
                title=u'Canaima Comunal',
                description='',
                text=u'',
                subjects=(u'Soluciones', u'Sector comunas', u'Distribución', u'Canaima Comunal'),
                excludeFromNav=True,
            ),
            dict(
                type='Document',
                title=u'GeoCanaima',
                description='',
                text=u'',
                subjects=(u'Soluciones', u'Geomática', u'Distribución', u'GeoCanaima'),
                excludeFromNav=True,
            ),
        ],
    ),
    dict(
        type='Folder',
        title=u'Soporte y Aprendizaje',
        description=u'En esta sección brindamos ayuda o soporte técnico para el uso y corrección de errores en la herramienta.',
        _addable_types=['Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'ProviderFolder'],
        _children=[
            dict(
                type='Folder',
                title=u'Necesito ayuda',
                description=u'Saque el máximo provecho de su solución de Canaima, y no dejes que te frenen los complejos problemas técnicos. Existen distintas formas de obtener soporte para Canaima GNU/Linux.',
                _addable_types=['Folder', 'Document', 'File', 'Image', 'collective.cover.content'],
                _children=[
                    dict(
                        type='Document',
                        title=u'Ayuda interactiva',
                        description=u'Saque el máximo provecho de su solución de Canaima, y no dejes que te frenen los complejos problemas técnicos. Existen distintas formas de obtener soporte para Canaima GNU/Linux.',
                        text=u'',
                        subjects=(u'Soporte y Aprendizaje', u'Necesito ayuda', u'Ayuda interactiva'),
                    ),
                    dict(
                        type='Document',
                        title=u'Soporte a programas',
                        description=u'Soporte a programas incluidos en las diversas soluciones de Canaima GNU/Linux.',
                        text=u'',
                        subjects=(u'Soporte y Aprendizaje', u'Necesito ayuda', u'Soporte a programas'),
                    ),
                    dict(
                        type='Document',
                        title=u'Apoyo institucional',
                        description=u'Conozca las diversas organizaciones públicas y privadas que invierte gran cantidad tiempo y dinero en el proyecto Canaima.',
                        text=u'',
                        subjects=(u'Soporte y Aprendizaje', u'Necesito ayuda', u'Apoyo institucional'),
                    ),
                    dict(
                        type='Document',
                        title=u'Apoyo de la comunidad',
                        description=u'Conozca los diversos recursos electrónicos que ofrece la comunidad para apoyo y soporte en el proyecto Canaima.',
                        text=u'',
                        subjects=(u'Soporte y Aprendizaje', u'Necesito ayuda', u'Apoyo de la comunidad'),
                    ),
                ],
            ),
            dict(
                type='Folder',
                title=u'Yo quiero aprender',
                description=u'Si tiene una gran necesidad de aprender más de las soluciones Canaima, puede acceder a nuestra base de conocimientos e incluso a los diversos modelos de capacitación y certificación.',
                _addable_types=['Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'FSDDepartment'],
                _children=[
                    dict(
                        type='Document',
                        title=u'Capacitación y certificación',
                        description=u'Conozca los diversos actores de la comunidad Canaima ofrece capacitación y certificación en Software libre y Canaima GNU/Linux.',
                        text=u'',
                        subjects=(u'Soporte y Aprendizaje', u'Yo quiero aprender', u'Capacitación y certificación'),
                    ),
                    dict(
                        type='Folder',
                        title=u'Base de conocimientos',
                        description=u'Conozca los diversos actores de la comunidad Canaima ofrece capacitación y certificación en Software libre y Canaima GNU/Linux.',
                        _addable_types=['Folder', 'Document', 'File', 'Image'],
                        _children=[
                            dict(
                                type='Document',
                                title=u'Preguntas frecuentes',
                                description=u'Las preguntas de uso frecuentes son utilizadas como referencias rápida a las preguntas más comunes sobre el proyecto Canaima.',
                                text=u'',
                                subjects=(u'Soporte y Aprendizaje', u'Yo quiero aprender', u'Preguntas frecuentes'),
                            ),
                            dict(
                                type='Document',
                                title=u'Glosarios',
                                description=u'Las glosarios de términos utilizados en el proyecto Canaima.',
                                text=u'',
                                subjects=(u'Soporte y Aprendizaje', u'Yo quiero aprender', u'Glosarios'),
                            ),
                            dict(
                                type='Folder',
                                title=u'Enlaces',
                                description=u'Los enlaces a diversos recursos utilizados en el proyecto Canaima.',
                                _addable_types=['Link'],
                                subjects=(u'Soporte y Aprendizaje', u'Yo quiero aprender', u'Enlaces'),
                                _children=[
                                    dict(
                                        type='Link',
                                        title=u'Listas de correo',
                                        description=u'Las preguntas de uso frecuentes son utilizadas como referencias rápida a las preguntas más comunes sobre el proyecto Canaima.',
                                        remoteUrl='http://listas.canaima.softwarelibre.gob.ve/',
                                        subjects=(u'Soporte y Aprendizaje', u'Yo quiero aprender', u'Base de conocimientos', u'Listas de correo'),
                                    ),
                                ],
                            ),
                            dict(
                                type='Folder',
                                title=u'Presentaciones',
                                description=u'Este es un espacio donde pensamos publicar las láminas de presentaciones realizadas sobre el proyecto Canaima, las cuales se puede publicar en la plataforma colaborativa Canaima o en sitios como ​Slideshare.net​, entre otros.',
                                _addable_types=['Link'],
                                subjects=(u'Soporte y Aprendizaje', u'Yo quiero aprender', u'Presentaciones'),
                                _children=[
                                    dict(
                                        type='Link',
                                        title=u'\'canaima gnu linux\' on SlideShare',
                                        description=u'Presentaciones publicadas en SlideShare.com',
                                        remoteUrl='http://www.slideshare.net/search/slideshow?searchfrom=header&q=canaima+gnu+linux',
                                        subjects=(u'Soporte y Aprendizaje', u'Yo quiero aprender', u'Base de conocimientos', u'\'canaima gnu linux\' on SlideShare'),
                                    ),
                                ],

                            ),
                            dict(
                                type='Folder',
                                title=u'Vídeos demostrativos',
                                description=u'Este es un espacio donde pensamos publicar los diversos vídeos realizados sobre el proyecto Canaima, las cuales se puede publicar en la plataforma colaborativa Canaima o en sitios como ​Youtube.com​, Vimeo.com​,​ entre otros.',
                                _addable_types=['Link'],
                                subjects=(u'Soporte y Aprendizaje', u'Yo quiero aprender', u'Vídeos demostrativos'),
                                _children=[
                                    dict(
                                        type='Link',
                                        title=u'Representación Visual de Canaima GNU/Linux',
                                        description=u'Representación Visual, Software Libre, Canaima - YouTube.',
                                        remoteUrl='https://www.youtube.com/watch?v=N9RwAYPtFNY',
                                        subjects=(u'Soporte y Aprendizaje', u'Yo quiero aprender', u'Base de conocimientos', u'Representación Visual de Canaima GNU/Linux'),
                                    ),
                                ],

                            ),
                        ],
                    ),
                    dict(
                        type='Document',
                        title=u'Manuales y Tutoriales',
                        description=u'Diversos manuales y tutoriales del proyecto Canaima GNU/Linux.',
                        text=u'',
                        subjects=(u'Soporte y Aprendizaje', u'Yo quiero aprender', u'Manuales y Tutoriales'),
                    ),
                    dict(
                        type='Document',
                        title=u'Centro de mercadotecnia',
                        description=u'Diversos recursos para la mercadotecnia del proyecto Canaima GNU/Linux.',
                        text=u'',
                        subjects=(u'Soporte y Aprendizaje', u'Yo quiero aprender', u'Centro de mercadotecnia'),
                    ),
                ],
            ),
            dict(
                type='Folder',
                title=u'Consultoría',
                description=u'La Administración Pública Nacional (APN) en Venezuela dispone de varias instituciones adscritas al Ministerio de Ciencia y Tecnología donde los proveedores asisten y soportan a las diversas ediciones de Canaima.',
                _addable_types=['Folder', 'Collection', 'Document', 'File', 'Image', 'collective.cover.content', 'FSDDepartment'],
                _children=[
                    dict(
                        type='Document',
                        title=u'Servicios del estado',
                        description=u'La fundación Centro nacional de Tecnologías (CNTI), dispone de varios productos y servicios dirigidos a las instituciones públicas, sector productivo y comunidades organizadas.',
                        text=u'',
                        subjects=(u'Soporte y Aprendizaje', u'Consultoría', u'Servicios del estado'),
                    ),
                    dict(
                        type='Collection',
                        title=u'Buscar un experto',
                        description=u'Los proveedores proporcionan una variedad de servicios de software, hardware e implementación para ayudar a sacar el máximo partido a su entorno de TIC usando software libre y código abierto.',
                        sort_reversed=True,
                        sort_on=u'effective',
                        limit=1000,
                        query=[
                            dict(
                                i='portal_type',
                                o='plone.app.querystring.operation.selection.is',
                                v=['Document', 'Link'],
                            ),
                            dict(
                                i='path',
                                o='plone.app.querystring.operation.string.relativePath',
                                v='../soporte-y-aprendizaje/mercado-de-servicios/servicios-empresariales',
                            ),
                        ],
                    ),
                ],
            ),
            dict(
                type='Folder',
                title=u'Mercado de servicios',
                description=u'Es el espacio para ofrecer productos y servicios en el Proyecto Canaima, este espacio lo nombra la misma comunidad, no está sujeto al formalismo del Servicio Nacional de Contrataciones (SNC) ni de la Industri Venezolana de Software Libre (INVESOL) simplemente es un censo de los distintos actores que ofrecen soporte comercial a Canaima.',
                _addable_types=['Folder', 'Document', 'Link', 'File', 'Image', 'collective.cover.content', 'ProviderFolder', 'FSDDepartment'],
                _children=[
                    dict(
                        type='Link',
                        title=u'INVESOL',
                        description=u'La Industria Venezolana de Software Libre (INVESOL)',
                        remoteUrl='http://www.softwarelibre.gob.ve/index.php?option=com_content&view=article&id=71:invesol&catid=42:contenido-estatico',
                    ),
                    # dict(
                    #    type='Document',
                    #    title=u'Soporte técnico a Canaimitas',
                    #    description=u'Ofrece el servicio de soporte técnico a Hardware y Software de la computadoras Canaimitas del proyecto Canaima Educativo.',
                    #    text=u'',
                    # ),
                ],
            ),
        ],
    ),
    dict(
        type='Folder',
        title=u'Descargas',
        description=u'Canaima GNU /Linux y sus ediciones son cien por ciento libres para ifundirla(s) y compartirla(s). Principalmente la distribución se hace a través de internet.',
        _addable_types=['Folder', 'Document', 'File', 'Image', 'collective.cover.content'],
        _children=[
            dict(
                type='Folder',
                title=u'Obtener Canaima',
                description=u'Para obtener una copia de las diversas ediciones Canama puede obtenerla usted mismo o buscar un "Proveedor de copias de Software libre"',
                _addable_types=['Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'ProviderFolder', 'FSDDepartment'],
                _children=[
                    dict(
                        type='Document',
                        id='verifique-descarga-imagen-iso',
                        title=u'Verifique la descarga de la imagen ISO',
                        description=u'Conozca si su descarga de la imagen ISO de Canaima GNU/Linux se descargo correctamente.',
                        text=u'',
                        subjects=(u'Descargas', u'Obtener Canaima', u'MD5', u'SHA1', u'ISO'),
                    ),
                    dict(
                        type='Document',
                        title=u'Canaima Popular',
                        description=u'Esta es la última versión de la Edición de escritorio Canaima Popular de la Metadistribución Canaima GNU/Linux.',
                        text=u'',
                        subjects=(u'Descargas', u'Obtener Canaima', u'Canaima Popular'),
                    ),
                    dict(
                        type='Document',
                        title=u'Canaima Educativo',
                        description=u'Esta es la última versión de la semilla de las canaimitas para "Canaima 1", "Canaima 2", "Canaima 3" y "Canaima Docente" del proyecto Canaima Educativo basado en "Canaima Popular 2.0 y 3.0".',
                        text=u'',
                        subjects=(u'Descargas', u'Obtener Canaima', u'Canaima Educativo'),
                    ),
                    dict(
                        type='Document',
                        title=u'Canaima Colibri',
                        description=u'Esta es la última versión de la Edición de escritorio Canaima Colibrí de la Metadistribución Canaima GNU/Linux.',
                        text=u'',
                        subjects=(u'Descargas', u'Obtener Canaima', u'Canaima Colibri'),
                    ),
                    dict(
                        type='Document',
                        title=u'Canaima Comunal',
                        description=u'Esta es la última versión de la Edición de escritorio Canaima Popular de la Metadistribución Canaima GNU/Linux, la cual fue lanzada el 14/11/2012.',
                        text=u'',
                        subjects=(u'Descargas', u'Obtener Canaima', u'Canaima Comunal'),
                    ),
                    dict(
                        type='Document',
                        title=u'Canaima Caribay',
                        description=u'Esta es la última versión de la Edición de escritorio Canaima Caribay de la Metadistribución Canaima GNU/Linux.',
                        text=u'',
                        subjects=(u'Descargas', u'Obtener Canaima', u'Canaima Caribay'),
                    ),
                    dict(
                        type='Document',
                        title=u'GeoCanaima',
                        description=u'Esta es la última versión de la Edición de escritorio GeoCanaima de la Metadistribución Canaima GNU/Linux.la cual fue lanzada el 31/10/2011.',
                        text=u'',
                        subjects=(u'Descargas', u'Obtener Canaima', u'GeoCanaima'),
                    ),
                ],
                # _layout='verifique-descarga-imagen-iso',
            ),
            dict(
                type='Document',
                title=u'Obtener códigos fuentes',
                description=u'Cada paquete fuente de la metadistribución Canaima GNU/Linux tiene asociada un repositorio de código fuente en repositorios Git. Estos repositorios de código fuente son actualizados y mantenidos por los desarrolladores.',
                text=u'',
                subjects=(u'Descargas', u'Obtener Canaima', u'Obtener códigos fuentes'),
            ),
            # dict(
            #     type='collective.cover.content',
            #     title=u'Complementos del RNA',
            #     description=u'Cada paquete fuente de la metadistribución Canaima GNU/Linux tiene asociada un repositorio de código fuente en repositorios Git. Estos repositorios de código fuente son actualizados y mantenidos por los desarrolladores.',
            #     text=u'',
            #     subjects=(u'Descargas', u'Obtener Canaima', u'Obtener códigos fuentes'),
            # ),
            dict(
                type='Folder',
                title=u'Complementos del RNA',
                description=u'El Repositorio Nacional de Aplicaciones (RNA), busca ser un espacio colaborativo de referencia, donde se encuentran y promueven aplicaciones, herramientas y proyectos en TI, que son desarrollados en Software Libre bajo estándares abiertos, de utilidad e interés para la Administración Pública y las comunidades organizadas.',
                subjects=(u'Descargas', u'Obtener Canaima', u'Complementos del RNA'),
                _addable_types=['Link'],
                _children=[
                    dict(
                        type='Link',
                        title=u'Administración',
                        description=u'Complementos del RNA sobre Administración',
                        remoteUrl='http://repositorio.softwarelibre.gob.ve/index.php?option=com_rnamain&task=showAllProjects&thematicId=317&lang=es',
                        subjects=(u'Descargas', u'Complementos del RNA', u'Administración'),
                    ),
                    dict(
                        type='Link',
                        title=u'Desarrollo',
                        description=u'Complementos del RNA sobre Desarrollo',
                        remoteUrl='http://repositorio.softwarelibre.gob.ve/index.php?option=com_rnamain&task=showAllProjects&thematicId=316&lang=es',
                        subjects=(u'Descargas', u'Complementos del RNA', u'Desarrollo'),
                    ),
                    dict(
                        type='Link',
                        title=u'Educación',
                        description=u'Complementos del RNA sobre ',
                        remoteUrl='http://repositorio.softwarelibre.gob.ve/index.php?option=com_rnamain&task=showAllProjects&thematicId=318&lang=es',
                        subjects=(u'Descargas', u'Complementos del RNA', u'Educación'),
                    ),
                    dict(
                        type='Link',
                        title=u'Ingeniería',
                        description=u'Complementos del RNA sobre Ingeniería',
                        remoteUrl='http://repositorio.softwarelibre.gob.ve/index.php?option=com_rnamain&task=showAllProjects&thematicId=319&lang=es',
                        subjects=(u'Descargas', u'Complementos del RNA', u'Ingeniería'),
                    ),
                    dict(
                        type='Link',
                        title=u'Multimedia',
                        description=u'Complementos del RNA sobre Multimedia',
                        remoteUrl='http://repositorio.softwarelibre.gob.ve/index.php?option=com_rnamain&task=showAllProjects&thematicId=313&lang=es',
                        subjects=(u'Descargas', u'Complementos del RNA', u'Multimedia'),
                    ),
                    dict(
                        type='Link',
                        title=u'Ofimática',
                        description=u'Complementos del RNA sobre Ofimática',
                        remoteUrl='http://repositorio.softwarelibre.gob.ve/index.php?option=com_rnamain&task=showAllProjects&thematicId=312&lang=es',
                        subjects=(u'Descargas', u'Complementos del RNA', u'Ofimática'),
                    ),
                    dict(
                        type='Link',
                        title=u'Seguridad',
                        description=u'Complementos del RNA sobre Seguridad',
                        remoteUrl='http://repositorio.softwarelibre.gob.ve/index.php?option=com_rnamain&task=showAllProjects&thematicId=315&lang=es',
                        subjects=(u'Descargas', u'Complementos del RNA', u'Seguridad'),
                    ),
                    dict(
                        type='Link',
                        title=u'Telecomunicaciones',
                        description=u'Complementos del RNA sobre Telecomunicaciones',
                        remoteUrl='http://repositorio.softwarelibre.gob.ve/index.php?option=com_rnamain&task=showAllProjects&thematicId=320&lang=es',
                        subjects=(u'Descargas', u'Complementos del RNA', u'Telecomunicaciones'),
                    ),
                    dict(
                        type='Link',
                        title=u'Otros',
                        description=u'Complementos del RNA sobre Otros',
                        remoteUrl='http://repositorio.softwarelibre.gob.ve/index.php?option=com_rnamain&task=showAllProjects&thematicId=321&lang=es',
                        subjects=(u'Descargas', u'Complementos del RNA', u'Otros'),
                    ),
                ],
            ),
        ],
    ),
    dict(
        type='Folder',
        title=u'Comunidad',
        description=u'Conozca los diversos modos de participación en comunidad Canaima GNU/Linux.',
        _layout='@@usersmap_view',
        _addable_types=['Folder', 'Document', 'File', 'Image', 'collective.cover.content', 'FSDFacultyStaffDirectory'],
        _children=[
            dict(
                type='Document',
                title=u'Unirse a Canaima',
                description=u'Las formas de participación en el proyecto Canaima son diversas, tanto para desarrolladores de GNU/Linux con experiencia como para recién llegados al mundo del Software Libre.',
                text=u'',
            ),
            dict(
                type='Document',
                title=u'Estar conectado',
                description=u'Conéctate con nosotros a través de las redes sociales y ayúdanos a socializar el proyecto Canaima en la Web.',
                text=u'',
            ),
            dict(
                type='Folder',
                title=u'Organización',
                description=u'Las formas de participación en el proyecto Canaima son diversas, tanto para desarrolladores de GNU/Linux con experiencia como para recién llegados al mundo del Software Libre.',
                # _addable_types=['Folder', 'Document', 'File', 'Image', 'News', 'collective.cover.content'],
            ),
            dict(
                type='Folder',
                title=u'Equipos',
                description=u'Si deseas ser parte de nuestra comunidad muy activa o darnos una mano haciendo de Canaima un mejor proyecto, canalizamos muchas maneras en las que puedes brindarnos tu ayuda.',
                # _addable_types=['Folder', 'Document', 'File', 'Image', 'News', 'collective.cover.content'],
            ),
            dict(
                type='Folder',
                title=u'Forja',
                description=u'Es el espacio colaborativo donde diversos chamanes, canaimeros y/o activistas en Canaima ayudan a forjar el proyecto usando lineamientos y herramientas que promueven la colaboración y mejoras continuas de los equipos de trabajos.',
                _addable_types=['Document', 'File', 'Image', 'News', 'collective.cover.content'],
            ),
            dict(
                type='Folder',
                title=u'Reuniones',
                description=u'La comunidad Canaima realiza periódicamente diversos encuentros formales e informales a continuación como Cayapa Canaima, Cayapa Técnica, Día Canaima, FLISOL, CNSL, entre otros.',
            ),
            dict(
                type='Folder',
                # type='FSDFacultyStaffDirectory',
                title=u'Grupos',
                description=u'Dentro de la comunidad Canaima existen diversidad de colectivos que son activistas, los cuales promueven la adopción e uso de tecnologías libres en sus ámbitos de acción de vida, por ejemplo vida comunitaria, vida académica, activismo político entre otros...',
            ),
            dict(
                type='Folder',
                title=u'Opinión',
                description=u'Este es un espacio para la opinión socio-política y cultural, ofreciendo un medio de expresión, información, debate y difusión de contenidos de interés colectivo, principalmente políticos, sociales, económicos y de promoción cultural.',
            ),
            dict(
                type='Folder',
                title=u'Galería de imágenes',
                description=u'Galería de imágenes del proyecto.',
            ),
        ],
    ),
    dict(
        type='Folder',
        title=u'Novedades',
        description=u'',
        _addable_types=['Folder', 'Collection', 'Event', 'News', 'Link', 'File', 'collective.cover.content'],
        _children=[
            dict(
                type='Folder',
                title=u'Artículos',
                description=u'Artículos de noticias.',
                excludeFromNav=True,
                _addable_types=['News Item', 'collective.cover.content'],
            ),
            dict(
                type='Folder',
                title=u'Eventos',
                description=u'Próximos eventos.',
                excludeFromNav=True,
                _addable_types=['Events'],
            ),
            dict(
                type='Link',
                title=u'Blogs',
                description=u'Planeta de Blogs del proyecto Canaima.',
                remoteUrl='https://colab.canaima.softwarelibre.gob.ve/planet/',
            ),
            dict(
                type='Collection',
                title=u'Comunidad',
                description=u'Novedades relacionadas al proyecto Canaima reportadas por miembros de la comunidad Canaima.',
                sort_reversed=True,
                sort_on=u'effective',
                limit=1000,
                query=[
                    dict(
                        i='portal_type',
                        o='plone.app.querystring.operation.selection.is',
                        v=['collective.nitf.content'],
                    ),
                    dict(
                        i='path',
                        o='plone.app.querystring.operation.string.relativePath',
                        v='../articulos',
                    ),
                    dict(
                        i='review_state',
                        o='plone.app.querystring.operation.selection.is',
                        v=['published'],
                    ),
                    dict(
                        i='genre',
                        o='plone.app.querystring.operation.selection.is',
                        v=['Current'],
                    ),
                    dict(
                        i='section',
                        o='plone.app.querystring.operation.selection.is',
                        v='Comunidad',
                    ),
                ],
                subjects=(u'Novedades', u'Noticias', u'Comunidad'),
            ),
            dict(
                type='Collection',
                title=u'Gobierno',
                description=u'Novedades relacionadas al proyecto Canaima reportadas por actores del Gobierno Venezolano.',
                sort_reversed=True,
                sort_on=u'effective',
                limit=1000,
                query=[
                    dict(
                        i='portal_type',
                        o='plone.app.querystring.operation.selection.is',
                        v=['collective.nitf.content'],
                    ),
                    dict(
                        i='path',
                        o='plone.app.querystring.operation.string.relativePath',
                        v='../articulos',
                    ),
                    dict(
                        i='review_state',
                        o='plone.app.querystring.operation.selection.is',
                        v=['published'],
                    ),
                    dict(
                        i='genre',
                        o='plone.app.querystring.operation.selection.is',
                        v=['Current'],
                    ),
                    dict(
                        i='section',
                        o='plone.app.querystring.operation.selection.is',
                        v='Gobierno',
                    ),
                ],
                subjects=(u'Novedades', u'Noticias', u'Gobierno'),
            ),
            dict(
                type='Collection',
                title=u'Discusiones',
                description=u'Espacio de opinión critica del proyecto Canaima reportadas por actores del Gobierno Venezolano.',
                sort_reversed=True,
                sort_on=u'effective',
                limit=1000,
                query=[
                    dict(
                        i='portal_type',
                        o='plone.app.querystring.operation.selection.is',
                        v=['collective.nitf.content'],
                    ),
                    dict(
                        i='path',
                        o='plone.app.querystring.operation.string.relativePath',
                        v='../articulos',
                    ),
                    dict(
                        i='review_state',
                        o='plone.app.querystring.operation.selection.is',
                        v=['published'],
                    ),
                    dict(
                        i='genre',
                        o='plone.app.querystring.operation.selection.is',
                        v=['Current'],
                    ),
                    dict(
                        i='section',
                        o='plone.app.querystring.operation.selection.is',
                        v='Discusiones',
                    ),
                ],
                subjects=(u'Novedades', u'Noticias', u'Discusiones'),
            ),
            dict(
                type='Collection',
                title=u'Actividades',
                description=u'Cronograma de actividades del proyecto Canaima.',
                sort_reversed=True,
                sort_on=u'effective',
                limit=1000,
                query=[
                    dict(
                        i='portal_type',
                        o='plone.app.querystring.operation.selection.is',
                        # v=['collective.nitf.content'],
                        v=['Events'],
                    ),
                    dict(
                        i='path',
                        o='plone.app.querystring.operation.string.relativePath',
                        v='../eventos',
                    ),
                    dict(
                        i='review_state',
                        o='plone.app.querystring.operation.selection.is',
                        v=['published'],
                    ),
                ],
                subjects=(u'Novedades', u'Noticias', u'Actividades'),
            ),
        ],
    ),
]

SITE_STRUCTURE = _add_id(SITE_STRUCTURE)
