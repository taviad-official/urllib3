"""Compatibility imports for Python 2/3"""

from ..six import _MovedItems, MovedModule, MovedAttribute, _importer

# Initialize moves
moves = _MovedItems(__name__)

# Add http_client
from . import http_client

# Add queue
from . import queue

# Add urllib
from . import urllib

# Add xrange
xrange = MovedAttribute("xrange", "__builtin__", "builtins", "xrange", "range")

# Make the moves module available
__all__ = ["moves", "http_client", "queue", "urllib", "xrange"]