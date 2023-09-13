import re
from utils.constants import COMMAND_ARGUMENTS

class CommandParser():
  def __init__(self):
    self.expressions = [
      '^(?:using|with|wielding)[\w ]* (\w+) (\w+)[\w ]* (\w+)', #to account for poorly worded commands!
      '^(\w+)[the ]* (\w+) (?:using|with|wielding)[\w ]* (\w+) and[\w ]* (\w+)$',
      '^(\w+)[the ]* (\w+) (?:using|with|wielding)[\w ]* (\w+)$',
      '^(\w+|pick up)[the ]* (\w+)$',
      '^(go|walk|move|visit) (?:(back|to|the|towards|in the direction of| )*)(\w+)$',
      '^(\w+)$'
    ]        

  def find_first_match(self, input):
    """
    Method to retrieve the matching text from a user's input command.
    """

    for expression in self.expressions:
        matches = re.search(expression, input)
        if matches:
            return [group for group in matches.groups() if group and group.strip() != '']
        
  def get_command_and_arguments_from_input(self, user_input):
    """
    Method to retrieve the command from the matched text, from the user's input.
    input argument is a string.
    """
    user_input = user_input.lower()

    command = ''
    arguments = {}
    matches = self.find_first_match(user_input) #this is a list
    print (matches)
    if len(matches) > 0:
      for word in matches:
        if word in COMMAND_ARGUMENTS.keys():
          command = word
          break
          
      if COMMAND_ARGUMENTS[command] == 1:
        arguments['target'] = matches[-1]

      elif COMMAND_ARGUMENTS[command] == 2:
        arguments['target'] = matches[1]
        arguments['weapons'] = matches[2:]
        
      return [command, arguments]
        