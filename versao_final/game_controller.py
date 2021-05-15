from game_model import GameModel
from game_view import GameView
from configs import *
from time import sleep


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
        self.__game_over = False
        self.__start_playing = False
        self.__win = False

    def run(self):
        self.__modules
        self.load_level()
        # self.__view.music("The_Mandalorian_OST_Main_Theme.mp3", -1)  # view
        while self.__running:
            self.__clock.tick(self.__model.FPS)
            # logica de game over
            while self.__game_over:
                self.events()
                self.warning("GAME OVER")
                pg.display.flip()
                sleep(3)
                self.__game_over = False
                self.__menu = True
            while self.__win:
                self.events()
                self.warning("YOU WIN")
                pg.display.flip()
                sleep(3)
                self.__win = False
                self.__menu = True
            while self.__menu:
                self.events()  # Vou passar para dentro de update *
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

            # logica de comportamento dos inimigos
            if self.__start_playing == True:
                for enemy in self.__level.enemies:
                    enemy.follow_rect(self.__player)
                    self.enemy_attack(enemy)

    def update(self):
        self.physics()
        self.kill_the_dead()
        self.__view.update_scene()

    def load_level(self):
        # posicao do jogador, deve ser carregada de level
        self.__player.pos = self.__level.spawn_point

    def button(self, msg, x, y, w, h, inactive, active, action=None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if (x+w) > mouse[0] > x and (y+h) > mouse[1] > (h):
            pg.draw.rect(self.__view.screen, active, (x, y, w, h))
            if click[0] == 1 and action != None:
                if action == "start":
                    self.__menu = False
                if action == "quit":
                    self.__model.data(True)
                    self.__quit()
                if action == "load":
                    self.__model.data(False)
                    self.__menu = False
                if action == "menu":
                    self.__menu = True
        else:
            pg.draw.rect(self.__view.screen, inactive, (x, y, w, h))

        self.__button, self.__button_rect = self.__view.message(
            BLACK, msg, None, 20, (x+(w/2)), (y+(h/2)))
        self.__view.screen.blit(self.__button, self.__button_rect)

    def menu(self):
        self.__message, self.__message_rect = self.__view.message(
            BLUE, "Baby Yoda's Rescue", None, 100, (WIDTH/2), (HEIGHT/2))
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

    def warning(self, warning):  # "GAME OVER" ou "YOU WIN"
        self.__message, self.__message_rect = self.__view.message(
            RED, warning, None, 100, (WIDTH/2), (HEIGHT/2))

        self.__view.screen.blit(self.__bg, self.__bg.get_rect())
        self.__view.screen.blit(self.__message, self.__message_rect)

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

        if self.__player.health <= 0.0:
            self.__game_over = True
            self.__player.kill()

    def collisions(self):  # Causa a colisão

        def collisions_rect(rect):
            collision_tolerance = 10

            hits_platforms = pg.sprite.spritecollide(
                rect, self.__level.platforms, False, False)

            for platform in hits_platforms:
                if abs(rect.rect.bottom - platform.rect.top) < collision_tolerance:
                    rect.collisions["bottom"] = platform.rect.top
                else:
                    rect.collisions["bottom"] = False

                if abs(rect.rect.top - platform.rect.bottom) < collision_tolerance:
                    rect.collisions["top"] = platform.rect.bottom

                if (abs(rect.rect.left - platform.rect.right) < collision_tolerance):
                    rect.collisions["left"] = platform.rect.right
                else:
                    rect.collisions["left"] = False

                if (abs(rect.rect.right - platform.rect.left) < collision_tolerance):
                    rect.collisions["right"] = platform.rect.left
                else:
                    rect.collisions["right"] = False

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
            self.__win = True

    # define a colisao de ataques
    def attack_collision(self):

        hits = pg.sprite.groupcollide(self.__attacks,
                                      self.__level.enemies, False, False)
        # destroi lazers que batem na plataforma
        pg.sprite.groupcollide(
            self.__attacks, self.__level.platforms, True, False)

        hits_player = pg.sprite.spritecollide(
            self.__player, self.__attacks, False)

        # adiciona eventuais colisoes em player
        for item in hits_player:
            hits.update({item: [self.__player]})

        # itera sobre dict
        for attack, sprite in hits.items():
            # se o ataque nao e do atacante
            if attack.shooter != sprite[0]:
                # diminui vida do sprite atingido
                sprite[0].health -= attack.damage * (random.randint(1, 10)/10)
                attack.kill()

    def enemy_attack(self, enemy):
        random_attack = random.randint(0, 15)
        trooper_imprecision = random.randint(-100, 100)
        if random_attack < 2:
            lazer = self.__model.gen_lazer(
                enemy, self.__player.pos + (trooper_imprecision, trooper_imprecision))
            self.__attacks.add(lazer)
            self.__view.update_attacks()

    def commands(self, event):

        # logica de comandos
        keys = pg.key.get_pressed()

        # Se player se movimentar ou atirar: está jogando
        if self.__player.acc.x != 0 or self.__player.vel.y == self.__player.jump_acc:
            self.start_playing = True

        # seta esquerda
        if keys[pg.K_a]:  # and not self.__player.collisions["left"]:
            self.__player.animation("left")
            self.__player.acc.x = -1 * self.__player.std_acc

        # seta direita
        if keys[pg.K_d]:  # and not self.__player.collisions["right"]:
            self.__player.animation("right")
            self.__player.acc.x = self.__player.std_acc

        if not keys[pg.K_d] and not keys[pg.K_a]:
            self.__player.acc.x = 0

        # logica de salto
        if (keys[pg.K_SPACE] or keys[pg.K_w]) and self.__player.air_timer < 10:
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
