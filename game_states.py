class GameStates:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_states()

        # 在任何情况下都不应重置最高分
        self.high_score = 0

        self.level = 1

    def reset_states(self):
        """初始化在游戏运行期间可能发生变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0