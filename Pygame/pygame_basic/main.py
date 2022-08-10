import pygame, sys

                
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280 # 가로
screen_height = 720 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("testing game")



class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        
        # Move sprites
        self.sprites = []
        self.Rsprites = []
        
        self.direction = True
        self.is_animating = False
        self.is_attack = False
        
        self.sprites.append(pygame.image.load('image/메인남캐_Move_01.gif'))
        self.sprites.append(pygame.image.load('image/메인남캐_Move_02.gif'))
        self.sprites.append(pygame.image.load('image/메인남캐_Move_03.gif'))
        self.sprites.append(pygame.image.load('image/메인남캐_Move_04.gif'))
        self.sprites.append(pygame.image.load('image/메인남캐_Move_05.gif'))
        self.sprites.append(pygame.image.load('image/메인남캐_Move_06.gif'))
        
        self.current_sprite = 0
        self.current_attack_sprite = 0
        
        self.image = self.sprites[self.current_sprite]
        
        self.rect = self.image.get_rect()
        self.rect.y = pos_y
        # self.rect.topleft = [pos_x, pos_y]
        
        #----------------------------------------------------------------
        ## 이미지 스케일링 ( 사이즈 조절 )
        # for idx,x in enumerate(self.sprites):
        #     x = pygame.transform.scale(x, (200,100))
        #     self.sprites[idx] = x
        
        # 오른쪽 이미지
        for i in (self.sprites):
            self.Rsprites.append(pygame.transform.flip(i, True, False))    

        # 속도
        self.velocity_x = 0

        #--------------------------------------------------------
        
        # Attack sprites
        self.attack_sprites = []
        self.attack_Rsprites = []
        
        self.attack_sprites.append(pygame.image.load('image/메인남캐_Attack_01.gif'))
        self.attack_sprites.append(pygame.image.load('image/메인남캐_Attack_02.gif'))
        self.attack_sprites.append(pygame.image.load('image/메인남캐_Attack_03.gif'))
        self.attack_sprites.append(pygame.image.load('image/메인남캐_Attack_04.gif'))
        self.attack_sprites.append(pygame.image.load('image/메인남캐_Attack_05.gif'))
        self.attack_sprites.append(pygame.image.load('image/메인남캐_Attack_06.gif'))
        self.attack_sprites.append(pygame.image.load('image/메인남캐_Attack_07.gif'))
        self.attack_sprites.append(pygame.image.load('image/메인남캐_Attack_08.gif'))
        
        for i in (self.attack_sprites):
            self.attack_Rsprites.append(pygame.transform.flip(i, True, False))  
        
    def animate(self):
        self.is_animating = True
        self.velocity_x = 2
        
    def unanimate(self):
        self.is_animating = False
        self.is_attack = False
        self.velocity_x = 0
        
    def update(self):
        # 좌우 이동
        if self.is_animating == True: 
            if self.direction == True:    # 오른쪽
               self.image = self.Rsprites[int(self.current_sprite)]
               
            else:       #왼쪽
                self.image = self.sprites[int(self.current_sprite)]
                self.velocity_x = abs(self.velocity_x ) * -1
            
            self.current_sprite += 0.2
            
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                
            
            self.rect.x += self.velocity_x

        # 공격
        if self.is_attack == True:
            self.velocity_x = 0
            
            if self.direction == True:
                self.image = self.attack_Rsprites[int(self.current_attack_sprite)]

            else :
                self.image = self.attack_sprites[int(self.current_attack_sprite)]
                
            self.current_attack_sprite += 0.2
                
            if self.current_attack_sprite >= len(self.attack_sprites):
                self.current_attack_sprite = 0
                self.unanimate()

# 스테이지
stage = pygame.image.load("stage.png")
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이 위에 캐릭터를 두기 위해 사용


character = pygame.image.load("image/메인남캐_Move_01.gif")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height - character_height - stage_height)

# 캐릭터 움직임
moving_sprites = pygame.sprite.Group()
player = Player(10,screen_height - stage_height - character_height)
moving_sprites.add(player)


# 러닝
running = True
while running :
    
    screen.fill((0,0,0))
    
    # 2. 이벤트 처리 ( 키보드, 마우스 등 )
    for event in pygame.event.get(): # 어떤 이벤트가 발생하는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하면 ( 안쓰면 꺼지지 않음 )
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.direction = True
                player.animate()
                
            if event.key == pygame.K_LEFT:
                player.direction = False
                player.animate()
            if event.key == pygame.K_SPACE:
                player.is_attack = True
                player.animate()
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.unanimate()

    if player.rect.x < 0:
        player.rect.x = 0
        
    elif player.rect.x > screen_width - character_width:
        player.rect.x = screen_width - character_width
    
    
    
    screen.blit(stage, (0, screen_height - stage_height))
    
    moving_sprites.draw(screen)
    moving_sprites.update()
    
    
    pygame.display.update() #게임 화면을 다시 그리기 ! (반드시 계속 호출 되어야 되는 부분)
    
    clock.tick(60) #게임 화면의 초당 프레임 수를 설정
    
# 파이게임 종료
pygame.quit()