import roll_dice 

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

def move_player(position : int , dice : int ) -> int :
    """it will move player according to currect dice number"""
    updated_position = position+dice
    if updated_position>100:
        print("Greater than 100!")
        return position
    return updated_position

def display_position(name : str,position : int)-> None:
    print(f"{name} is at position {position}")


def play_game():
    """main fun to start game"""
    turn = 1
    print("-- Snake and Ladder Game Started ---")
    while True:
        """run util user first give valid name"""
        player_1 = input("Enter first player name : ")
        if not "".join(player_1.split()).isalpha():
            print("Enter valid name!!")
            continue
        break;
    player_1_pos = 0

    while True:
        """run util user second give valid name"""
        player_2 = input("Enter Second player name : ")
        if not "".join(player_2.split()).isalpha():
            print("Enter valid name!!")
            continue
        break;

    player_2_pos = 0

    while True:
        """runs until someone will win"""
        if turn == 1:
            n = input(f"{player_1} click Enter :")
            current_roll = roll_dice.roll_dice()
            player_1_pos = move_player(player_1_pos,current_roll)
            check_snake_or_ladder(player_1,player_1_pos)
            display_position(player_1,player_1_pos)
            if player_1_pos == 100:
                print(f"{player_1} Won the Game!!!!!")
                break;
            turn = 2
        else:
            n = input(f"{player_2} click Enter :")
            current_roll = roll_dice.roll_dice()
            player_2_pos = move_player(player_2_pos,current_roll)
            check_snake_or_ladder(player_2,player_2_pos)
            display_position(player_2,player_2_pos)
            if player_2_pos == 100:
                print(f"{player_2} Won the Game!!!!")
                break;
            turn = 1

if __name__ == "__main__":
    play_game()
