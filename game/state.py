"""
state of game
"""
from abc import abstractmethod
from game.spirites.paddle import NormalPaddle
from game.utils.constans import GAME_BACKGROUND, WIDTH, HEIGHT
from game.utils.utility import draw_text


class GameState:
    """
    abstract class represent state of game
    """

    def __init__(self, game):
        """
        :param game:
        """
        self.game = game

    @abstractmethod
    def apply(self):
        """
        do some stuff depending on state
        :return:
        """


class InitializeState(GameState):
    """
    class represent state before game starts
    create and add collisions between sprites
    """

    def __init__(self, game):
        super().__init__(game)

        self._add_sprites()
        self._add_ball_collide_sprites()
        self.game.back_to_start()

    def _add_sprites(self):
        """
        add all sprite to draw on screen
        :return:
        """
        self.game.all_spirits.empty()
        self.game.all_spirits.add(self.game.paddle)
        self.game.all_spirits.add(self.game.ball)
        self.game.all_spirits.add(self.game.level.bricks)

    def _add_ball_collide_sprites(self):
        """
        add all ball collision
        :return:
        """
        self.game.ball.remove_all_collide_sprites()
        self.game.ball.add_paddle_spirit(self.game.paddle)
        self.game.ball.add_brick_sprites(self.game.level.bricks, on_collide=self.game.brick_collide)

    def apply(self):
        self.game.state = ScoreState(self.game)


class ScoreState(GameState):
    """
    class represent state when player can get the point
    """

    def apply(self):
        self.game.screen.fill(GAME_BACKGROUND)
        self.game.all_spirits.update()
        self.game.all_spirits.draw(self.game.screen)
        draw_text(self.game.screen, str(self.game.score), WIDTH - 50, 20)

        if self.game.level.complete:
            self.game.state = LoadNextLevelState(self.game)

        if self.game.ball.rect.y > HEIGHT:
            self.game.state = LoseLifeState(self.game)


class LoseLifeState(GameState):
    """
    class represent state when ball is off screen
    """

    def __init__(self, game):
        super().__init__(game)
        self.game.life -= 1
        self.game.back_to_start()

    def apply(self):
        if self.game.life > 0:
            self.game.state = ScoreState(self.game)
            self.game.paddle.state.turn_off()
            self.game.paddle.state = NormalPaddle(self.game)
        else:
            self.game.state = GameOverState(self.game)


class LoadNextLevelState(GameState):
    """
    class represent state when player complete level
    """

    def apply(self):
        if self.game.level.next_level is not None:
            self.game.level = self.game.level.next_level()
            self.game.paddle.state.turn_off()
            self.game.paddle.state = NormalPaddle(self.game)
            self.game.state = InitializeState(self.game)
        else:
            self.game.state = GameOverState(self.game)


class GameOverState(GameState):
    """
    class represent state when player end all levels
    """

    def apply(self):
        draw_text(self.game.screen, str(self.game.score), WIDTH/2, HEIGHT/2, 50)
