"""Compatibility imports for http.client/httplib"""

from ..six import MovedModule, _importer

# Create the module
http_client = MovedModule("http_client", "httplib", "http.client")

# Import all the necessary components
if http_client.mod == "http.client":
    from http.client import *
    from http.client import IncompleteRead
else:
    from httplib import *
    from httplib import IncompleteRead

# Make everything available
__all__ = ["IncompleteRead"] 