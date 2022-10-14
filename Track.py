"""Define the Track class."""
from Agent import Agent


class Track():
    """Track class."""

    def __init__(self, distance: int, max_capacity: int, node1, node2,
                 weight: int, name: str):
        """Set the variables for the Track class."""
        self.travellers = 0
        self.name = name
        self.distance = distance
        self.max_capacity = max_capacity
        self.full = False
        self.weight = weight
        self.start_node = node1
        self.end_node = node2

        node1.add_edge(self)
        node2.add_edge(self)

    def __repr__(self):
        """Return the name of the track."""
        return self.name

    def update_full(self):
        """Update the number of travellers on the track."""
        if self.travellers == self.max_capacity:
            self.full = True
        elif 0 <= self.travellers < self.max_capacity:
            self.full = False
        else:
            raise Exception("negative number of travellers - spooky")

    def add_if_can(self, agent: Agent):
        """Add the agent to the track if possible."""
        self.update_full()

        if not self.full:
            self.travellers += 1
            self.start_node.travellers -= 1
            agent.element = "Track"
            agent.current_track = self
            self.update_full()
            return
        else:
            return

    def remove(self, agent):
        """Remove and agent from the track."""
        self.update_full()
        self.travellers -= 1
        agent.elemt = "Node"
        self.update_full()
