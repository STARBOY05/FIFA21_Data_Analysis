def getPlayer(data, playerName):
    return data[data['PlayerName'] == playerName].reset_index()

def getPlayerAttribute(data, playerName, playerAttr):
    playerData = data[data['PlayerName'] == playerName]
    return playerData[playerAttr]

def getNationalityFlag(data, nation):
    for key, value in data.items():
        if(nation == value):
            return key

    