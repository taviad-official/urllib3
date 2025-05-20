"""Compatibility imports for urllib.robotparser"""

from ...six import _MovedItems, MovedModule, _importer

# Initialize robotparser
robotparser = _MovedItems(__name__)

# Add robotparser class
from urllib.robotparser import RobotFileParser

# Make the robotparser module available
__all__ = ["RobotFileParser"]
