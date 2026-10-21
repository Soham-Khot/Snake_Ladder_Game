import roll_dice
import display_positon
import check_snake_or_ladder
import move_position

def play_game():
    """main fun to start game"""
    turn = 1
    print("-- Snake and Ladder Game Started ---")
    while True:
        """run util user first give valid name"""
        player_1 = input("Enter first player name : ")
        if not "".join(player_1.strip().split()).isalpha():
            print("Enter valid name!!")
            continue
        break;
    player_1_pos = 0

    while True:
        """run util user second give valid name"""
        player_2 = input("Enter Second player name : ")
        if not "".join(player_2.strip().split()).isalpha():
            print("Enter valid name!!")
            continue
        break;

    player_2_pos = 0

    while True:
        """runs until someone will win"""
        if turn == 1:
            n = input(f"{player_1} click Enter :")
            current_roll = roll_dice.roll_dice()
            player_1_pos = move_position.move_player(player_1_pos,current_roll)
            # print(f"{player_1} == {player_1_pos}")
            player_1_pos = check_snake_or_ladder.check_snake_or_ladder(player_1,player_1_pos)
            display_positon.display_position(player_1,player_1_pos)
            if player_1_pos == 100:
                print(f"{player_1} Won the Game!!!!!")
                break;
            turn = 2
        else:
            n = input(f"{player_2} click Enter :")
            current_roll = roll_dice.roll_dice()
            player_2_pos = move_position.move_player(player_2_pos,current_roll)
            # print(f"{player_2} == {player_2_pos}")
            player_2_pos = check_snake_or_ladder.check_snake_or_ladder(player_2,player_2_pos)
            display_positon.display_position(player_2,player_2_pos)
            if player_2_pos == 100:
                print(f"{player_2} Won the Game!!!!")
                break;
            turn = 1
        print("-"*50)

if __name__ == "__main__":
    play_game()
