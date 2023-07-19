cricket_players=[{"name":"Virat kohli","no_of_centuries":75,"half_centuries":180,"wickets_taken":4,"hat_trick_wicket":1,"top_batting_scores":[183,78,178,245,111]},
    {"name":"Maxwell","no_of_centuries":3,"half_centuries":63,"wickets_taken":4,"hat_trick_wicket":55,"top_batting_scores":[145,256,167,254,222]},
    {"name":"Afridi","no_of_centuries":11,"half_centuries":45,"wickets_taken":395,"hat_trick_wicket":3,"top_batting_scores":[124,356,123,456,324]},
    {"name":"dwayne bravo","no_of_centuries":2,"half_centuries":26,"wickets_taken":199,"hat_trick_wicket":0,"top_batting_scores":[112,212,333,465,435]},
    {"name":"faf du plessis","no_of_centuries":21,"half_centuries":100,"wickets_taken":60,"hat_trick_wicket":10,"top_batting_scores":[199,387,476,398,176]}]
count=0
higher_hat_trick=[]
for player in cricket_players:
    if player['no_of_centuries']>10:
        count+=1
    if player['hat_trick_wicket']>5:
        higher_hat_trick.append(player['name'])
print(count)
print(higher_hat_trick)
for player in cricket_players:
    batting_scores=(player['top_batting_scores'])
    # print(batting_scores)
    top=player['top_batting_scores'][0]
    for batting_score in batting_scores:
        if batting_score>top:
            top=batting_score 
    print(top)
# result=higher_batting.append(top)
# print(result)
