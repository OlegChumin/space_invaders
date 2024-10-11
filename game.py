import math
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

# Счет игры
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10


# Игрок
player_image = pygame.image.load('player.png').convert_alpha()
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

# Снаряд
bullet_img = pygame.image.load('bullet.png').convert_alpha()
bullet_x = 0
bullet_y = player_y
bullet_y_change = 5  # Скорость движения снаряда
bullet_state = "ready"  # снаряд не виден "fire" - снаряд в движении

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

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(player_image, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


# TODO закончить функцию столкновений
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    if distance < 27:
        return True
    else:
        return False


# Основной цикл игры
running = True
while running:

    # Заливка экрана
    screen.fill(background_color)

    show_score(text_x, text_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # События нажатие клавиш влево вправо <- a ... d ->
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x  # снаряд/пуля вылетает с позиции игрока
                bullet_y = player_y
                fire_bullet(bullet_x, bullet_y)

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

    # Движение снаряда
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"

    # Движение противников
    # for i in range(len(enemy_x)):
    for i in range(len(enemy_x) -1, -1, -1):
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

        # проверка столкновения
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = player_y # сбрасываем снаряд
            bullet_state = "ready"
            # enemy_x[i] = random.randint(0, 936)
            # enemy_y[i] = random.randint(50, 150)
            score_value += 1
            del enemy_x[i]
            del enemy_y[i]
            del enemy_x_change[i]
            del enemy_y_change[i]
            del enemy_img[i]

        # Отображение врагов на экране
        if i < len(enemy_x):
            enemy(enemy_x[i], enemy_y[i], i)

    # Отображение игрока на экране
    player(player_x, player_y)

    # Обновление экрана
    pygame.display.update()
