"""


@note: These should include type-checking, dispatch, and MAYBE logic
@note: These generic functions might be better replaced with ABFs.
"""
from . import interfaces
from . import errors


def Assert(subject, category):
    """Generic function for 
    """
    _asserttype(category, interfaces.CategoryInterface)
    _asserttype(category, interfaces.AsserterInterface)


def Check(subject, category):
    _asserttype(category, interfaces.CategoryInterface)
    _asserttype(category, interfaces.CheckerInterface)

def Ensure(subject, category):
    pass

def EnsureDispatch(subject, category, interface):
    pass


# Local utility functions
def _asserttype(obj, klass):
    if not isinstance(obj, klass):
        raise errors.TypeValidationError(
            "Should be {0}".format(klass.__name__)
        )
