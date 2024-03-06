def player_joined():
    return False


print("Searching for player...")
print("Press (x) to stop queue")
while player_joined() == False:
    pass
    if input("") == "x":
        break

if player_joined == True:
    print("Player Joined the match")
else:
    print("no player joined the match")

"""
World.start.battle([player1, player2], Enemies)
"""