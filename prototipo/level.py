class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
 
    def move(self):
        pass

class Level():
    def __init__(self, Player, start_point: tuple, exit_point: tuple, Enemy: object, Item: object, item_pos: tuple, objective: int):
        self.Player: Player
        self.start_point = start_point
        self.exit_point = exit_point
        self.Enemy = Enemy
        self.Item = Item
        self.item_pos = item_pos
        self.objective = objective

    def begin_level(self):

        PT1 = platform()
        P1 = Player()
 
        all_sprites = pygame.sprite.Group()
        all_sprites.add(PT1)
        all_sprites.add(P1)

        platforms = pygame.sprite.Group()
        platforms.add(PT1)


        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_SPACE:
                        fase.Player.jump()

            displaysurface.fill((0,0,0))
            P1.update()

            for entity in all_sprites:
                displaysurface.blit(entity.surf, entity.rect)
                entity.move()

            pygame.display.update()
            FramePerSec.tick(FPS)


    def end_level(self):
        pass

    def check_key(self.Player.itens):
        pass

