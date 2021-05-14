from game_model import GameModel
from game_view import GameView
from configs import *


class GameController:
    def __init__(self):
        self.__model = GameModel()
        self.__sprites = pg.sprite.Group()
        self.__attacks = pg.sprite.Group()
        self.__view = GameView(self.__model.player,
                               self.__model.level,
                               self.__sprites,
                               self.__attacks)
        self.__player = self.__model.player
        self.__level = self.__model.level
        self.__clock = pg.time.Clock()
        # inicializa os modulos do pygame e retorna uma tupla com resultados
        self.__modules = pg.init()
        self.__running = True
        self.__menu = True
        self.__start_playing = False

    def load_level(self):
        # posicao do jogador, deve ser carregada de level
        self.__player.pos = self.__level.spawn_point

    def music(self, music, param):  # view
        pg.mixer.init()
        music = pg.mixer.Sound(music)
        music.play(param)

    def text_objects(self, text, font, color):  # view
        self.__message = font.render(text, True, color)
        return self.__message, self.__message.get_rect()

    def message(self, color, message, font, tamanho, x, y):  # view
        self.__font = pg.font.Font(font, tamanho)
        self.__text, self.__text_rect = self.text_objects(
            message, self.__font, color)
        self.__text_rect.center = (x, y)
        return self.__text, self.__text_rect

    def button(self, msg, x, y, w, h, inactive, active, action=None):  # view
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if (x+w) > mouse[0] > x and (y+h) > mouse[1] > (h):
            pg.draw.rect(self.__view.screen, active, (x, y, w, h))
            if click[0] == 1 and action != None:
                if action == "start":
                    self.__menu = False
                if action == "quit":
                    self.__model.data(True)
                    self.quit()
                if action == "load":
                    self.__model.data(False)
                    self.__menu = False
                if action == "restart":
                    pass
                if action == "save":
                    self.__model.data(True)
        else:
            pg.draw.rect(self.__view.screen, inactive, (x, y, w, h))

        self.__button, self.__button_rect = self.message(
            BLACK, msg, None, 20, (x+(w/2)), (y+(h/2)))
        self.__view.screen.blit(self.__button, self.__button_rect)

    def menu(self):  # view
        self.__message, self.__message_rect = self.message(
            BLUE, "Baby Yoda's Rescue", None, 100, (WIDTH/2), (HEIGHT/2))

        self.events()
        self.__bg = pg.image.load(data + "background-1.png")
        self.__view.screen.blit(self.__bg, self.__bg.get_rect())
        self.__view.screen.blit(self.__message, self.__message_rect)

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

        self.button("RESTART", (HEIGHT/4), (WIDTH/2), 100, 50,
                    AZUL_BONITO, AZUL_BONITO_CLARO, "restart")
        self.button("QUIT", (HEIGHT/4)+(WIDTH/2), (WIDTH/2),
                    100, 50, RED, LIGHT_RED, "quit")

    def win(self):  # view
        self.__message, self.__message_rect = self.message(
            WHITE, "YOU WIN", None, 100, (WIDTH/2), (HEIGHT/2))
        self.__view.screen.blit(self.__message, self.__message_rect)

        self.button("RESTART", (HEIGHT/4), (WIDTH/2), 100, 50,
                    AZUL_BONITO, AZUL_BONITO_CLARO, "restart")
        self.button("QUIT", (HEIGHT/4)+(WIDTH/2), (WIDTH/2),
                    100, 50, RED, LIGHT_RED, "quit")

    def run(self):
        self.__modules
        self.load_level()
        # self.music("The_Mandalorian_OST_Main_Theme.mp3", -1)  # view
        while self.__running:
            self.__clock.tick(self.__model.FPS)
            while self.__menu:
                self.menu()
                pg.display.flip()
            # sincroniza o loop de eventos com o clock
            self.events()
            self.update()
            self.__view.draw()

    # funcao de saida do pygame chamada em caso de fechamento de janela
    def quit(self):
        self.__running = False
        pg.quit()

    def events(self):
        for event in pg.event.get():
            # se fecha a janela termina o programa
            if event.type == pg.QUIT:
                self.__model.data(True)
                self.quit()

            self.commands(event)
            
            if self.__start_playing == True:
                for enemy in self.__level.enemies:
                    enemy.follow_rect(self.__player)

    def update(self):
        self.physics()
        self.kill_the_dead()
        self.__view.update_scene()

    def physics(self):
        self.collisions()
        self.lazer_movement()
        self.attack_collision()

        self.__player.char_physics()

        for enemy in self.__level.enemies:
            enemy.char_physics()


    def lazer_movement(self):
        for lazer in self.__attacks.sprites():
            lazer.pos.x += math.cos(lazer.angle) * lazer.vel
            lazer.pos.y += math.sin(lazer.angle) * lazer.vel
            lazer.rect.center = lazer.pos
        # criar funcao pra destruir lazers
            out_of_border = (lazer.rect.right >= WIDTH or lazer.rect.left <= 0
                             or lazer.rect.bottom >= HEIGHT or lazer.rect.top <= 0)
            if out_of_border:
                lazer.kill()

    def kill_the_dead(self):
        for sprite in self.__level.enemies:
            if sprite.health <= 0:
                sprite.kill()

    def collisions(self):  # Causa a colisão

        def collisions_rect(rect):
            collision_tolerance = 10

            hits_platforms = pg.sprite.spritecollide(rect, self.__level.platforms, False, False)

            for platform in hits_platforms:
                if abs(rect.rect.bottom - platform.rect.top) < collision_tolerance:
                    rect.collisions["bottom"] = platform.rect.top
                    rect.collisions["top"] = False

                if abs(rect.rect.top - platform.rect.bottom) < collision_tolerance:
                    rect.collisions["top"] = platform.rect.bottom
                    rect.collisions["bottom"] = False

                if abs(rect.rect.left - platform.rect.right) < collision_tolerance:
                    rect.collisions["left"] = True
                    rect.collisions["right"] = False

                if abs(rect.rect.right - platform.rect.left) < collision_tolerance:
                    rect.collisions["right"] = True
                    rect.collisions["left"] = False

            if not hits_platforms:
                rect.collisions["bottom"] = False
                rect.collisions["top"] = False
                rect.collisions["right"] = False
                rect.collisions["left"] = False


        collisions_rect(self.__player)
        
        for enemy in self.__level.enemies:
            collisions_rect(enemy)

        # Colisao com itens:
        hits_items = pg.sprite.spritecollide(
            self.__player, self.__level.items, True)
        if hits_items:
            self.__player.key = True

        # Colisao com a saida:
        hits_exit = pg.sprite.spritecollide(
            self.__player, self.__level.exit, False)
        if hits_exit and self.__player.key == True:
            self.quit()  # sai do jogo apos conseguir a chave

    # define a colisao de ataques
    def attack_collision(self):
        hits = pg.sprite.groupcollide(self.__attacks,
                                      self.__level.enemies, True, False)

        # destroi lazers que batem na plataforma
        pg.sprite.groupcollide(
            self.__attacks, self.__level.platforms, True, False)

        # itera sobre dict
        for attack, sprite in hits.items():
            # se o ataque nao e do atacante
            if attack.shooter != sprite:
                # diminui vida do sprite atingido
                sprite[0].health -= attack.damage * (random.randint(1, 10)/10)

    def commands(self, event):

        # logica de comandos
        keys = pg.key.get_pressed()

        # Se player se movimentar ou atirar: está jogando
        if self.__player.acc.x != 0  or self.__player.vel.y == self.__player.jump_acc:
            self.start_playing = True

        # seta esquerda
        if keys[pg.K_a] and not self.__player.collisions["left"]:
            self.__player.animation("left")
            self.__player.acc.x = -1 * self.__player.std_acc

        # seta direita
        if keys[pg.K_d] and not self.__player.collisions["right"]:
            self.__player.animation("right")
            self.__player.acc.x = self.__player.std_acc

        if not keys[pg.K_d] and not keys[pg.K_a]:
            self.__player.acc.x = 0

        # espaco
        if keys[pg.K_SPACE] or keys[pg.K_w] and self.__player.collisions["bottom"]:

            self.__player.vel.y = self.__player.jump_acc

        # clique de mouse mais posicao
        if event.type == pg.MOUSEBUTTONDOWN:
            lazer = self.__model.gen_lazer(self.__player, pg.mouse.get_pos())
            self.__attacks.add(lazer)
            self.__view.update_attacks()

    @ property
    def running(self):
        return self.__running

    @ running.setter
    def running(self, new_value):
        self.__running = new_value

    @ property
    def sprites(self):
        return self.__sprites
    
    @ property
    def start_playing(self):
        return self.__start_playing

    @ start_playing.setter
    def start_playing(self, new_value):
        self.__start_playing = new_value
