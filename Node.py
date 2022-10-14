"""Defines the node class."""
from Track import Track

class Node():
    """Node class."""

    def __init__(self, name: str, max_capacity: int, is_end: bool, pos):
        """Set variables for Node calss."""
        self.name = name
        self.max_capacity = max_capacity
        self.full = False
        self.edges_dict = dict()
        self.end = is_end
        self.pos = pos
        self.travellers=0
        if len(self.pos) != 2:
            raise Exception("pos must be a 2D position")

    def __repr__(self):
        """Return the name of the node."""
        return self.name

    def add_edge(self, track: Track):
        """Add edge to the node."""
        self.edges_dict[track] = track.weight

    def ideal_track(self):
        """Calculate the ideal track."""
        return max(self.edges_dict, key=self.edges_dict.get)

# class Node_Pair():
#     def __init__(self, max_capacityN1, max_capacityT1, max_capacityN2, dist):
