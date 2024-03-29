import pygame
pygame.init() # 반드시 해줘야 되는 부분

# 화면 크기 
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height)) # 480 * 640

#FPS
clock = pygame.time.Clock()



#배경 이미지 불러오기
background = pygame.image.load("/Users/ibyeong-gwon/Desktop/Git/Simple-Game/Pygame/pygame_basic/pixel.jpg")


# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load("/Users/ibyeong-gwon/Desktop/Git/Simple-Game/Pygame/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기

#중앙으로 위치 시키기
character_x_pos = screen_width / 2 - ( character_width / 2)# 화면 가로의 절반 크기에 해당하는 곳에 위치 ( 가로 )
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 위치 ( 세로 )

# 이동할 좌표
to_x = 0
to_y = 0


# 이동 속도
character_speed = 0.5

# 적 enemy 캐릭터
enemy = pygame.image.load("/Users/ibyeong-gwon/Desktop/Git/Simple-Game/Pygame/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터 가로 크기
enemy_height = enemy_size[1] # 캐릭터 세로 크기
enemy_x_pos = screen_width / 2 - ( enemy_width / 2)# 화면 가로의 절반 크기에 해당하는 곳에 위치 ( 가로 )
enemy_y_pos = screen_height / 2 - (enemy_height / 2 ) # 화면 세로 크기 가장 아래에 해당하는 위치 ( 세로 )


#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

# 이벤트 루프
running = True # 게임이 진행중인지 아닌지 확인하는거 = flag
while running :
    dt = clock.tick(60) #게임 화면의 초당 프레임 수를 설정
    
    # print("FPS : " + str(clock.get_fps())) # 프레임 확인
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하면 ( 안쓰면 꺼지지 않음 )
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌러 졌는지 확인
            
            # 방향키 
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
            
        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    #가로 경계값 처리 ( 맵밖으로 탈출 안하게)
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width- character_width :
        character_x_pos = screen_width- character_width
    
    #세로 경계값 처리 
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    #충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos # rect정보 업데이트
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
        
    # screen.fill((0,0,255)) #RGB 형태로 단색 배경을 채우는 코드
    screen.blit(background, (0,0)) # x,y 좌표가 0,0 // 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 크리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
    
    pygame.display.update() #게임 화면을 다시 그리기 ! (반드시 계속 호출 되어야 되는 부분)
    

# 파이게임 종료
pygame.quit()