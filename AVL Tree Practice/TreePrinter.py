import math
class TreePrinter:
    def node_tile(self,value,spaces):
        value_tile = spaces//2 - 1
        value_char = str(value) if value is not None else " "
        prefix = " " * value_tile
        suffix = " " * (spaces//2)
        return prefix + value_char + suffix

    def get_str(self,tree):
        self.tree = tree
        if self.tree.root is None:
            return ""
        self.height = tree.height(tree.root)
        # self.spaces = 2 * (2 ** math.ceil(math.log(self.height,2)))
        self.spaces = 2 * (2 ** (self.height-1))

        queue = [tree.root]
        printed = ""
        for level in range(self.height):
            num_tiles = 2**level            
            tile_spaces = self.spaces//num_tiles
            next_queue = []
            for tile in queue:
                if tile is None:
                    next_queue.extend([None,None])
                else:
                    next_queue.append(tile.left)
                    next_queue.append(tile.right)

                printed += self.node_tile(tile,tile_spaces)

            printed += "\n"
            queue = next_queue
        return printed