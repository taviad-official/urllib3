"""Compatibility imports for urllib.response"""

from ..six import _MovedItems, MovedModule, _importer

# Initialize urllib_response
urllib_response = _MovedItems(__name__)

# Add response functions
from urllib.response import (
    addbase, addclosehook, addinfo, addinfourl
)

# Make the urllib_response module available
__all__ = ["addbase", "addclosehook", "addinfo", "addinfourl"]
