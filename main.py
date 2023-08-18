import random
import time
import pygame


class GameInfo:
    pygame.display.set_caption('Gradient colors')
    size = 800, 800
    screen = pygame.display.set_mode(size)
    level_pixel_sizes = [200, 160, 100, 80, 50, 40, 32, 25, 20]
    pixel_size = level_pixel_sizes[0]
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
    solved_gradient = None
    selected1, selected2 = None, None

    @staticmethod
    def create_new_image():
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
        Gradient.solved_gradient = [i[::] for i in GameInfo.pixels]

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
                if (i == 0) + (j == 0) + (i == GameInfo.square_size - 1) + (
                        j == GameInfo.square_size - 1) == 2:
                    GameInfo.pixels[i][j] = Gradient.colors[0]
                    Gradient.colors.pop(0)
                else:
                    GameInfo.pixels[i][j] = color_list[cur]
                    cur += 1


def draw():
    for i in range(GameInfo.square_size):
        for j in range(GameInfo.square_size):
            pygame.draw.rect(GameInfo.screen, GameInfo.pixels[i][j], (
                GameInfo.pixel_size * j, GameInfo.pixel_size * i, GameInfo.pixel_size,
                GameInfo.pixel_size))
    if Gradient.selected1:
        pygame.draw.rect(GameInfo.screen, Gradient.selected1[0], (
            GameInfo.pixel_size * Gradient.selected1[1][1] - 10,
            GameInfo.pixel_size * Gradient.selected1[1][0] - 10,
            GameInfo.pixel_size + 20, GameInfo.pixel_size + 20))
    pygame.display.flip()


class Game:
    @staticmethod
    def pygame_start():
        GameInfo.screen.fill((71, 71, 71))
        Gradient.create_new_image()
        draw()
        shfl = False
        solved = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if GameInfo.pixels[event.pos[1] // GameInfo.pixel_size][
                            event.pos[0] // GameInfo.pixel_size] not in Gradient.colors:
                            if not Gradient.selected1:
                                Gradient.selected1 = (
                                    GameInfo.pixels[event.pos[1] // GameInfo.pixel_size][
                                        event.pos[0] // GameInfo.pixel_size],
                                    (event.pos[1] // GameInfo.pixel_size,
                                     event.pos[0] // GameInfo.pixel_size))
                                draw()
                            elif event.pos != Gradient.selected1[1]:
                                Gradient.selected2 = (
                                    GameInfo.pixels[event.pos[1] // GameInfo.pixel_size][
                                        event.pos[0] // GameInfo.pixel_size],
                                    (event.pos[1] // GameInfo.pixel_size,
                                     event.pos[0] // GameInfo.pixel_size))
                                GameInfo.pixels[Gradient.selected1[1][0]][Gradient.selected1[1][1]], \
                                    GameInfo.pixels[Gradient.selected2[1][0]][
                                        Gradient.selected2[1][1]] = \
                                    GameInfo.pixels[Gradient.selected2[1][0]][
                                        Gradient.selected2[1][1]], \
                                        GameInfo.pixels[Gradient.selected1[1][0]][
                                            Gradient.selected1[1][1]]
                                Gradient.selected1, Gradient.selected2 = None, None
                                draw()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        pygame.image.save(GameInfo.screen, f'Gradient{time.time()}.png')
                    if event.key == pygame.K_r:
                        Gradient.create_new_image()
                        solved = False
                        if shfl:
                            Gradient.shuffle()
                        draw()
                    if event.key == pygame.K_h:
                        shfl = not shfl
                    if event.key == pygame.K_f:
                        if pygame.display.get_window_size() == GameInfo.size:
                            pygame.display.set_mode(GameInfo.size, pygame.FULLSCREEN)
                        else:
                            pygame.display.set_mode(GameInfo.size)
                        draw()
                    if event.key == pygame.K_1:
                        print(1)
                        GameInfo.pixel_size = GameInfo.level_pixel_sizes[0]
                    if event.key == pygame.K_2:
                        GameInfo.pixel_size = GameInfo.level_pixel_sizes[1]
                    if event.key == pygame.K_3:
                        GameInfo.pixel_size = GameInfo.level_pixel_sizes[2]
                    if event.key == pygame.K_4:
                        GameInfo.pixel_size = GameInfo.level_pixel_sizes[3]
                    if event.key == pygame.K_5:
                        GameInfo.pixel_size = GameInfo.level_pixel_sizes[4]
                    if event.key == pygame.K_6:
                        GameInfo.pixel_size = GameInfo.level_pixel_sizes[5]
                    if event.key == pygame.K_7:
                        GameInfo.pixel_size = GameInfo.level_pixel_sizes[6]
                    if event.key == pygame.K_8:
                        GameInfo.pixel_size = GameInfo.level_pixel_sizes[7]
                    if event.key == pygame.K_9:
                        GameInfo.pixel_size = GameInfo.level_pixel_sizes[8]
            if solved is False and GameInfo.pixels == Gradient.solved_gradient:
                solved = True
                GameInfo.screen.fill((0, 255, 0))
                pygame.display.flip()
                pygame.time.delay(1000)
                draw()


Game.pygame_start()
