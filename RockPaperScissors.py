import random

from ConfigFromFile import get_config

def display(message):
    print(message)

def get_input_string(message):
    return input(message)

def get_input_int(message):
    return int(get_input_string(message))

def determine_winner(player, computer, name):
    if player == computer:
        result = "Draw"
    elif (player + 1)%3 == computer:
        result = f"{name} wins"
    elif (computer + 1)%3 == player:
        result = "Computer Wins"
    return result

def get_user_choice_request(weapons):
    request = "Select "
    for counter in range(len(weapons)):
        request += str(counter) + " for " + weapons[counter] + " "
    return request

def get_user_choice(weapons):
    request = get_user_choice_request(weapons)
    player = get_input_int(request)
    if player in [0, 1, 2]:
        display("You selected " + weapons[player])
    return player

def get_computer_choice(weapons):
    chosen = random.randint(0,2)
    display("Computer chose " + weapons[chosen])
    return chosen

def get_list_of_games(property):
    property = get_config()
    list_of_games = []
    for counter in range(1, len(property)):
        list_of_games.append(property[counter].split(":")[0])
    return list_of_games

def get_weapon_lists(property):
    weapon_lists = []
    for counter in range(1, len(property)):
        weapon_lists.append(property[counter].split(":")[1].split(","))
    return weapon_lists

def get_games_request(list_of_games):
    request = "Please select"
    for counter in range(len(list_of_games)):
        request += " " + str(counter) + " - " + list_of_games[counter]
    return request

def generate_games_list_request(property):
    list_of_games = get_list_of_games(property)
    request = get_games_request(list_of_games)
    return request

def get_game():
    property = get_config()
    request = generate_games_list_request(property)
    user_game = get_input_int(request)
    weapons_lists = get_weapon_lists(property)
    return weapons_lists[user_game]

def play():
    name = get_input_string("Enter your name: ")
    weapon = get_game()
    player = get_user_choice(weapon)
    while player in [0, 1, 2]:
        
        computer = get_computer_choice(weapon)
        result = determine_winner(player, computer, name)
        display(result)
        player = get_user_choice(weapon)

if __name__ == "__main__":
    play()




