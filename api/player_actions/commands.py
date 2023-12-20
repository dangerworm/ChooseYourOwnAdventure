from classes.game_response import GameResponse
from player_actions.attack import Attack
from player_actions.drop import Drop
from player_actions.investigate import Investigate
from player_actions.navigate import Navigate
from player_actions.take import Take

def run_command(game, command, arguments):
  if command == 'attack':
     target, weapons = Attack.parse(game, arguments)
     valid, message, is_creature = Attack.can_act(game, target, weapons)
     if valid:
       thing_hit, is_dead, message = Attack.act(game, target, is_creature, weapons)

      # Allow creature to attack back
     if is_creature and not is_dead:
       target = 'game_player'
       weapons = thing_hit.choose_weapons()
       thing_hit, is_dead, additional_message = Attack.act(game, target, is_creature, weapons)
       message += '\n' + additional_message

     return GameResponse(game.player.id, message, None)
  
  elif command == 'cast':
     return cast(game, arguments)
  
  elif command == 'drop':
   item_name, _ = Drop.parse(game, arguments)
   valid, message = Drop.can_act(game, item_name)
   if valid:
      message = Drop.act(game, item_name)

   return GameResponse(game.player.id, message, game.player.location.id)

  elif command == 'equip':
     return equip(game, arguments)
  
  elif command in ['go', 'walk', 'move', 'visit']:
     target, _ = Navigate.parse(game, arguments)
     valid, message = Navigate.can_act(game, target)

     if valid:
       message = Navigate.act(game, target)
      
     return GameResponse(game.player.id, message, game.player.location.id)
    
  elif command == 'help':
     return help()
  elif command == 'inventory':
     return inventory(game)
  elif command == 'investigate':
     target, _ = Investigate.parse(game, arguments)
     valid, message = Investigate.can_act(game, target)
    
     if valid:
       message = Investigate.act(game, target)
      
     return GameResponse(game.player.id, message, game.player.location.id)

  elif command == 'load':
     return load(game)
  elif command == 'look':
     return look(game)
  elif command == 'quit':
     return quit(game)
  elif command == 'save':
     return save(game)
  elif command == 'take' or command == 'pick up':
    item_name, _ = Take.parse(game, arguments)
    valid, message = Take.can_act(game, item_name)
    if valid:
       message = Take.act(game, item_name)

    return GameResponse(game.player.id, message, None)

  elif command == 'unequip':
     return unequip(game, arguments)
  elif command == 'use':
     return use(game, arguments)
  
def cast(game, spell):

    pass


def equip(game, item):
    pass

def help():
    #list commands
    pass

def inventory(game):
    return GameResponse(game.player.id, game.player.check_player_inventory(),None)

def load(game):
    pass

def look(game):
   return GameResponse(game.player.id, game.player.location.observations_and_items(), game.player.location.id)

def quit(game):
    pass

def save(game):
    pass

def unequip(game, item):
    pass

def use(game, item):
    pass
