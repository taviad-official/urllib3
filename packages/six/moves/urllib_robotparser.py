"""Compatibility imports for urllib.robotparser"""

from ..six import _MovedItems, MovedModule, _importer

# Initialize urllib_robotparser
urllib_robotparser = _MovedItems(__name__)

# Add robotparser class
from urllib.robotparser import RobotFileParser

# Make the urllib_robotparser module available
__all__ = ["RobotFileParser"]
