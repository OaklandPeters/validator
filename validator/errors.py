"""
Defines all exception types raised by this package.
"""

class ValidationError(Exception):
    """Root exception type for the validator/ package."""

class TypeValidationError(ValidationError, TypeError):
    """Invalid argument type into a function. Equivalent of TypeError."""

class KeyValidationError(ValidationError, KeyError):
    """Mapping object is missing a required key."""
