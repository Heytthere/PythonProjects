import random

def roll():
    min_value=1
    max_value=6

    return random.randint(min_value,max_value)

print("Hello and Welcome to the dice game")    
print("The total number of players should be between 2 to 5 only! ")

while True:    
    players = input("Press enter the number of players: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 5:
            break
        else:
                print("Error... The number of players should be between 2 to 5 only! ")
    else:
        print("Invalid value, try again..")

max_score = 50
players_scores = [ 0 for _ in range(players)]

while max(players_scores) < max_score:    
    for player_inx in range(players):
        print("\nPlayer no.",player_inx + 1,"'s turn has started") 
        print("Your total score is :",players_scores[player_inx],"\n")
        current_score=0

        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1, Hence you lose your turn!")
                current_score = 0
                break
            else:
                current_score +=  value
                print("You rolled a :",value)
                print("Your score is :",current_score)

        players_scores[player_inx] = current_score
        print("Your total score is :",players_scores[player_inx])

max_score = max(players_scores)
winning_inx = players_scores.index(max_score)
print("Winning player is:",winning_inx+1,"with the score of: ",max_score)

        