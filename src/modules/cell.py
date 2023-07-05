import random


class Cell:
    """Represents a cell"""
    def __init__(self, options) -> None:
        self.options: list = options
        self.collapsed: bool = False
    
    def entropy(self) -> int:
        """Return the entropy of options"""
        return len(self.options)
    
    def update(self) -> None:
        """Update the collapsed variable"""
        self.collapsed = bool(self.entropy() == 1)
    
    def observe(self) -> None:
        """observe (collapse) the cell"""
        try:
            self.options = [random.choice(self.options)]
            self.collapsed = True
        except:
            return