
# --------------------------------------------------------------------------------- #

class Tile:
    """Represents a tile"""
    def __init__(self):
        self.index: int = -1

        # TODO: edge class
        self.edges: list = []

        # TODO: options class
        self.up: list = []
        self.right: list = []
        self.down: list = []
        self.left: list = []

    def set_rules(self, tiles: list['Tile']):
        """Set the rules for each tile"""
        for tile in tiles:
            # up
            if self.edges[0] == tile.edges[2]:
                self.up.append(tile)
            # right
            if self.edges[1] == tile.edges[3]:
                self.right.append(tile)
            # down
            if self.edges[2] == tile.edges[0]:
                self.down.append(tile)
            # left
            if self.edges[3] == tile.edges[1]:
                self.left.append(tile)
