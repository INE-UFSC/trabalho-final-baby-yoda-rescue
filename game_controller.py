from game_model import GameModel
from game_view import GameView
from configs import *


def collision_types(rect, tiles):  # quem se move, movimento, com quem pode se colidir
    # dicionário pra saber com que lado se colidiu
    collision_types = {'top': False, 'bottom': False,
                       'right': False, 'left': False}
    movement = rect.vel
    # Movimento em X:
    hit_list = tiles  # tile vai ser a classe dos blocos
    for tile in hit_list:
        if movement[0] > 0:  # ou seja se movendo para a direita
            # rect.right = tile.rect.left  # deve ir para dentro de fisica
            collision_types['right'] = True
        elif movement[0] < 0:
            # rect.left = tile.rect.right
            collision_types['left'] = True

    # Movimento em Y:
    hit_list = tiles
    tile = ''
    for tile in hit_list:
        if movement[1] > 0:  # ou seja se movendo para a direita
            # rect.bottom = tile.rect.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            # rect.top = tile.rect.bottom
            collision_types['top'] = True

    return collision_types

# Move o personagem a partir das colisões que ele teve


"""def collision_movement(rect, tiles):  # Causa a colisão
    colided = collision_types(rect, tiles)
    print(colided)
    if colided[0]['right']:
        print('colided --- RIGHT ---')
        rect.vel.x = 0
        rect.right = colided[1].rect.left
    if colided[0]['left']:
        print('colided --- LEFT ---')
        rect.vel.x = 0
        rect.left = colided[1].rect.right
    if colided[0]['bottom']:
        print('colided --- BOTTOM ---')
        rect.vel.y = -5
        rect.bottom = colided[1].rect.top
    if colided[0]['top']:
        print('colided --- TOP ---')
        rect.vel.y = 0
        rect.top = colided[1].rect.bottom
"""


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

    def load_level(self):
        # posicao do jogador, deve ser carregada de level
        self.__player.pos = self.__level.spawn_point

    def music(self, music, param):
        pg.mixer.init()
        music = pg.mixer.Sound(music)
        music.play(param)

    def text_objects(self, text, font, color):
        self.__message = font.render(text, True, color)
        return self.__message, self.__message.get_rect()

    def message(self, color, message, font, tamanho, x, y):
        self.__font = pg.font.Font(font, tamanho)
        self.__text, self.__text_rect = self.text_objects(message, self.__font, color)
        self.__text_rect.center = (x, y)
        return self.__text, self.__text_rect

    def button(self, msg, x,y,w,h,inactive,active, action=None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if (x+w) > mouse[0] > x and (y+h) > mouse[1] > (h):
            pg.draw.rect(self.__view.screen,active,(x,y,w,h))
            if click[0] == 1 and action != None:
                if action == "start":
                    self.__menu = False
                if action == "quit":
                    self.quit()
        else:
            pg.draw.rect(self.__view.screen,inactive,(x,y,w,h))

        self.__button, self.__button_rect = self.message(BLACK, msg, None, 20, (x+(w/2)), (y+(h/2)))
        self.__view.screen.blit(self.__button, self.__button_rect)

    def menu(self):
        self.__message, self.__message_rect = self.message(BLUE, "Baby Yoda's Rescue", None, 100,(WIDTH/2),(HEIGHT/2))

        self.events()
        self.__bg = pg.image.load(data + "background-1.png")
        self.__view.screen.blit(self.__bg, self.__bg.get_rect())
        self.__view.screen.blit(self.__message, self.__message_rect)

        self.button("START", (HEIGHT/4), (WIDTH/2), 100, 50, AZUL_BONITO, AZUL_BONITO_CLARO, "start")
        self.button("QUIT", (HEIGHT/4)+(WIDTH/2), (WIDTH/2), 100, 50, RED, LIGHT_RED, "quit")


    def game_over(self):
        self.__message, self.__message_rect = self.message(RED, "GAME OVER", None, 100, (WIDTH/2), (HEIGHT/2))
        self.__view.screen.blit(self.__message, self.__message_rect)

        self.button("RESTART", (HEIGHT/4), (WIDTH/2), 100, 50, AZUL_BONITO, AZUL_BONITO_CLARO, "restart")
        self.button("QUIT", (HEIGHT/4)+(WIDTH/2), (WIDTH/2), 100, 50, RED, LIGHT_RED, "quit")


    def win(self):
        self.__message, self.__message_rect = self.message(WHITE, "YOU WIN", None, 100, (WIDTH/2), (HEIGHT/2))
        self.__view.screen.blit(self.__message, self.__message_rect)

        self.button("RESTART", (HEIGHT/4), (WIDTH/2), 100, 50, AZUL_BONITO, AZUL_BONITO_CLARO, "restart")
        self.button("QUIT", (HEIGHT/4)+(WIDTH/2), (WIDTH/2), 100, 50, RED, LIGHT_RED, "quit")


    def run(self):
        self.__modules
        self.load_level()
        #self.music("The_Mandalorian_OST_Main_Theme.mp3", -1)  # view
        while self.__running:
            self.__clock.tick(self.__model.FPS)
            while self.__menu:
                self.menu()
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
                self.quit()

            self.commands(event)

    def update(self):
        self.physics()  # events vão para dentro de physics *
        self.collisions()
        self.kill_the_dead()
        self.__view.update_scene()

    def physics(self):
        # movimenta os lazers a partir do tempo
        self.lazer_movement()
        self.attack_collision()

        # Updates do player:
        # Posição do player marcada como ponto do meio inferior
        self.__player.rect.midbottom = self.__player.pos

        if not self.__player.collisions["bottom"]:
            self.__player.acc += self.__player.vec(
                0, 0.01)  # adiciona gravidade a y

        if self.__player.collisions["bottom"]:
            self.__player.acc.y = 0
            self.__player.vel.y = 0
            self.__player.pos.y -= 1

        """        if self.__player.collisions["left"]:
            self.__player.acc.x = 0
            self.__player.vel.x = 0"""

        # decrementar a aceleração em x
        # self.__player.acc.x += self.__player.vel.x * self.__player.fric
        # print(
        #    f'------ PHYSICS------\nself.__player.vel: {self.__player.vel}\nself.__player.acc: {self.__player.acc}')

        self.__player.acc.x += self.__player.vel.x * self.__player.fric
        self.__player.vel += self.__player.acc

        self.__player.pos += self.__player.vel + 0.5 * self.__player.acc
        print(self.__player.vel.x, self.__player.fric,
              self.__player.vel.x * self.__player.fric)

        if self.__player.vel.x > 2:
            self.__player.vel.x = 2
        if self.__player.vel.x < -2:
            self.__player.vel.x = -2

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

        collision_tolerance = 10

        hits_platforms = pg.sprite.spritecollide(
            self.__player, self.__level.platforms, False, False)

        for platform in hits_platforms:
            if abs(self.__player.rect.bottom - platform.rect.top) < collision_tolerance:
                self.__player.collisions["bottom"] = True
                self.__player.collisions["top"] = False

            if abs(self.__player.rect.top - platform.rect.bottom) < collision_tolerance:
                self.__player.collisions["top"] = True
                self.__player.collisions["bottom"] = False
            if abs(self.__player.rect.left - platform.rect.right) < collision_tolerance:
                self.__player.collisions["left"] = True
                self.__player.collisions["right"] = False
            if abs(self.__player.rect.right - platform.rect.left) < collision_tolerance:
                self.__player.collisions["right"] = True
                self.__player.collisions["left"] = False

        if not hits_platforms:
            self.__player.collisions["bottom"] = False
            self.__player.collisions["top"] = False
            self.__player.collisions["right"] = False
            self.__player.collisions["left"] = False

        # Colisao com itens:
        hits_items = pg.sprite.spritecollide(
            self.__player, self.__level.items, True)
        if hits_items:
            self.__player.key = True
            # print('self.__player.key:', self.__player.key)

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

        # espaco
        if keys[pg.K_SPACE] or keys[pg.K_w] and self.__player.collisions["bottom"]:

            self.__player.vel.y = self.__player.jump_acc

        # clique de mouse mais posicao
        if event.type == pg.MOUSEBUTTONDOWN:
            lazer = self.__model.gen_lazer(self.__player,
                                           self.__player.rect.center, pg.mouse.get_pos())
            self.__attacks.add(lazer)
            self.__view.update_attacks()
        # print(
        #    f'-------- EVENTS --------\nself.__player.vel: {self.__player.vel}\nself.__player.acc: {self.__player.acc}')

    @ property
    def running(self):
        return self.__running

    @ running.setter
    def running(self, new_value):
        self.__running = new_value

    @ property
    def sprites(self):
        return self.__sprites
