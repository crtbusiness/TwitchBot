import srcomapi

#Cache game ID for ease of access
api = srcomapi.SpeedrunCom(); api.debug = 1
game = api.search(srcomapi.datatypes.Game, {"name": "Popeye 2021"})[0]
gameID = "o6gnr591"
assert(game.name == "Popeye 2021")

def getWorldRecord():
    #get world record
    record = game.categories[0].records[0]
    assert(isinstance(record.runs[0]["run"], srcomapi.datatypes.Run))
    return(record)