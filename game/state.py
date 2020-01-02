from abc import abstractmethod
from game.utils.constans import *


class GameState(object):

    def __init__(self, game):
        self.game = game

    @abstractmethod
    def apply(self):
        pass


class InitializeState(GameState):

    def __init__(self, game):
        super().__init__(game)

        self._add_sprites()
        self._add_ball_collide_sprites()
        self.game.create_listeners()

    def _add_sprites(self):
        self.game.all_spirits.empty()
        self.game.all_spirits.add(self.game.paddle)
        self.game.all_spirits.add(self.game.ball)
        self.game.all_spirits.add(self.game.bricks)

    def _add_ball_collide_sprites(self):
        self.game.ball.remove_all_collide_sprites()
        self.game.ball.add_collide_sprites(self.game.paddle, True)
        self.game.ball.add_collide_sprites(self.game.bricks)

    def apply(self):
        self.game.state = ScoreState(self.game)


class ScoreState(GameState):

    def __init__(self, game):
        super().__init__(game)

    def apply(self):
        self.game.screen.fill(GAME_BACKGROUND)
        self.game.all_spirits.update()
        self.game.all_spirits.draw(self.game.screen)

        if self.game.level.complete:
            self.game.state = LoadNextLevelState(self.game)

        if self.game.ball.rect.y > HEIGHT:
            self.game.state = LoseLifeState(self.game)


class LoseLifeState(GameState):

    def __init__(self, game):
        super().__init__(game)
        self.game.life -= 1
        self.game.ball.moving = False

    def apply(self):
        if self.game.life > 0:
            self.game.ball.rect.x = self.game.paddle.rect.x + 45
            self.game.ball.rect.y = 540
            self.game.state = ScoreState(self.game)
        else:
            self.game.state = GameOverState(self.game)


class LoadNextLevelState(GameState):

    def __init__(self, game):
        super().__init__(game)

    def apply(self):
        pass


class GameOverState(GameState):

    def __init__(self, game):
        super().__init__(game)

    def apply(self):
        pass
