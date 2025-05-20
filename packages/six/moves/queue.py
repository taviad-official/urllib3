"""Compatibility imports for queue/Queue"""

from ..six import MovedModule, _importer

# Create the module
queue = MovedModule("queue", "Queue", "queue")

# Import all the necessary components
if queue.mod == "queue":
    from queue import *
else:
    from Queue import *

# Make everything available
__all__ = ["Empty", "Full", "Queue", "LifoQueue", "PriorityQueue", "SimpleQueue"] 