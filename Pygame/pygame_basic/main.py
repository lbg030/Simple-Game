import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        
        self.sprites = []
        self.Lsprites = []
        
        self.direction = True
        self.is_animating = False
        
        self.sprites.append(pygame.image.load('메인남캐_Move_01.gif'))
        self.sprites.append(pygame.image.load('메인남캐_Move_02.gif'))
        self.sprites.append(pygame.image.load('메인남캐_Move_03.gif'))
        self.sprites.append(pygame.image.load('메인남캐_Move_04.gif'))
        self.sprites.append(pygame.image.load('메인남캐_Move_05.gif'))
        self.sprites.append(pygame.image.load('메인남캐_Move_06.gif'))
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        
        self.rect = self.image.get_rect()
        
        self.rect.topleft = [pos_x, pos_y]
        
        # R_SQUIR_IMG = pygame.transform.flip(L_SQUIR_IMG,True,False)
        for i in (self.sprites):
            self.Lsprites.append(pygame.transform.flip(i, True, False))    
        
    def animate(self):
        self.is_animating = True
    
    def unanimate(self):
        self.is_animating = False
        
    def update(self):
        if self.is_animating == True:
            if self.direction == True:   
               self.image = self.Lsprites[int(self.current_sprite)]
            
            else:   
                
                self.image = self.sprites[int(self.current_sprite)]
            self.current_sprite += 0.2
                
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280 # 가로
screen_height = 720 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("testing game")

moving_sprites = pygame.sprite.Group()
player = Player(10,screen_height - 120)
moving_sprites.add(player)

running = True
while running :
    
    screen.fill((255,255,255))
    
    # 2. 이벤트 처리 ( 키보드, 마우스 등 )
    for event in pygame.event.get(): # 어떤 이벤트가 발생하는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하면 ( 안쓰면 꺼지지 않음 )
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.direction = True
                player.animate()
                
            elif event.key == pygame.K_LEFT:
                player.direction = False
                player.animate()
                
        if event.type == pygame.KEYUP:
            player.unanimate()
            
    moving_sprites.draw(screen)
    moving_sprites.update()
    
    pygame.display.update() #게임 화면을 다시 그리기 ! (반드시 계속 호출 되어야 되는 부분)
    
    clock.tick(60) #게임 화면의 초당 프레임 수를 설정
    
# 파이게임 종료
pygame.quit()