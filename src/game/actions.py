from enum import Enum

class Actions(Enum):
    UP = 0
    DOWN = 1
    SPIT_FIRE = 2

    def validate_action(action_value: int):
        """
        Validates the given action. Raises exception if the action is invalid.

        Args:
            action_value (int): integer value for action.
        """
        try:
            action = Actions(action_value)
        except ValueError:
            raise Exception("Invalid Action specified")
