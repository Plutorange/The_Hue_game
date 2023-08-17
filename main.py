import random
import time

import pygame


class GameInfo:
    pygame.init()
    pygame.display.set_caption('Gradient colors')
    size = 800, 800
    screen = pygame.display.set_mode(size)
    pixel_size = 80
    square_size = 800 // pixel_size
    pixels = []
    for i in range(square_size):
        pixels.append([])
        for j in range(square_size):
            pixels[i].append((71, 71, 71))


class Gradient:
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))]

    @staticmethod
    def create_new_image():
        GameInfo.pixel_size = 80
        GameInfo.square_size = 800 // GameInfo.pixel_size
        GameInfo.pixels = []
        for i in range(GameInfo.square_size):
            GameInfo.pixels.append([])
            for j in range(GameInfo.square_size):
                GameInfo.pixels[i].append((71, 71, 71))
        Gradient.colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                           (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                           (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                           (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))]
        for i in range(GameInfo.square_size):
            GameInfo.pixels[0][i] = (
                round(Gradient.colors[0][0] + (Gradient.colors[1][0] - Gradient.colors[0][0]) / (
                        GameInfo.square_size - 1) * i),
                round(Gradient.colors[0][1] + (Gradient.colors[1][1] - Gradient.colors[0][1]) / (
                        GameInfo.square_size - 1) * i),
                round(Gradient.colors[0][2] + (Gradient.colors[1][2] - Gradient.colors[0][2]) / (
                        GameInfo.square_size - 1) * i))
            GameInfo.pixels[GameInfo.square_size - 1][i] = (
                round(Gradient.colors[2][0] + (Gradient.colors[3][0] - Gradient.colors[2][0]) / (
                        GameInfo.square_size - 1) * i),
                round(Gradient.colors[2][1] + (Gradient.colors[3][1] - Gradient.colors[2][1]) / (
                        GameInfo.square_size - 1) * i),
                round(Gradient.colors[2][2] + (Gradient.colors[3][2] - Gradient.colors[2][2]) / (
                        GameInfo.square_size - 1) * i))
            GameInfo.pixels[i][0] = (
                round(Gradient.colors[0][0] + (Gradient.colors[2][0] - Gradient.colors[0][0]) / (
                        GameInfo.square_size - 1) * i),
                round(Gradient.colors[0][1] + (Gradient.colors[2][1] - Gradient.colors[0][1]) / (
                        GameInfo.square_size - 1) * i),
                round(Gradient.colors[0][2] + (Gradient.colors[2][2] - Gradient.colors[0][2]) / (
                        GameInfo.square_size - 1) * i))
            GameInfo.pixels[i][GameInfo.square_size - 1] = (
                round(Gradient.colors[1][0] + (Gradient.colors[3][0] - Gradient.colors[1][0]) / (
                        GameInfo.square_size - 1) * i),
                round(Gradient.colors[1][1] + (Gradient.colors[3][1] - Gradient.colors[1][1]) / (
                        GameInfo.square_size - 1) * i),
                round(Gradient.colors[1][2] + (Gradient.colors[3][2] - Gradient.colors[1][2]) / (
                        GameInfo.square_size - 1) * i))
        for i in range(GameInfo.square_size - 1):
            for j in range(GameInfo.square_size - 1):
                GameInfo.pixels[i][j] = (
                    round(GameInfo.pixels[i][0][0] + (
                            GameInfo.pixels[i][GameInfo.square_size - 1][0] -
                            GameInfo.pixels[i][0][0]) / (GameInfo.square_size - 1) * j),
                    round(GameInfo.pixels[i][0][1] + (
                            GameInfo.pixels[i][GameInfo.square_size - 1][1] -
                            GameInfo.pixels[i][0][1]) / (GameInfo.square_size - 1) * j),
                    round(GameInfo.pixels[i][0][2] + (
                            GameInfo.pixels[i][GameInfo.square_size - 1][2] -
                            GameInfo.pixels[i][0][2]) / (GameInfo.square_size - 1) * j))

    @staticmethod
    def shuffle():
        color_list = []
        for i in GameInfo.pixels:
            color_list += i
        for i in Gradient.colors:
            color_list.remove(i)
        random.shuffle(color_list)
        cur = 0
        for i in range(GameInfo.square_size):
            for j in range(GameInfo.square_size):
                if (i == 0) + (j == 0) + (i == GameInfo.square_size - 1) + (j == GameInfo.square_size - 1) == 2:
                    GameInfo.pixels[i][j] = Gradient.colors[0]
                    Gradient.colors.pop(0)
                else:
                    GameInfo.pixels[i][j] = color_list[cur]
                    cur += 1


class Game:
    @staticmethod
    def pygame_start():
        GameInfo.screen.fill((71, 71, 71))
        Gradient.create_new_image()
        for i in range(GameInfo.square_size):
            for j in range(GameInfo.square_size):
                pygame.draw.rect(GameInfo.screen, GameInfo.pixels[i][j],
                                 (GameInfo.pixel_size * j, GameInfo.pixel_size * i,
                                  GameInfo.pixel_size, GameInfo.pixel_size))
        pygame.display.flip()
        shfl = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        pygame.image.save(GameInfo.screen, f'Gradient{time.time()}.png')
                    if event.key == pygame.K_r:
                        Gradient.create_new_image()
                        if shfl:
                            Gradient.shuffle()
                        for i in range(GameInfo.square_size):
                            for j in range(GameInfo.square_size):
                                pygame.draw.rect(GameInfo.screen, GameInfo.pixels[i][j],
                                                 (GameInfo.pixel_size * j, GameInfo.pixel_size * i,
                                                  GameInfo.pixel_size, GameInfo.pixel_size))
                        pygame.display.flip()
                    if event.key == pygame.K_h:
                        shfl = not shfl


Game.pygame_start()
Gradient.create_new_image()
