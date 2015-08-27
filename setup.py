from setuptools import setup, find_packages
import os

version = '0.1'
description = 'The Website for Canaima GNU/Linux project'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open(os.path.join('docs', 'HISTORY.rst')).read()
)

setup(name='canaimagnulinux.web.policy',
      version=version,
      description=description,
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business :: Groupware",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone4 policy product canaima gnu linux website',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/CanaimaGNULinux/canaimagnulinux.web.policy',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['canaimagnulinux', 'canaimagnulinux.web'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Products.CMFPlacefulWorkflow',
          'Products.Doormat==1.0',
          'Products.FacultyStaffDirectory==3.1.3',
          'Products.PloneFormGen==1.7.16',
          'Products.PloneServicesCenter==0.2.7',
          'Products.PloneSoftwareCenter==1.6.4',
          'plone.api==1.3.2',
          'plone.app.ldap==1.3.1',
          'canaimagnulinux.web.theme',
          'collective.cover==1.0a11',
          'collective.disqus==2.0rc1',
          'collective.facebook.portlets==1.0b2',
          'collective.geo.usersmap',
          'collective.googleanalytics',
          'collective.googlenews==1.0rc3',
          'collective.nitf==1.0b4',
          'collective.opendata==1.0a2',
          'collective.polls==1.6.2',
          'collective.twitter.portlets==1.0b3',
          'collective.twitter.tweet==1.0b3',
          'collective.upload==1.0rc1',
          'sc.social.like==2.1',
      ],
      extras_require={
          'test': [
              'plone.app.robotframework',
              'plone.app.testing [robot] >=4.2.2',
              'plone.browserlayer',
              'plone.testing',
              'robotsuite',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
