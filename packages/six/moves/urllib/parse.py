"""Compatibility imports for urllib.parse"""

from ...six import _MovedItems, MovedModule, _importer

# Initialize parse
parse = _MovedItems(__name__)

# Add parse functions
from urllib.parse import (
    ParseResult, SplitResult, parse_qs, parse_qsl, urldefrag,
    urljoin, urlparse, urlsplit, urlunparse, urlunsplit,
    quote, quote_plus, unquote, unquote_plus, unquote_to_bytes,
    urlencode, splitquery, splittag, splituser, splitvalue,
    uses_fragment, uses_netloc, uses_params, uses_query,
    uses_relative
)

# Make the parse module available
__all__ = [
    "ParseResult", "SplitResult", "parse_qs", "parse_qsl", "urldefrag",
    "urljoin", "urlparse", "urlsplit", "urlunparse", "urlunsplit",
    "quote", "quote_plus", "unquote", "unquote_plus", "unquote_to_bytes",
    "urlencode", "splitquery", "splittag", "splituser", "splitvalue",
    "uses_fragment", "uses_netloc", "uses_params", "uses_query",
    "uses_relative"
] 