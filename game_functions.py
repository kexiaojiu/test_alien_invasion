#coding=utf-8
import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_key_down_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        #向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #创建一个子弹，并将子弹加入到编组bullets中
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        #按键q退出游戏
        sys.exit()

def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        #停止移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        #停止移动飞船
        ship.moving_left = False
    


def check_events(ai_settings, screen, ship, bullets):
    """监视键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, aliens):
    """更新屏幕的图像，并切换到新屏幕"""    
    # 每次循环时候都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()        
    ship.blitme()
    aliens.draw(screen)
    #~ for alien in aliens.sprites():
        #~ alien.blitme()
                
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹位置，删除已经消失的子弹"""
    # 更新子弹位置
    bullets.update()
    
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没有超过子弹数上限，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        # 创建一个子弹，并将子弹加入到编组bullets中
        net_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(net_bullet)


def create_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    # 创建一个外星人并计算一行可以容纳多少外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    
    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
        # 创建一个外星人并把它加入当前行
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
