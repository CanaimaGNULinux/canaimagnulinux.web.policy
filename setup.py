from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='canaimagnulinux.web.policy',
      version=version,
      description="A Plone 4.3 policy product for customizing a Plone site",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
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
          'plone.api==1.3.2',
          # -*- Extra requirements: -*-
          'Products.CMFPlacefulWorkflow',
          'plone.app.ldap==1.3.1',
          'collective.geo.usersmap',
          'collective.googleanalytics',
          'collective.googlenews==1.0rc3',
          'collective.disqus==2.0rc1',
          'collective.facebook.portlets==1.0b2',
          'collective.twitter.portlets==1.0b3',
          'collective.twitter.tweet==1.0b3',
          'sc.social.like==2.1',
          'collective.nitf==1.0b4',
          'collective.upload==1.0rc1',
          'collective.polls==1.6.2',
          'collective.cover==1.0a11',
          'Products.Doormat==1.0',
          'Products.PloneFormGen==1.7.16',
          'Products.PloneSoftwareCenter==1.6.4',
          'Products.PloneServicesCenter==0.2.7',
          'Products.FacultyStaffDirectory==3.1.3',
          'canaimagnulinux.web.theme',
      ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
