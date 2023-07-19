cricket_players=[{"name":"Virat kohli","no_of_centuries":75,"half_centuries":180,"wickets_taken":4,"hat_trick_wicket":1,"top_batting_score":183},
    {"name":"Maxwell","no_of_centuries":3,"half_centuries":63,"wickets_taken":4,"hat_trick_wicket":55,"top_batting_score":145},
    {"name":"Afridi","no_of_centuries":11,"half_centuries":45,"wickets_taken":395,"hat_trick_wicket":3,"top_batting_score":124},
    {"name":"dwayne bravo","no_of_centuries":2,"half_centuries":26,"wickets_taken":199,"hat_trick_wicket":0,"top_batting_score":112},
    {"name":"faf du plessis","no_of_centuries":21,"half_centuries":100,"wickets_taken":60,"hat_trick_wicket":10,"top_batting_score":199}]
for player in cricket_players:
    if player['no_of_centuries']>10:
        print(player['name'])
for player in cricket_players:
    if player['hat_trick_wicket']>5:
        print(player['name'])
for player in cricket_players:
    max=player['top_batting_score']
print(max)
