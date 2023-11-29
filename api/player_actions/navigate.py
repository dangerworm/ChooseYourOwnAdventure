from utils.constants import DIRECTIONS, DIRECTION_INDICES, N, E, S, W
from player_actions.action import Action

class Navigate(Action):
    """
    Static class so does not require __init__ or any attributes to be passed in.
    """

    def can_act(game, target):
        """
        Function to check whether the player can move in the selected direction.
        """
        
        destinations = [DIRECTIONS[exit] for exit in game.player.location.exits]

        valid = True
        message = ''

        new_locations = Navigate.get_new_locations_in_target_direction(game, target)

        if target not in destinations:
            valid = False
            message = f'You cannot go that way.'

        elif target == None:
            valid = False
            message = 'You did not specify a direction in which to travel.'

        elif len(new_locations) == 0:
             valid = False
             message = 'That location does not exist'

        return valid, message
        

    def act (game, target):
        """
        Function to move in a chosen direction 
        """

        new_location = Navigate.get_new_locations_in_target_direction(game, target)[0]
        new_location.spawn_creatures(game)

        game.player.location = new_location
        
        return game.player.location.location_summary(game.time_of_day)

    def get_new_locations_in_target_direction(game, target):
      """
      Function to find the location in the target direction 
      """
       
      direction_index = DIRECTION_INDICES[target]
      current_location = game.player.location
      x_locations = [location for location in game.locations.values() if location.x == current_location.x]
      y_locations = [location for location in game.locations.values() if location.y == current_location.y]
    
      if direction_index == N:
        x_locations.sort(key=lambda location: location.y, reverse=True)
        return [location for location in x_locations if location.y < current_location.y]
        
      elif direction_index == S:
        x_locations.sort(key=lambda location: location.y, reverse=False)
        return [location for location in x_locations if location.y > current_location.y]
      
      elif direction_index == E:
        y_locations.sort(key=lambda location: location.x, reverse=False)
        return [location for location in y_locations if location.x > current_location.x]
      
      elif direction_index == W:
        y_locations.sort(key=lambda location: location.x, reverse=True)
        return [location for location in y_locations if location.x < current_location.x]
