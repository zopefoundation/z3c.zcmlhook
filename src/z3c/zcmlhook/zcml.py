from zope import schema
from zope.configuration.fields import GlobalObject
from zope.interface import Interface


class ICustomActionDirective(Interface):

    handler = GlobalObject(
        title="Function to execute",
        description="This function will be executed during ZCML processing",
        default=None,
        required=True,
    )

    order = schema.Int(
        title="Execution order",
        description=(
            "Set to a high number to execute late, or a negative number to"
            " execute early"),
        default=0,
        required=False,
    )

    discriminator = schema.ASCIILine(
        title="Custom discriminator",
        description="By default, the full dotted name to the handler "
        "function is used as the discriminator. If you want "
        "to use the same function more than once, or if you "
        "want to override a custom action defined elsewhere "
        "with an overrides.zcml, you can set the "
        "discriminator explicitly.",
        default=None,
        required=False,
    )


def customAction(_context, handler, order=0, discriminator=None):
    if discriminator is None:
        discriminator = f"{handler.__module__}.{handler.__name__}"

    _context.action(
        discriminator=("executeCustomFunction", discriminator),
        callable=handler,
        args=(),
        order=order)
