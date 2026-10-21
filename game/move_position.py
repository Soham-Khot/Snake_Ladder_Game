def move_player(position : int , dice : int ) -> int :
    """it will move player according to currect dice number"""
    updated_position = position+dice
    if updated_position>100:
        print("Greater than 100!")
        return position
    return updated_position