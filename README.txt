
Introduction
============

Complete silliness: This Plone theme makes your site look like Alex Clark's Twitter profile::

    http://twitter.com/aclark4life

That's it.

Installation
------------

Add ``plonetheme.aclark_twitter`` to the ``eggs`` parameter of your
``plone.recipe.zope2instance`` section::

    [plone]
    recipe = plone.recipe.zope2instance
    eggs = 
        ...
        plonetheme.aclark_twitter

Now run buildout, restart Plone, and install the theme in Site Setup ->
Add-ons.
