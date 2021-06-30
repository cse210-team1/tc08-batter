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
        score = cast["score"][0] # there's only one
        self._check_bricks(bricks, ball, score, cast)
        self._check_walls(ball, cast)
        self._check_paddle(paddle, ball)
                
    def _check_bricks(self, bricks, ball, score, cast):
        for brick in bricks:
            if brick.get_color() == constants.HIT_COLOR:
                bricks.remove(brick)
            if ball.get_position().add(ball.get_velocity()).equals(brick.get_position()):
                self._bounce(ball,"y")
                brick.set_color(constants.HIT_COLOR)
                score.add_points(10)
            if len(bricks) == 0:
                game_over(cast,game_state='win')

    def _bounce(self, ball, direction):
        """ Tells the ball what to do when it hits an object
        
        Args: 
            ball (Actor): the ball that needs to bounce
            direction (String): x or y, what direction is the bounce occuring"""
        velocity = ball.get_velocity()
        pos_varient = random.randint(0,1)
        neg_varient = random.randint(-1,0)
        x = velocity.get_x() 
        y = velocity.get_y()
        
        if direction == "x":
            # Creating variance in y inversion creates too many problems
            x *= -1     
        elif direction == "y":
            if random.randint(0,1) == 1:
                if abs(x) >= 2:
                    x = x + 1 if x < 0 else x - 1
                else:
                    x = x - 1 if x < 0 else x + 1
            y *= -1 
        ball.set_velocity(Point(x,y))


    def _check_walls(self, ball, cast):
        x = ball.get_position().add(ball.get_velocity()).get_x()
        y = ball.get_position().get_y()
        if (x <= 1) or (x >= constants.MAX_X):
            self._bounce(ball,"x")
        if (y <= 0):
            self._bounce(ball,"y")
        if (y >= constants.MAX_Y):
            self.game_over(cast)
            
    def _check_paddle(self,paddle, ball):
        ball_position = ball.get_position().add(ball.get_velocity())
        bat_y = paddle.get_position().get_y()
        bat_x = paddle.get_position().get_x()
        if paddle.get_color() == constants.PADDLE_HIT:
            paddle.set_color(7)
        for i in range(len(paddle.get_text())):
            x = bat_x + i
            if ball_position.equals(Point(x,bat_y)):
                paddle.set_color(constants.PADDLE_HIT)
                self._bounce(ball,"y")
                
    def game_over(self, cast, game_state=""):
        for tag in cast:
            for actor in cast[tag]:
                if actor.get_description() == "score keeper":
                    pass
                else:
                    actor.set_text("")
        banner = cast["banner"][0] # There is only one
        score = cast["score"][0]
        if game_state == "win":
            banner.set_text("YOU WIN!")
        else:
            banner.set_text("GAME OVER")
        x = round(constants.MAX_X/2)
        y = round(constants.MAX_Y/2) + 1
        score.set_position(Point(x,y))
            

        
        
    
        