from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='TheGreyLandscape',
      version=version,
      description="The Grey Landscape, Core Flux",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Alchemist Glacialis',
      author_email='alch.glacialis@thegreylandscape.com',
      url='http://thegreylandscape.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'WebCore',
          'Elixir',
          'SQLAlchemy'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      paster_plugins = ['PasteScript', 'WebCore']
      )
