from classes.game_response import GameResponse
from constants import DIRECTION_NAMES, N, S, E, W
from player_actions.attack import Attack

def run_command(game, command, arguments):
  if command == 'attack':
    
    target, weapons = Attack.parse(game, arguments)

    result = Attack.can_act(game, target, weapons)
    if result.valid:
       message = Attack.act(game, target, weapons)
    else:
      message = result.message
      return GameResponse(game.player.id, message, None)
  elif command == 'cast':
    return cast(game, arguments)
  elif command == 'drop':
    return drop(game, arguments)
  elif command == 'equip':
    return equip(game, arguments)
  elif command == 'go':
    return go(game, arguments)
  elif command == 'help':
     return help()
  elif command == 'inventory':
     return inventory(game)
  elif command == 'investigate':
     return investigate(game, arguments)
  elif command == 'load':
     return load(game)
  elif command == 'look':
     return look(game)
  elif command == 'quit':
     return quit(game)
  elif command == 'save':
     return save(game)
  elif command == 'take':
     return take(game, arguments)
  elif command == 'unequip':
     return unequip(game, arguments)
  elif command == 'use':
     return use(game, arguments)

def cast(game, spell):
    pass

def drop(game, item):
    pass

def equip(game, item):
    pass

def go(game, arguments):
  direction_name = arguments['direction']
  direction = DIRECTION_NAMES[direction_name]
  
  if direction not in game.player.location.exits:
    return GameResponse(game.player.id, 'You cannot go that way.', None)

  current_location = game.player.location
  x_locations = [location for location in game.locations if location.x == current_location.x]
  y_locations = [location for location in game.locations if location.y == current_location.y]
  new_location = None

  if direction == N:
    x_locations.sort(key=lambda location: location.y, reverse=True)
    new_location = [location for location in x_locations if location.y < current_location.y][0]
    
  elif direction == S:
    x_locations.sort(key=lambda location: location.y, reverse=False)
    new_location = [location for location in x_locations if location.y > current_location.y][0]
  
  elif direction == E:
    y_locations.sort(key=lambda location: location.x, reverse=False)
    new_location = [location for location in y_locations if location.x > current_location.x][0]
  
  elif direction == W:
    y_locations.sort(key=lambda location: location.x, reverse=True)
    new_location = [location for location in y_locations if location.x < current_location.x][0]

  new_location.spawn_creatures(game)

  game.player.location = new_location
  
  return GameResponse(game.player.id, game.player.location.location_summary(game.time_of_day), None)

def help():
    #list commands
    pass

def inventory(game):
    pass

def investigate(game, arguments):
   location_item_ids = game.player.location.items
   list_of_items = [item for item in game.items if item.id in location_item_ids]
   item_being_investigated = [item for item in list_of_items if item.name.lower() == arguments['item'].lower()][0]
   return GameResponse(game.player.id, str(item_being_investigated.investigation(game.items)), game.player.location.id)

def load(game):
    pass

def look(game):
   location_item_ids = game.player.location.items
   list_of_items = [item for item in game.items if item.id in location_item_ids]
   return GameResponse(game.player.id, game.player.location.observations_and_items(list_of_items), game.player.location.id)

def quit(game):
    pass

def save(game):
    pass

def take(game, item):
    pass

def unequip(game, item):
    pass

def use(game, item):
    pass
