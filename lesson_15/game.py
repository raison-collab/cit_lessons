import pygame
from characters import Character, Osel, Bird
from coins import Coin


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('2D Plaformer')

        self.character = self.get_character()
        self.coin = pygame.image.load('img/coin.png')
        self.background = pygame.image.load('img/back1.jpg')

        self.coins = [Coin(100, 200, pygame.image.load('img/coin.png')), Coin(700, 100, pygame.image.load('img/coin.png')), Coin(300, 400, pygame.image.load('img/coin.png')), Coin(500, 300, pygame.image.load('img/coin.png'))]

        # счет
        self.score = 0

        # контроль частоты кадров
        self.clock = pygame.time.Clock()

        self.running = True

    def get_character(self) -> Character:
        choose = int(input("Выберите персонажа:\n1)базовый\n2)осел\n>>>"))
        if choose == 1:
            return Character(400, 300, pygame.image.load('img/personage.png'))
        elif choose == 2:
            return Osel(150, 150, pygame.image.load('img/osel.png'))
        else:
            raise ValueError('Нет такого персонажа')

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.character.vx = -5
                    self.character.direction = 'left'

                if event.key == pygame.K_RIGHT:
                    self.character.vx = 5
                    self.character.direction = 'right'

                if event.key == pygame.K_UP:
                    self.character.vy = -10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.character.vx = 0

    # Обновление экрана
    def update_screen(self):
        self.character.update_coordinates()

        for i, coin in enumerate(self.coins):
            if coin.collid(self.character):
                self.score += 1
                del self.coins[i]

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.character.draw(self.screen)

        for coin in self.coins:
            coin.draw(self.screen)

        font = pygame.font.SysFont('Arial', 32)
        text = font.render(f"Счет {self.score}", True, (0, 0, 0))
        self.screen.blit(text, (10, 10))

        # обновление экрана
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(60)

            self.events()

            self.update_screen()

            self.draw()
