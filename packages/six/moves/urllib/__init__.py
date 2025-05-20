"""Compatibility imports for urllib"""

from ...six import _MovedItems, MovedModule, _importer

# Initialize urllib
urllib = _MovedItems(__name__)

# Add parse
from . import parse

# Add error
from . import error

# Add request
from . import request

# Add response
from . import response

# Add robotparser
from . import robotparser

# Make the urllib module available
__all__ = ["urllib", "parse", "error", "request", "response", "robotparser"]
