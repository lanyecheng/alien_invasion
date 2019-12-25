#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/12/21

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    play_button = Button(screen, 'Play')

    # 创建一个用于存储游戏统计信息的实例、并创建计分牌，放在屏幕的右上角
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 检查键盘
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 更新飞船位置
            ship.update()
            # 更新子弹位置
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 更新外星人的位置
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        # 使用更新后的位置绘制屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
