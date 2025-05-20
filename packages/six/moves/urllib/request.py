"""Compatibility imports for urllib.request"""

from ...six import _MovedItems, MovedModule, _importer

# Initialize request
request = _MovedItems(__name__)

# Add request functions and classes
from urllib.request import (
    urlopen, install_opener, build_opener, pathname2url, url2pathname,
    getproxies, Request, OpenerDirector, HTTPDefaultErrorHandler,
    HTTPRedirectHandler, HTTPCookieProcessor, ProxyHandler,
    BaseHandler, HTTPPasswordMgr, HTTPPasswordMgrWithDefaultRealm,
    AbstractBasicAuthHandler, HTTPBasicAuthHandler, ProxyBasicAuthHandler,
    AbstractDigestAuthHandler, HTTPDigestAuthHandler, ProxyDigestAuthHandler,
    HTTPHandler, HTTPSHandler, FileHandler, FTPHandler, CacheFTPHandler,
    UnknownHandler, HTTPErrorProcessor, urlretrieve, urlcleanup,
    URLopener, FancyURLopener, proxy_bypass, parse_http_list,
    parse_keqv_list
)

# Make the request module available
__all__ = [
    "urlopen", "install_opener", "build_opener", "pathname2url", "url2pathname",
    "getproxies", "Request", "OpenerDirector", "HTTPDefaultErrorHandler",
    "HTTPRedirectHandler", "HTTPCookieProcessor", "ProxyHandler",
    "BaseHandler", "HTTPPasswordMgr", "HTTPPasswordMgrWithDefaultRealm",
    "AbstractBasicAuthHandler", "HTTPBasicAuthHandler", "ProxyBasicAuthHandler",
    "AbstractDigestAuthHandler", "HTTPDigestAuthHandler", "ProxyDigestAuthHandler",
    "HTTPHandler", "HTTPSHandler", "FileHandler", "FTPHandler", "CacheFTPHandler",
    "UnknownHandler", "HTTPErrorProcessor", "urlretrieve", "urlcleanup",
    "URLopener", "FancyURLopener", "proxy_bypass", "parse_http_list",
    "parse_keqv_list"
]
