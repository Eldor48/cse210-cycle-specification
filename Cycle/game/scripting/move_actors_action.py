import constants
from game.scripting.action import Action


class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()
            
        snake1 = cast.get_first_actor("snakes")
        snake2 = cast.get_second_actor("snakes")

        if script.get_actions("update")[1]._is_game_over:
            snake1.grow_tail(1, constants.WHITE)
            snake2.grow_tail(1, constants.WHITE)
            
        else: 
            snake1 = cast.get_first_actor("snakes")
            snake2 = cast.get_second_actor("snakes")
            
            snake1.grow_tail(1, constants.GREEN)
            snake2.grow_tail(1, constants.RED)