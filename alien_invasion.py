#coding=utf-8
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    """设置背景颜色"""
    bg_color = (230,230,230)
    
    """创建一只飞船"""
    ship = Ship(screen)
    
    """开始游戏的主循环"""
    while True:
        # 监视键盘和鼠标事件
        gf.check_events()
        
        # 更新屏幕的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, ship)

run_game()
