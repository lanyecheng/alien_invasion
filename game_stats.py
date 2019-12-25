#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/12/21

class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = False
        self.reset_stats()
        self.open_file_higt()

    def reset_stats(self):
        """初始化在游戏运作期间可能变化的统计信息"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def open_file_higt(self):
        with open(self.ai_settings.score_name) as file_object:
            for line in file_object:
                self.high_score = int(line)