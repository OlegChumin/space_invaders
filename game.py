import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройка экрана
screen = pygame.display.set_mode((1000, 800))

# Название и иконка
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space_invaders_new_icon.png')
pygame.display.set_icon(icon)

# Фон
background_color = (0, 0, 0)

# Игрок
player_image = pygame.image.load('top_down_spaceship_final.png').convert_alpha()
player_x = 500
player_y = 680
player_x_change = 0

# Противник
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 12

# Размещение врагов в рядах и с уникальными скоростями
rows = 3  # Количество рядов
cols = 4  # Количество колонок
enemy_width = 64  # Ширина спрайта противника
enemy_height = 64  # Высота спрайта противника
padding_x = 50  # Отступ между противниками по X
padding_y = 50  # Отступ между противниками по Y

# Создаем врагов в виде сетки (рядами)
for row in range(rows):
    for col in range(cols):
        enemy_img.append(pygame.image.load('enemy.png').convert_alpha())
        enemy_x.append(50 + col * (enemy_width + padding_x))  # Распределяем врагов по X
        enemy_y.append(50 + row * (enemy_height + padding_y))  # Распределяем врагов по Y
        enemy_x_change.append(0.05)  # Одинаковая скорость по X для всех врагов
        enemy_y_change.append(5)  # Когда враг достиг края, он двигается вниз на 30 пикселей

def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

# Основной цикл игры
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
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5

        # Отпускание клавиш
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Изменение координат игрока
    player_x += player_x_change

    # Границы экрана для игрока
    if player_x <= 15:
        player_x = 15
    elif player_x >= 875:
        player_x = 875

    # Движение противников
    for i in range(len(enemy_x)):
        enemy_x[i] += enemy_x_change[i]

        # Если враг достиг края экрана, меняем направление движения и опускаем вниз
        if enemy_x[i] <= 0:
            enemy_x_change[i] = abs(enemy_x_change[i])  # Двигается вправо
            for j in range(len(enemy_y)):
                enemy_y[j] += enemy_y_change[i]  # Все враги спускаются
        elif enemy_x[i] >= 936:  # Учитываем ширину экрана и спрайта
            enemy_x_change[i] = -abs(enemy_x_change[i])  # Двигается влево
            for j in range(len(enemy_y)):
                enemy_y[j] += enemy_y_change[i]  # Все враги спускаются

        # Отображение врагов на экране
        enemy(enemy_x[i], enemy_y[i], i)

    # Отображение игрока на экране
    player(player_x, player_y)

    # Обновление экрана
    pygame.display.update()
