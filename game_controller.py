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

    def load_level(self):
        # posicao do jogador, deve ser carregada de level
        self.__player.pos = self.__level.spawn_point


    def run(self):
        self.__modules
        self.load_level()
        # self.__view.music("The_Mandalorian_OST_Main_Theme.mp3", -1)  # view
        while self.__running:
            self.__clock.tick(self.__model.FPS)
            while self.__view.menu:
                self.events()  # Vou passar para dentro de update *
                self.__view.menu_i()
                pg.display.flip()
            # sincroniza o loop de eventos com o clock
            self.events()  # Vou passar para dentro de update *
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
