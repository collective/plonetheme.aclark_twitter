=========================
plonetheme.aclark_twitter
=========================

This Plone theme is inspired by a *complete silliness*: make your Plone site look 
like `Alex Clark's Twitter Profile`_.

Introduction
============

ACLARK's Twitter is an installable Plone Theme developed by `ACLARK.NET, LLC`_, 
using the **skins theme** features and **python egg** packaging.

Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/plonetheme.aclark_twitter/raw/master/screenshot.png


Features
========

- It's an installable Plone Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- It's have support clean uninstallation.


Installation
============


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``plonetheme.aclark_twitter`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.aclark_twitter


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.aclark_twitter',
    ],


Plock
-----

Install with `Plock`_: ::

    $ pip install plock
    $ plock -a plonetheme.aclark_twitter .


Contribute
==========

- Issue Tracker: https://github.com/collective/plonetheme.aclark_twitter/issues
- Source Code: https://github.com/collective/plonetheme.aclark_twitter


License
=======

The project is licensed under the GPLv2.

Credits
-------

- Alex Clark (aclark at aclark dot net).
- Leonardo J. Caballero G. (leonardocaballero at gmail dot com).

.. _`Alex Clark's Twitter Profile`: https://twitter.com/aclark4life
.. _`ACLARK.NET, LLC`: http://www.aclark.net/
.. _`Plock`:https://pypi.org/project/plock/