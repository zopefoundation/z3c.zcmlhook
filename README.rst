Introduction
============

This package provides means of hooking into the Zope (ZCML) configuration
process.

Custom ZCML actions
-------------------

It is sometimes useful to execute a function during the execution of 
configuration actions, for example to perform one-off configuration that does
not warrant a new directive. The ``<zcml:customAction />`` directive is
provided for this purpose.

For example, you may want to call a function called
``my.package.finalConfiguration()`` "late" in the configuration action
execution cycle. This can be achieved with the following ZCML statements::

    <configure
        xmlns="http://namespaces.zope.org/zope"
        xmlns:zcml="http://namespaces.zope.org/zcml"
        i18n_domain="my.package">
        
        <include package="z3c.zcmlhook" file="meta.zcml" />
        
        <zcml:customAction
            handler="my.package.finalConfiguration"
            order="9999"
            />
        
    </configure>

The ``handler`` attribute gives the name of a function to execute. The
function should take no arguments. The ``order`` attribute is optional, and
can be used to influence when in the configuration cycle the function is
executed. The default value for this, as for most Zope configuration actions,
is ``0``.

Overriding custom actions
-------------------------

If you want to override the invocation of a custom handler in an
``overrides.zcml``, you need to tell ``zope.configuration`` which handler to
override. You can do that by setting the *discriminator* explicitly. A
discriminator is used to uniquely identify a configuration action. In the
case of the ``<zcml:customAction />`` directive, the discriminator is based
on the full dotted name to the function by default. Thus, you could override
the function call above like so::

        <zcml:customAction
            handler="my.otherpackage.overrideFinalConfiguration"
            discriminator="my.package.finalConfiguration"
            order="9999"
            />

Using a handler more than once
------------------------------

The ``discriminator`` attribute can also be used to explicitly allow using
the same handler more than once. If you wanted to call
``my.package.finalConfiguration`` again, you would normally get a
configuration conflict. However, with a (unique) custom discriminator, the
second call is allowed::

        <zcml:customAction
            handler="my.package.finalConfiguration"
            discriminator="my.package.finalConfiguration:early"
            order="-9999"
            />

        <zcml:customAction
            handler="my.package.finalConfiguration"
            discriminator="my.package.finalConfiguration:late"
            order="9999"
            />

Here, we are attempting to call our configuration action "very early" as
well as "very late" in the configuration process.
