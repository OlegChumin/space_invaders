import pygame
import random

from pygame import event

# Инициализация Pygame
pygame.init()

# Настройка экрана
screen = pygame.display.set_mode((1000, 800))

# Название и иконка
# TODO добавить иконку (Глеб сделает иконку)
pygame.display.set_caption("Space Invaders")

# Цвет фона
background_color = (0, 0, 0);

# Игрок
player_image = pygame.image.load('player.png')
player_x = 370
player_y = 450
player_x_change = 0


def player(x, y):
    screen.blit(player_image, (x, y))


# Игрок
running = True
while running:

    # Заливка экрана
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # События нажатие клавиш влево вправо <- a ... d ->
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5

        # Отпускание клавиш
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player_x_change = 0

    # Изменение координат игрока
    player_x += player_x_change

    # Границы экрана для игрока
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Отображение игрока на экране
    player(player_x, player_y)

    # Обновлением экрана
    pygame.display.update()
