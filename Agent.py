"""Defines the agent class."""


class Agent:
    """Agent class."""

    def __init__(self, speed, initial_node):
        """Set variables of agent."""
        self.speed = speed
        self.current_node = initial_node
        self.current_track = None
        self.exit = False
        self.element = "Node"
        self.timer = 0
        initial_node.travellers += 1

    def __repr__(self):
        """Return the element of the agent."""
        return self.element

    def exit(self):
        """Exit the agent."""
        self.exit = True
