# -*- coding: utf-8 -*-
"""
webapp2
=======
webapp2 is a lightweight Python web framework compatible with Google App
Engine's `webapp <http://code.google.com/appengine/docs/python/tools/webapp/>`_.

webapp2 is a `single file <http://code.google.com/p/webapp-improved/source/browse/webapp2.py>`_
that follows the simplicity of webapp, but improves it in some ways:
it extends webapp to offer better URI routing and exception handling,
a full featured response object and a more flexible dispatching mechanism.

webapp2 also offers the package `webapp2_extras <http://code.google.com/p/webapp-improved/source/browse/#hg%2Fwebapp2_extras>`_
with several optional utilities: sessions, localization, internationalization,
domain and subdomain routing, secure cookies and support for threaded
environments.

webapp2 can also be used outside of Google App Engine, independently of the
App Engine SDK.

For a complete description of how webapp2 improves webapp, see
`webapp2 features <http://webapp-improved.appspot.com/features.html>`_.

Quick links
-----------

- `User Guide <http://webapp-improved.appspot.com/>`_
- `Official Repository <http://code.google.com/p/webapp-improved/>`_
- `Discussion Group <https://groups.google.com/forum/#!forum/webapp2>`_
- `@webapp2 <https://twitter.com/#!/webapp2>`_
"""
from setuptools import setup

setup(
    name = 'webapp2',
    version = '2.1',
    license = 'Apache Software License',
    url = 'http://webapp-improved.appspot.com',
    description = "Taking Google App Engine's webapp to the next level!",
    long_description = __doc__,
    author = 'Rodrigo Moraes',
    author_email = 'rodrigo.moraes@gmail.com',
    zip_safe = False,
    platforms = 'any',
    py_modules = [
        'webapp2',
    ],
    packages = [
        'webapp2_extras',
    ],
    include_package_data=True,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)