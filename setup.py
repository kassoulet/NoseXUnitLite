#-*- coding: utf-8 -*-
import sys
import distutils.util

if sys.version_info[0] > 2 or (sys.version_info[0] == 2 and sys.version_info[1] >= 5):
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup
else:
    import warnings
    warnings.warn('setuptools not used')
    from distutils.core import setup

execfile(distutils.util.convert_path('nosexunitlite/__init__.py'))

setup(
    name = "NoseXUnitLite",
    version = __version__,
    description = "XML Output plugin for Nose",
    long_description = "A plugin for nose/nosetests that produces an XML report of the result of a test.",
    author = "Olivier Mansion & Gautier Portet",
    author_email = "kassoulet@gmail.com",
    zip_safe = True,
    license = "GNU Library or Lesser General Public License (LGPL)",
    url = "http://",
    packages = ['nosexunitlite'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        ],
    install_requires = ['nose >= 0.11.1'],
    entry_points = {'nose.plugins.0.10': [ 'nosexunitlite = nosexunitlite.plugin:NoseXUnitLite' ], },
    test_suite = 'nose.collector',
)

