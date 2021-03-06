from setuptools import setup, find_packages
import os

version = '1.3'

setup(name='plonetheme.aclark_twitter',
      version=version,
      description="Complete silliness: make your Plone site look like Alex Clark's Twitter profile.",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      # Get more strings from
      # https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme aclark twitter cms',
      author='Alex Clark',
      author_email='aclark@aclark.net',
      maintainer='Leonardo Caballero',
      maintainer_email='leonardocaballero@gmail.com',
      url='https://github.com/collective/plonetheme.aclark_twitter/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
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
      test_suite='plonetheme.aclark_twitter.tests.test_suite',
      )
