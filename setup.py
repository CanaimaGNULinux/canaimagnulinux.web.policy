from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='canaima.policy',
      version=version,
      description="A Plone 3 policy product for customizing a Plone site",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone3 policy product canaima gnu linux website',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://gitorious.org/plataforma-canaima/canaima.policy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['canaima'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
