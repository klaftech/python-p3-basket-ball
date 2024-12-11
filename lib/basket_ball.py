def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


"""
JS:
function numPointsScored(name) {
    const game = gameObject();
    for (const teamKey in game) {
        const playersObj = game[teamKey]["players"];
        for (const playerKey in playersObj) {
            if (playerKey === name) {
                const playerStats = playersObj[playerKey];
                return playerStats.points;
            }
        }
        }
    }
"""

# def num_points_per_game(player_name):
#     dict = game_dict()
#     for team in dict:
#         player = [player.get("points_per_game") for player in dict[team]["players"] if player.get("name") == player_name]
#         if player != []:
#             return player[0]
#     return "player not found"
# print(num_points_per_game("Jarrett Allen"))


def decorator(original_func):
    def wrapper(*args):
        dict = game_dict()
        for team in dict:
            
            #call the outer function
            params = original_func(*args)
            player_name = params.get("player_name")
            filter = params.get("filter")

            player = [player.get(filter) for player in dict[team]["players"] if player.get("name") == player_name]
            if player != []:
                return player[0]
        return "player not found"
    return wrapper

@decorator
def num_points_per_game(player_name):
    return {"player_name": player_name, "filter": "points_per_game"}

@decorator
def player_age(player_name):
    return {"player_name": player_name, "filter": "age"}

@decorator
def player_shoe_brand(player_name):
    return {"player_name": player_name, "filter": "shoe_brand"}



print(num_points_per_game("Rui Hachimura"))
print(player_age("Rui Hachimura"))
print(player_shoe_brand("Rui Hachimura"))



def get_team(team_name):
    dict = game_dict()
    for team_away in dict:
        team = dict[team_away]["team_name"]
        if team == team_name:
            return dict[team_away]
        
def team_colors(team_name):
    team = get_team(team_name)
    return team["colors"]

def team_names():
    dict = game_dict()
    home = dict['home']['team_name']
    away = dict['away']['team_name']
    return [home, away]



def player_numbers(team_name):
    team = get_team(team_name)
    return [player.get("number") for player in team["players"]]
    
team_colors("Cleveland Cavaliers")
print(team_names())
player_numbers("Cleveland Cavaliers")

def player_stats(player_name):
    dict = game_dict()
    for team in dict:
        player = [player for player in dict[team]["players"] if player.get("name") == player_name]
        if player != []:
            return player[0]
        
def get_players_by_shoe_brand(shoe_brand):
    dict = game_dict()
    for team in dict:
        return [player for player in dict[team]["players"] if player.get("shoe_brand") == shoe_brand]
    
print(player_stats("Jarrett Allen"))


get_players_by_shoe_brand("Nike")


# i just re-read the instructions....
# its not quite what were were doing
# they want us to build dict, with key for each brand and value of list with each players stats
# then calculate and print average for each brand but summing all stats in each list, divided by length
# we can iterate therough brands and call this function for each, but thats not really what they want us to do
# ACTUALLY, i just re-read again... and it says we can do however we'd like, they were just recommending as possible
def print_average_rebounds_by_shoe_brand(shoe_brand):
    players = get_players_by_shoe_brand(shoe_brand)
    rebounds_var = 0
    for player in players:
        rebounds = player.get("rebounds_per_game")
        rebounds_var += rebounds
    players_length = len(players)
    rebounds_avg = rebounds_var / players_length
    print(f"{shoe_brand}: {rebounds_avg:.2f}")

print_average_rebounds_by_shoe_brand("Nike")




"""
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
"""
print("********************************************")

# importing functools for reduce()
import functools

def average_rebounds_by_shoe_brand():
    stats = {}
    dict = game_dict()
    for team_away in dict:
        for player in dict[team_away]["players"]:
            brand = player.get("shoe_brand")
            rebounds = player.get("rebounds_per_game")

            data = stats.get(brand)
            if data:
                data.append(rebounds)
            else:
                data = [rebounds]
            stats[brand] = data
    #print(stats)

    # generate averages for stats
    for brand,data in stats.items():
        sum = functools.reduce(lambda a, b: a+b, data)
        average = sum / len(data)
        print(f"{brand}:  {average:.2f}")

average_rebounds_by_shoe_brand()