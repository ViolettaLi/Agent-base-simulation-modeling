"""Defines and runs simulation."""
from Propagate import propagate
from gui import *

agents, tracks = guis()

print(propagate(agents, tracks, dt=0.1, animate=True))
