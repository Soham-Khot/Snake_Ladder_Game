snake_pos = {99:54,70:55,52:42,25:2,95:72}
ladder_pos = {6:25,11:40,17:69,46:90,60:85}


def check_snake_or_ladder(name : str,position : int) -> int:
    """check Whether it is on snake head or ladder's bottom"""
    pre =position
    if position in snake_pos :
        position=snake_pos[position]
        print(f"{name} came a from {pre} to {position}")
        return position
    if position in ladder_pos:
        position = ladder_pos[position]
        print(f"{name} climbed a ladder from {pre} to {position}")
        return position
    return position