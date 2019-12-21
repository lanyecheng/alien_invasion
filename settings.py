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
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1