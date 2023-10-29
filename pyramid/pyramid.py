def get_max_blocks(height: int):
    blocks = 0
    for h in range(1, height + 1):  # Fix here: `height` should be integer, not iterable
        blocks += h
    return blocks

def get_min_blocks(height: int):
    # In a pyramid, the minimum blocks required are the same as the maximum blocks
    return get_max_blocks(height)

def get_height(blocks: int):
    height = 0
    while blocks > 0:
        height += 1
        blocks -= height
    if blocks < 0:
        return height - 1
    return height
