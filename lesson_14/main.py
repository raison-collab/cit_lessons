import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('2D Plaformer')

# загрузка персонажа и монетки
character = pygame.image.load('img/personage1.png')
coin = pygame.image.load('img/coin1.png')
background = pygame.image.load('img/back1.jpg')

# настройка начальных координат
x = 400
y = 300
vx = 0
vy = 0
direction = 'right'

# координаты монет
coins = [(100, 200), (300, 400), (500, 300), (700, 100)]

# счет
score = 0

# контроль частоты кадров
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)

    events = pygame.event.get()

    # работа с событиями
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vx = -5
                direction = 'left'

            if event.key == pygame.K_RIGHT:
                vx = 5
                direction = 'right'

            if event.key == pygame.K_UP:
                vy = -10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                vx = 0

    # обновление координат с учетом скорости и гравитации
    x += vx
    y += vy
    vy += 1

    # ограничения на выход за границы карты
    if x < 0:
        x = 0
    if x > 800:
        x = 600
    if y < 0:
        y = 20
    if y > 600:
        y = 550

    screen.blit(background, (0, 0))

    # отобразил персонажа
    if direction == 'right':
        screen.blit(character, (x, y))
    else:
        flipped = pygame.transform.flip(character, True, False)
        screen.blit(flipped, (x, y))

    # отобразил монеты
    for coord in coins:
        screen.blit(coin, (coord[0], coord[1]))

    for i, (cx, cy) in enumerate(coins):
        if ((x + 25) - (cx + 25)) ** 2 + ((y + 25) - (cy + 25)) ** 2 < 50 ** 2:
            score += 1
            del coins[i]

    font = pygame.font.SysFont('Arial', 32)
    text = font.render(f"Счет {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # обновление экрана
    pygame.display.flip()

    # если монеты кончились, то закрываем игру
    if len(coins) == 0:
        running = False
        time.sleep(200)
