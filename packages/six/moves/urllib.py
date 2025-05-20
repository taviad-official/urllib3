"""Compatibility imports for urllib"""

from ..six import _MovedItems, MovedModule, _importer

# Initialize urllib
urllib = _MovedItems(__name__)

# Add parse
from . import urllib_parse

# Add error
from . import urllib_error

# Add request
from . import urllib_request

# Add response
from . import urllib_response

# Add robotparser
from . import urllib_robotparser

# Make the urllib module available
__all__ = ["urllib", "urllib_parse", "urllib_error", "urllib_request", "urllib_response", "urllib_robotparser"]
