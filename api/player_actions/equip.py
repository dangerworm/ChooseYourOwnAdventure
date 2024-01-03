from player_actions.action import Action

class Equip(Action):
    """
      Static class so does not require __init__ or any attributes to be passed in.
    """
    def can_act(game, target_item):
      """
      Function to check whether the player has any equipment (weapons etc.) that 
      can be equipped, or if not, whether these are in the location the player 
        is in.
      """

      valid = True
      message = ''

      if target_item == None:
        valid = False
        message = 'You did not specify an item to equip.'
        return valid, message
      
      #TODO: It would be really nice to be able to equip creatures (for realism, shits and giggles, etc.)
      #HOWEVER:
      # If I pick up a spider and put it in my items, the logic here will lose track of the fact it is a creature
      # We could fix this by putting an is_creature flag on items, but that breaks all sorts of models and assumptions.
      #
      # There's also the rather dark and nasty question of whether putting a live fly into your items turns it into
      # a dead fly, because it will be crushed.
      # Or, if you put a live bird in your pack and 5 days go by without you taking it out and feeding/watering it,
      # does it become a dead bird? Or an angry bird? Or a weak bird? Or just lose HP according to the days it was there?
      
      item_names, _ = Action.get_nearby_items(game, target_item, includeCreatures = False)

      if target_item not in item_names:
        valid = False
        message = f'You do not have that item ({target_item}) to equip.'
        return valid, message
      
      return valid, message
    
    def act(game, target_item):
      """
      Function to equip a target item.
       1. take in command "equip the sword"
       2. logic check do we have that item in the inventory? or, if not, is it in the location we are at? if we dont have it and it is in the location we are in, pick up and equip it.
       3. if we have the item, equip item, update player.equipped list
         3a. if we took the item from the location remove it from the location and add to the inventory
       4. if we dont have item, adivse player we cant equip the item as we do not have it. 
      """

      possible_items_to_equip = []
      source = ''
      
      possible_items_to_equip += [item for item in game.player.items if item.name.lower()
                            == target_item.lower()]
      source = 'player.items'

      if len(possible_items_to_equip) == 0:
        possible_items_to_equip += [item for item in game.player.location.items if item.name.lower()
                              == target_item.lower()]
        source = 'player.location.items'
      
      #TODO: future development to go here: check whether you have the required 
      #number of hands free to hold the item you have specified!
      thing_to_equip = possible_items_to_equip[0]

      #equip the item
      game.player.equipped.append(thing_to_equip)

      #update the inventory / location to reflect the item being equipped now
      if source == 'player.items':
        game.player.items.remove(thing_to_equip)

      elif source == 'player.location.items':
        game.player.location.items.remove(thing_to_equip)

      message = f"You have equipped the {target_item}"
      
      return message
