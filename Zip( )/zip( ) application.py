
def zip_application(players,scores):
    # printing players and scores.
    for pl, sc in zip(players, scores):
        print("Player :  %s     Score : %d" % (pl, sc))
# initializing their scores
scores = [100, 15, 17, 28, 43]
players = ["Sindu", "Saina Nehwal", "Usha", "Dravid", "Kiran"]
zip_application(players,scores)