"""Compatibility imports for urllib.error"""

from ..six import _MovedItems, MovedModule, _importer

# Initialize urllib_error
urllib_error = _MovedItems(__name__)

# Add error classes
from urllib.error import (
    URLError, HTTPError, ContentTooShortError
)

# Make the urllib_error module available
__all__ = ["URLError", "HTTPError", "ContentTooShortError"]
