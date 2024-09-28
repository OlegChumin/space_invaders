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
icon = pygame.image.load('space_invaders_icon.png')
pygame.display.set_icon(icon)

# Фон
background_color = (0, 0, 0);
# TODO background = pygame.image.load('background.png')

# Игрок
player_image = pygame.image.load('player.png')
player_x = 370
player_y = 550
player_x_change = 0

# Противник
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 12

# Размещение врагов в ряды и с уникальными скоростями
for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0, 775))  # Случайное положение по X
    enemy_y.append(random.randint(50, 200))  # Более равномерное распределение по Y
    enemy_x_change.append(0.3 + random.random() * 0.2)  # Немного разные скорости для каждого
    enemy_y_change.append(30)


def player(x, y):
    screen.blit(player_image, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


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
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1

        # Отпускание клавиш
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player_x_change = 0

    # Изменение координат игрока
    player_x += player_x_change

    # TODO границы экрана для игрока надо выровнять
    if player_x <= 15:
        player_x = 15
    elif player_x >= 775:
        player_x = 775

    # Движение противника
    for i in range(num_of_enemies):

        enemy_x[i] += enemy_x_change[i]

        # Если враг достиг края экрана, меняем направление и опускаем вниз
        if enemy_x[i] <= 0:
            enemy_x_change[i] = abs(enemy_x_change[i])  # Двигается вправо
            enemy_y[i] += enemy_y_change[i]  # Спускается на одну линию вниз
        elif enemy_x[i] >= 775:
            enemy_x_change[i] = -abs(enemy_x_change[i])  # Двигается влево
            enemy_y[i] += enemy_y_change[i]  # Спускается на одну линию вниз

        # Отображение врагов на экране
        enemy(enemy_x[i], enemy_y[i], i)

    # Отображение игрока на экране
    player(player_x, player_y)

    # Обновлением экрана
    pygame.display.update()
