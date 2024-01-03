from classes.game_response import GameResponse
from player_actions.attack import Attack
from player_actions.drop import Drop
from player_actions.equip import Equip
from player_actions.investigate import Investigate
from player_actions.navigate import Navigate
from player_actions.take import Take

def run_command(game, command, arguments):
  if command == 'attack': #done
     return attack(game, arguments)
  
  elif command == 'cast':
     return cast(game, arguments)
  
  elif command == 'drop': #done
     return drop(game, arguments)

  elif command == 'equip': #drop
     return equip(game, arguments)
  
  elif command in ['go', 'walk', 'move', 'visit']:
     return navigate(game, arguments)
    
  elif command == 'help':
     return help()
  
  elif command == 'inventory': #done
     return inventory(game)
  
  elif command == 'investigate': #done
     return investigate(game, arguments)

  elif command == 'load':
     return load(game)
     
  elif command == 'look': #done
     return look(game)
  
  elif command == 'quit':
     return quit(game)
  
  elif command == 'save':
     return save(game)
  
  elif command == 'take' or command == 'pick up': #done
    return take(game, arguments)

  elif command == 'unequip': 
     return unequip(game, arguments)
  
  elif command == 'use':
     return use(game, arguments)

#-----------------------
#   Command Functions
#-----------------------
def attack(game, arguments):
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

def cast(game, arguments):
    pass

def drop(game, arguments):
   item_name, _ = Drop.parse(game, arguments)
   valid, message = Drop.can_act(game, item_name)
   if valid:
      message = Drop.act(game, item_name)

   return GameResponse(game.player.id, message, game.player.location.id)

def equip(game, arguments):
   target_item, _ = Equip.parse(game, arguments)
   valid, message = Equip.can_act(game, target_item)
   if valid:
      message = Equip.act(game, target_item)
   return GameResponse(game.player.id, message, game.player.location.id)

def help():
    #list commands
    pass

def inventory(game):
    return GameResponse(game.player.id, game.player.check_player_inventory(),None)

def investigate(game, arguments):
   target, _ = Investigate.parse(game, arguments)
   valid, message = Investigate.can_act(game, target)
   
   if valid:
      message = Investigate.act(game, target)
   
   return GameResponse(game.player.id, message, game.player.location.id)

def load(game):
    pass

def look(game):
   return GameResponse(game.player.id, game.player.location.observations_and_items(), game.player.location.id)

def navigate(game, arguments):
   target, _ = Navigate.parse(game, arguments)
   valid, message = Navigate.can_act(game, target)

   if valid:
      message = Navigate.act(game, target)
   
   return GameResponse(game.player.id, message, game.player.location.id)

def quit(game):
    pass

def save(game):
    pass

def take(game, arguments):
   item_name, _ = Take.parse(game, arguments)
   valid, message = Take.can_act(game, item_name)
   if valid:
      message = Take.act(game, item_name)

   return GameResponse(game.player.id, message, None)

def unequip(game, item):
    pass

def use(game, item):
    pass
