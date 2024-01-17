from player_actions.action import Action

class Unequip(Action):
    """
      Static class so does not require __init__ or any attributes to be passed in.
    """
    def can_act(game, target_item):
      """
      Function to check whether the player has any equipment (weapons etc.) equipped that 
      can be unequipped.
      """

      valid = True
      message = ''

      if target_item == None:
        valid = False
        message = 'You did not specify an item to unequip.'
        return valid, message
      
      equipped_items = [item.name.lower() for item in game.player.equipped]

      if target_item not in equipped_items:
        valid = False
        message = f'You do not have that item ({target_item}) equipped.'
        return valid, message
      
      return valid, message
    
    def act(game, target_item):
      """
      Function to unequip a target item.
       1. take in command "unequip the sword"
       2. logic check do we have that item equipped?
       3. if we have the item equipped, unequip and update player.equipped list and return to inventory
       4. if we dont have item equipped, adivse player we cant unequip the item as we do not have it equipped. 
      """

      items_to_unequip = [item for item in game.player.equipped if item.name.lower()
                           == target_item.lower()]
      
      thing_to_unequip = items_to_unequip[0]

      #unequip the item
      game.player.equipped.remove(thing_to_unequip)

      #update the inventory with the now unequipped item
      game.player.items.append(thing_to_unequip)

      message = f"You have unequipped the {target_item}"
      
      return message
