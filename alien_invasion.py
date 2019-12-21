#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/12/21

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 开始游戏的主循环
    while True:
        # 检查键盘
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船位置
        ship.update()
        # 更新子弹位置
        gf.update_bullets(bullets)
        gf.create_fleet(ai_settings, screen, ship, aliens)
        # 使用更新后的位置绘制屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
