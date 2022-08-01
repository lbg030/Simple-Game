import random
import pygame
#----------------------------------------------------------------#

# 기본 초기화 ( 반드시 해야 할 것들 )
pygame.init() # 반드시 해줘야 되는 부분

# 화면 크기 
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height)) # 480 * 640

#화면 타이틀 설정
pygame.display.set_caption("ddong Game") #게임 이름

#FPS
clock = pygame.time.Clock()

#--------------------------------------------------------#

# 1. 사용자 게임 초기화( 배경화면, 게임 이미지, 좌표, 속도, 폰트 등 )

#배경 만들기
background = pygame.image.load("/Users/ibyeong-gwon/Desktop/Git/Simple-Game/Pygame/pygame_basic/pixel.jpg")

#캐릭터 만들기
character = pygame.image.load("/Users/ibyeong-gwon/Desktop/Git/Simple-Game/Pygame/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - ( character_width / 2)# 화면 가로의 절반 크기에 해당하는 곳에 위치 ( 가로 )
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 위치 ( 세로 )

#이동 위치
to_x = 0
character_speed = 10

# 똥 만들기
enemy = pygame.image.load("/Users/ibyeong-gwon/Desktop/Git/Simple-Game/Pygame/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터 가로 크기
enemy_height = enemy_size[1] # 캐릭터 세로 크기
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 4

running = True # 게임이 진행중인지 아닌지 확인하는거 = flag
while running :
    dt = clock.tick(60) #게임 화면의 초당 프레임 수를 설정
    # print("FPS : " + str(clock.get_fps())) # 프레임 확인
    
    # 2. 이벤트 처리 ( 키보드, 마우스 등 )
    for event in pygame.event.get(): # 어떤 이벤트가 발생하는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하면 ( 안쓰면 꺼지지 않음 )
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌러 졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
                
        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤 # 이부분 주석처리하면 한방향으로 계속 이동
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x
    
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height :
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        
    # 4. 충돌 처리
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
        
    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 크리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    pygame.display.update() #게임 화면을 다시 그리기 ! (반드시 계속 호출 되어야 되는 부분)
    
pygame.time.delay(2000) # 2초 정도 대기 (ms)
# 파이게임 종료
pygame.quit()