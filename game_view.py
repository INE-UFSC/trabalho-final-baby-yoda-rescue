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
        self.__menu = True
        self.__data_active = True
        self.__data_signal = False
        self.__quit = False

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

    def button(self, msg, x, y, w, h, inactive, active, action=None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if (x+w) > mouse[0] > x and (y+h) > mouse[1] > (h):
            pg.draw.rect(self.__screen, active, (x, y, w, h))
            if click[0] == 1 and action != None:
                if action == "start":
                    self.__menu = False
                if action == "quit":
                    self.__data_active = True
                    self.__data_signal = True
                    self.__quit = True
                if action == "load":
                    self.__data_active = True
                    self.__data_signal = False
                    self.__menu = False
                if action == "menu":
                    self.__menu = True
        else:
            pg.draw.rect(self.__screen, inactive, (x, y, w, h))

        self.__button, self.__button_rect = self.message(
            BLACK, msg, None, 20, (x+(w/2)), (y+(h/2)))
        self.__screen.blit(self.__button, self.__button_rect)

    def menu_i(self):  # view
        self.__message, self.__message_rect = self.message(
            BLUE, "Baby Yoda's Rescue", None, 100, (WIDTH/2), (HEIGHT/2))
        self.__bg = pg.image.load(data + "background-1.png")
        self.__screen.blit(self.__bg, self.__bg.get_rect())
        self.__screen.blit(self.__message, self.__message_rect)

        self.button("START", (HEIGHT/4)+30, (WIDTH/2), 100, 50,
                    AZUL_BONITO, AZUL_BONITO_CLARO, "start")
        self.button("LOAD", (HEIGHT/4)+200, (WIDTH/2), 100,
                    50, AZUL_BONITO, AZUL_BONITO_CLARO, "load")
        self.button("QUIT", (HEIGHT/4)+(WIDTH/2)-30,
                    (WIDTH/2), 100, 50, RED, LIGHT_RED, "quit")

    def pause(self):
        pass

    def game_over(self):  # view
        self.__message, self.__message_rect = self.message(
            RED, "GAME OVER", None, 100, (WIDTH/2), (HEIGHT/2))
        self.__view.screen.blit(self.__message, self.__message_rect)

        self.button("MENU", (HEIGHT/4), (WIDTH/2), 100, 50,
                    AZUL_BONITO, AZUL_BONITO_CLARO, "menu")
        self.button("QUIT", (HEIGHT/4)+(WIDTH/2), (WIDTH/2),
                    100, 50, RED, LIGHT_RED, "quit")

    def win(self):  # view
        self.__message, self.__message_rect = self.message(
            WHITE, "YOU WIN", None, 100, (WIDTH/2), (HEIGHT/2))
        self.__screen.blit(self.__message, self.__message_rect)

        self.button("MENU", (HEIGHT/4), (WIDTH/2), 100, 50,
                    AZUL_BONITO, AZUL_BONITO_CLARO, "menu")
        self.button("QUIT", (HEIGHT/4)+(WIDTH/2), (WIDTH/2),
                    100, 50, RED, LIGHT_RED, "quit")

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, scr):
        self.__screen = scr

    @property
    def menu(self):
        return self.__menu

    @property
    def data_active(self):
        return self.__data_active

    @property
    def data_active(self):
        return self.__data_signal

    @property
    def quit(self):
        return self.__quit
