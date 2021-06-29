import random
from game import constants
from game.action import Action
from game.point import Point
import sys

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        self._check_bricks(bricks, ball)
        self._check_walls(ball)
        self._check_paddle(paddle, ball)
                
    def _check_bricks(self, bricks, ball):
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                self._bounce(ball,"y")
                bricks.remove(brick)
    

    def _bounce(self, ball, direction):
        """ Tells the ball what to do when it hits an object
        
        Args: 
            ball (Actor): the ball that needs to bounce
            direction (String): x or y, what direction is the bounce occuring"""
        velocity = ball.get_velocity()
        x = velocity.get_x()
        y = velocity.get_y()
        
        if direction == "x":
            x *= -1
        elif direction == "y":
            y *= -1
        ball.set_velocity(Point(x,y))


    def _check_walls(self, ball):
        x = ball.get_position().get_x()
        y = ball.get_position().get_y()
        if (x == 1) or (x == constants.MAX_X):
            self._bounce(ball,"x")
        if (y == 0):
            self._bounce(ball,"y")
        if (y == constants.MAX_Y):
            sys.exit()
            
    def _check_paddle(self,paddle, ball):
        ball_position = ball.get_position()
        bat_y = paddle.get_position().get_y()
        bat_x = paddle.get_position().get_x()
        for i in range(len(paddle.get_text())):
            x = bat_x + i
            if ball_position.equals(Point(x,bat_y)):
                self._bounce(ball,"y")
        
        
    
        