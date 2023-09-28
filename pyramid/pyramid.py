
def get_max_blocks(height: int):
    blocks = 0
    blocks_in_level = 0
    for h in height:
        blocks_in_level += 1
        blocks += blocks_in_level
    return blocks

def get_min_blocks(height: int):
    pass

def get_height(blocks: int):
    pass
