from configs import *

class GameView:
    def __init__(self, player, level, sprites, attacks):
        self.__screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.__player = player
        self.__level = level
        self.__sprites = sprites
        self.__caption = pg.display.set_caption(TITULO)
        self.__attacks = attacks
        self.__background = pg.image.load(
            data + "background-1.png")  # provisorio MUDAR ENDERECO
        self.__bg_x = 0
        self.__rel_x = None

    def draw(self):
        self.bg_movement()
        # desenha todos os sprites OTIMIZAR para sprites individuais
        self.__sprites.draw(self.__screen)
        # realiza o flip apos desenhar tudo
        self.__screen_health = self.message(
            WHITE, "HEALTH = "+str(self.__player.health), None, 30, 80, 20)
        self.__screen.blit(self.__screen_health[0], self.__screen_health[1])
        pg.display.flip()

    def update_attacks(self):
        self.__sprites.add(self.__attacks)

    def bg_movement(self):
        # lógica do movimento do background
        self.__rel_x = self.__bg_x % self.__background.get_rect().width  # avaliar repeticoes
        self.__screen.blit(self.__background, [
            self.__rel_x - self.__background.get_rect().width, 0])
        # replicacao do bg
        if self.__rel_x < WIDTH:
            self.__screen.blit(self.__background, (self.__rel_x, 0))
        # movimento do bg
        self.__bg_x -= 1

    def update_scene(self):
        # Adiciona sprites ao grupo principal de sprites
        self.__sprites.add(
            self.__player, self.__level.platforms,
            self.__level.items, self.__level.exit,
            self.__level.enemies, self.__attacks)
        if (self.__player.pos.x - (self.__player.size[0]/2)) < 0:
            self.__level.back()
            self.__level.update()
            self.__player.pos.x = self.__player.pos.x + WIDTH

        if (self.__player.pos.x - (self.__player.size[0]/2) > WIDTH):
            self.__level.next()
            self.__level.update()
            # varia, cuidar com os pixeis de cada fase
            self.__player.pos.x = self.__player.pos.x - WIDTH

    def text_objects(self, text, font, color):
        self.__message = font.render(text, True, color)
        return self.__message, self.__message.get_rect()

    def message(self, color, message, font, tamanho, x, y):
        self.__font = pg.font.Font(font, tamanho)
        self.__text, self.__text_rect = self.text_objects(
            message, self.__font, color)
        self.__text_rect.center = (x, y)
        return self.__text, self.__text_rect

    def music(self, music, param):
        pg.mixer.init()
        music = pg.mixer.Sound(music)
        music.play(param)

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, scr):
        self.__screen = scr