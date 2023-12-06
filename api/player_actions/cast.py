from player_actions.action import Action
from random import choice

class Cast(Action):
  """
    Static class so does not require __init__ or any attributes to be passed in.
  """
  
  def can_act(game, target, spell):
      """
      Function to check whether the player has any equipment (weapons etc.) that 
      can be used to attack a target, and whether the target is in the same
      location, to be attacked.
      
      """
        
      #TODO: Decide the mechanics for casting spells (e.g. knowing scrolls, spells, etc. and how this 
      # interplays with the player's mana attribute)

      pass 