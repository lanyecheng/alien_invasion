#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/12/21


class Settings:
    """存储游戏所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 1

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        self.score_name = 'score_high.txt'

        # 外星人设置
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        # 加快游戏节奏的速度
        self.speedup_scale = 1.2
        # 得分提高倍数
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # 飞船的速度
        self.ship_speed_factor = 1.5
        # 子弹速度
        self.bullet_speed_factor = 3
        # 外星人移动速度
        self.alien_speed_factor = 1
        # fleet_direction 为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        # 击落一个外星人记10分
        self.alien_points = 10

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)